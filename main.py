import time
from avl import AVL
from avl import separar_palavras

class IndiceRemissivoAVL:
    def __init__(self):
        self.avl = AVL()
        self.total = 0
        self.distintas_lista = []
        self.repetidas = 0
        self.tempo = 0

    def construir_indice(self, nome_arquivo):
        inicio = time.time()

        try:
            arq = open(nome_arquivo, 'r', encoding='utf-8')
            linhas = arq.readlines()
            arq.close()

            for i in range(len(linhas)):
                palavras = separar_palavras(linhas[i])
                for p in palavras:
                    self.total += 1
                    if p not in self.distintas_lista:
                        self.distintas_lista.append(p)
                    else:
                        self.repetidas += 1
                    self.avl.insere(p, i + 1)
            self.tempo = time.time() - inicio
        except FileNotFoundError:
            print("Arquivo não encontrado!")

    def remove_palavra(self, palavra, linha):
        nova_raiz = self.avl.remove(self.avl.get_raiz(), palavra, linha)
        self.avl._AVL__raiz = nova_raiz

    def busca_aproximada(self, prefixo):
        lista = []
        self.avl.buscaPrefixo(self.avl.get_raiz(), prefixo, lista)
        return lista
    
    def buscar_me_palavra(self, palavra):
        return self.avl.buscar_me(self.avl.get_raiz(), palavra)
        
    def palavra_mais_frequente(self):
        lista = self.avl.emOrdem()
        if not lista:
            return "Nenhuma palavra processada."
        maior = None
        max_linhas = -1
        for no in lista:
            if len(no.linhas) > max_linhas:
                max_linhas = len(no.linhas)
                maior = no.palavra
        return maior
    
    def gerar_arquivo_indice(self, nome_saida):
        lista_nos = self.avl.emOrdem()
        if not lista_nos:
            return

        arq = open(nome_saida, 'w', encoding='utf-8')
        arq.write("Índice Remissivo:\n")
        for no in lista_nos:
            linhas_originais = no.linhas
            linhas_unicas = []
            if len(linhas_originais) > 0:
                linhas_unicas.append(linhas_originais[0])

                for i in range(1, len(linhas_originais)):
                    if linhas_originais[i] != linhas_originais[i-1]:
                        linhas_unicas.append(linhas_originais[i])
            str_linhas = ""
            for i in range(len(linhas_unicas)):
                str_linhas += str(linhas_unicas[i])
                if i < len(linhas_unicas) - 1:
                    str_linhas += ","
            
            arq.write(f"{no.palavra}: {str_linhas}\n")

        arq.write("\n")
        arq.write(f"Total de palavras: {self.total}\n")
        arq.write(f"Palavras distintas: {len(self.distintas_lista)}\n")
        arq.write(f"Palavras descartadas (repetidas): {self.repetidas}\n")
        arq.write(f"Tempo de construção: {self.tempo:.4f}s\n")
        arq.write(f"Total de rotações AVL: {self.avl.rotacoes}\n")
        arq.close()


if __name__ == '__main__':
    indice = IndiceRemissivoAVL()
    indice.construir_indice("entrada.txt")


    print("\n--- Teste de busca (ME) ---")
    resposta = indice.buscar_me_palavra("mia")
    if resposta == -1:
        print("Palavra não encontrada")
    elif resposta == 0:
        print("Palavra encontrada. ME = 0(árvore balanceada)")
    elif resposta == 1:
        print("Palavra encontrada e possui desequilíbrio")


    print("Busca aproximada:", indice.busca_aproximada('ab'))
    print("Palavra mais frequente:", indice.palavra_mais_frequente())

    indice.gerar_arquivo_indice("indice.txt")
    print("Arquivo 'indice.txt' gerado com sucesso.")