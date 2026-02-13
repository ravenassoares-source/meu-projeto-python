from no import NOAVL

class AVL:
    def __init__(self):
        self.__raiz = None
        self.rotacoes = 0

    def get_raiz(self):
        return self.__raiz
    
    def __alturaNO(self, no):
        if (no == None):
            return -1
        else:
            return no.altura

    def __fatorBalanceamento_NO(self, no):
        if (no == None):
            return 0
        return self.__alturaNO(no.esq) - self.__alturaNO(no.dir)
    
    def __maior(self, n1, n2):
        if n1 > n2:
            return n1
        else:
            return n2
                
    def __RotacaoLL(self, A):
        B = A.esq
        A.esq = B.dir
        B.dir = A
        A.altura = self.__maior(self.__alturaNO(A.esq),self.__alturaNO(A.dir)) + 1
        B.altura = self.__maior(self.__alturaNO(B.esq),A.altura) + 1
        self.rotacoes += 1
        return B

    def __RotacaoRR(self, A):
        B = A.dir
        A.dir = B.esq
        B.esq = A
        A.altura = self.__maior(self.__alturaNO(A.esq),self.__alturaNO(A.dir)) + 1
        B.altura = self.__maior(self.__alturaNO(B.dir),A.altura) + 1
        self.rotacoes += 1
        return B

    def __RotacaoLR(self, A):
        A.esq = self.__RotacaoRR(A.esq)
        A = self.__RotacaoLL(A)
        self.rotacoes += 1
        return A

    def __RotacaoRL(self, A):
        A.dir = self.__RotacaoLL(A.dir)
        A = self.__RotacaoRR(A)
        self.rotacoes += 1
        return A
    
    def insere(self, palavra, linha):
        self.__raiz = self.__insereNO(self.__raiz, palavra, linha)

    def __insereNO(self, atual, palavra, linha):
        if atual is None:
            novo = NOAVL(palavra, linha)
            novo.linhas.append(linha)
            return novo

        if palavra < atual.palavra:
            atual.esq = self.__insereNO(atual.esq, palavra, linha)
        elif palavra > atual.palavra:
            atual.dir = self.__insereNO(atual.dir, palavra, linha)
        else:
            if linha not in atual.linhas:
                atual.linhas.append(linha)
            return atual

        # Atualiza altura e retorna sempre o nó atual
        atual.altura = self.__maior(self.__alturaNO(atual.esq), self.__alturaNO(atual.dir)) + 1
        
        fb = self.__fatorBalanceamento_NO(atual)

        if fb >= 2:
            if palavra < atual.esq.palavra:
                return self.__RotacaoLL(atual)
            else:
                return self.__RotacaoLR(atual)
        
        if fb <= -2:
            if palavra > atual.dir.palavra:
                return self.__RotacaoRR(atual)
            else:
                return self.__RotacaoRL(atual)
            
        return atual
    
    def __procuraMenor(self, atual):
        no1 = atual
        no2 = atual.esq
        while(no2 != None):
            no1 = no2
            no2 = no2.esq
        return no1
    
    def remove(self, palavra, linha):
        self.__raiz = self.__removeNO(self.__raiz, palavra, linha)
    
    def __removeNO(self, atual, palavra, linha):
        if(atual == None):
            return None
        
        if palavra < atual.palavra:
            atual.esq = self.__removeNO(atual.esq, palavra, linha)
        elif palavra > atual.palavra:
            atual.dir = self.__removeNO(atual.dir, palavra, linha)
        else:
            if linha in atual.linhas:
                atual.linhas.remove(linha)

            if len(atual.linhas) > 0:
                return atual

            if not atual.esq:
                return atual.dir
            elif not atual.dir:
                return atual.esq

            temp = self.__procuraMenor(atual.dir)
            atual.palavra = temp.palavra
            atual.linhas = temp.linhas
            atual.dir = self.__removeNO(atual.dir, temp.palavra, temp.linhas[0])

        
        atual.altura = self.__maior(self.__alturaNO(atual.esq), self.__alturaNO(atual.dir)) + 1
        fb = self.__fatorBalanceamento_NO(atual)

        if fb >=2:
            if self.__fatorBalanceamento_NO(atual.esq) >= 0:
                return self.__RotacaoLL(atual)
            else:
                return self.__RotacaoLR(atual)
            
        if fb <= -2:
            if self.__fatorBalanceamento_NO(atual.dir) <= 0:
                return self.__RotacaoRR(atual)
            else:
                return self.__RotacaoRL(atual)

        return atual

    def emOrdem(self):
        lista = []
        if (self.__raiz != None):
            self.__emOrdem(self.__raiz, lista)
        return lista

    def __emOrdem(self, atual, lista):
        if atual:
            self.__emOrdem(atual.esq, lista)
            lista.append(atual)
            self.__emOrdem(atual.dir, lista)

    def contar_nos(self, atual):
        if atual is None:
            return 0
        return 1 + self.contar_nos(atual.esq) + self.contar_nos(atual.dir)
    
    def buscar_me(self, atual, palavra):
        if not atual:
            return -1
        if palavra == atual.palavra:
            me = self.contar_nos(atual.esq) - self.contar_nos(atual.dir)
            print(f"Valor do ME para '{palavra}': {me}")
            if me == 0:
                return 0
            else:
                return 1
        elif palavra < atual.palavra:
            return self.buscar_me(atual.esq, palavra)
        else:
            return self.buscar_me(atual.dir, palavra)

    
    def __compararPrefixo(self, palavra, prefixo):
        if len(prefixo) > len(palavra):
            return False
        for i in range(len(prefixo)):
            if palavra[i] != prefixo[i]:
                return False
        return True
    
    def buscaPrefixo(self, atual, prefixo, lista):
        if atual:
            if self.__compararPrefixo(atual.palavra, prefixo):
                lista.append(atual.palavra)
            self.buscaPrefixo(atual.esq, prefixo, lista)
            self.buscaPrefixo(atual.dir, prefixo, lista)

def eh_letra(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or c in 'áàâãéèêíóôõúçñÁÀÂÃÉÈÊÍÓÔÕÚÇÑ'

def separar_palavras(linha):
    palavras = []
    atual = ''
    for c in linha:
        if eh_letra(c):
            atual += c.lower()
        else:
            if atual:
                palavras.append(atual)
                atual = ''
    if atual:
        palavras.append(atual)
    return palavras