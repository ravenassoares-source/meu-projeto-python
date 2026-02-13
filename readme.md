------Índice Remissivo usando AVL
Vinícius Gabriel Dias - 12111GIN045
Ravena Sarmento Soares - 12211GIN040
------

------ Introdução
O presente trabalho tem como objetivo o desenvolvimento de um índice remissivo automático, capaz de identificar e organizar as palavras presentes em um arquivo texto, indicando as respectivas linhas em que cada termo ocorre. Para garantir eficiência nas operações de inserção, remoção e busca, foi adotada a estrutura de dados árvore AVL, uma variação da árvore binária de busca que procura manter seu balanceamento automático.
A solução foi projetada de forma a processar o texto linha por linha, extrair as palavras válidas e inseri-las na árvore AVL, fazendo associação de cada palavra a uma lista de linhas. Dessa forma, é obtido um índice em ordem alfabética, trazendo eficiência mesmo para arquivos extensos.

------ Estruturas de Dados Utilizadas
A principal estrutura de dados utilizada foi a árvore AVL, escolhida devido à sua propriedade de balanceamento automático, que assegura complexidade logarítmica nas operações fundamentais. Cada nó da árvore armazena uma palavra e uma lista contendo as linhas em que ela aparece, permitindo a construção de um índice remissivo completo e organizado.
Além disso, foram utilizadas listas auxiliares para controle estatístico do número total de palavras, palavras distintas e ocorrências repetidas.

------ Classe NOAVL
A classe NOAVL representa o nó da árvore AVL. Cada objeto dessa classe armazena:

- A palavra indexada;
- Uma lista contendo as linhas onde a palavra ocorre;
- A altura do nó, necessária para o cálculo do balanceamento;
- Referências para os filhos esquerdo e direito.

Essa estrutura permite que cada palavra seja armazenada apenas uma vez na árvore, enquanto múltiplas ocorrências são registradas na lista de linhas.

------ Classe AVL
A classe AVL implementa toda a lógica de funcionamento da árvore AVL, sendo responsável pelas operações de inserção, remoção, balanceamento, busca e percursos.
As principais funções implementadas são:

- Inserção - "def insere(self, palavra, linha)", "def __insereNO(self, atual, palavra, linha)": Realiza a inserção de uma nova palavra na árvore. Caso a palavra já exista, apenas a linha correspondente é adicionada à lista de ocorrências. Após cada inserção, a altura dos nós é atualizada e, se necessário, são aplicadas rotações para manter o balanceamento da árvore.

- Rotações - "def __RotacaoLL(self, A)", "def __RotacaoRR(self, A)", "def __RotacaoLR(self, A)", "def __RotacaoRL(self, A)": Foram implementadas quatro rotações clássicas da árvore AVL: rotação simples à direita (LL), rotação simples à esquerda (RR), rotação dupla esquerda-direita (LR) e rotação dupla direita-esquerda (RL). Essas operações garantem que a diferença de altura entre subárvores permaneça dentro dos limites permitidos.

- Remoção - "def remove(self, palavra, linha)", "def __removeNO": Permite remover uma ocorrência específica de uma palavra. Caso a lista de linhas fique vazia, o nó correspondente é removido da árvore, respeitando as regras da árvore binária de busca e mantendo o balanceamento AVL.

- Percurso em ordem - "def emOrdem(self)", "def __emOrdem(self, atual, lista)": Realiza o percurso simétrico da árvore, possibilitando a obtenção das palavras em ordem alfabética, essencial para a geração do índice remissivo.

- Busca exata e cálculo da Medida de Equilíbrio (ME) - "def contar_nos(self, atual)", "def buscar_me(self, atual, palavra)": Permite localizar uma palavra na árvore e calcular sua medida de equilíbrio, verificando a diferença entre o número de nós nas subárvores esquerda e direita.

- Busca aproximada por prefixo - "def __compararPrefixo(self, palavra, prefixo)", "def buscaPrefixo(self, atual, prefixo, lista)": Percorre a árvore em busca de palavras que iniciem com determinado prefixo, fornecendo sugestões ou correspondências parciais.

------ Funções de auxílio
Funções auxiliares responsáveis pelo tratamento do texto:
- eh_letra(c): Verifica se um caractere é uma letra válida, incluindo letras acentuadas.
- separar_palavras(linha): Processa cada linha do texto, extraindo apenas palavras válidas, convertendo-as para letras minúsculas e descartando símbolos, números e pontuação.
Essas funções tem como objetivo assegurar a correta padronização dos dados antes da inserção na árvore.

------ Classe IndiceRemissivoAVL
A classe IndiceRemissivoAVL coordena todo o processo de construção do índice remissivo. Suas principais responsabilidades incluem:
- Leitura do arquivo de entrada;
- Processamento das linhas e separação das palavras;
- Inserção das palavras na árvore AVL;
- Armazenamento de dados estatísticos, como número total de palavras, quantidade de palavras distintas, palavras repetidas, tempo de execução e total de rotações realizadas.
Além disso, essa classe disponibiliza métodos para busca aproximada, cálculo da medida de equilíbrio, identificação da palavra mais frequente e geração do arquivo final contendo o índice remissivo.

------ Exemplos de Uso
Considere o seguinte trecho de texto como entrada:
"A família deu conta, então, do que o pai antes anunciara: Sombrinha, afinal das contas, sempre se confirmava regredindo.
De dia para dia ela ia ficando sempre menorzita. Não havia que iludir — as roupas 14 iam sobrando, o leito ia crescendo."

O arquivo "indice" criado, retorna:
Índice Remissivo:

a: 1
afinal: 1
antes: 1
anunciara: 1
as: 2
confirmava: 1
conta: 1
contas: 1
crescendo: 2
das: 1
de: 2
deu: 1
dia: 2
do: 1
ela: 2
então: 1
família: 1
ficando: 2
havia: 2
ia: 2
iam: 2
iludir: 2
leito: 2
menorzita: 2
não: 2
o: 1,2
pai: 1
para: 2
que: 1,2
regredindo: 1
roupas: 2
se: 1
sempre: 1,2
sobrando: 2
sombrinha: 1

Total de palavras: 40
Palavras distintas: 35
Palavras descartadas (repetidas): 5
Tempo de construção: 0.0005s
Total de rotações AVL: 30

A busca aproximada pelo prefixo "so" e pela palavra "sombrinha" retorna:

Valor do ME para 'sombrinha': 0
Palavra encontrada. ME = 0(árvore balanceada)
Busca aproximada: ['sobrando', 'sombrinha']
Palavra mais frequente: o

