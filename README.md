# Projeto de Grafos
Projeto correspondente ao trabalho final da disciplina de Grafos, do Curso de Sistemas de Informação da UFPA, ministrada pelo professor Nelson Cruz Sampaio Neto.
## Problema Proposto
O grupo de até 5 (cinco) integrantes deverá implementar um programa computacional, em linguagem de programação a sua escolha, que trabalhe os itens abaixo ao receber um grafo orientado ou não orientado como entrada.
<ol>
    <li> Verificar a existência de uma determinada aresta.</li>
    <li> Informar o grau de um dado vértice.</li>
    <li> Informar a adjacência de um dado vértice.</li>
    <li> Verificar se o grafo é cíclico.</li>
    <li> Verificar se o grafo é conexo.</li>
    <li> Informar quantos e quais são os componentes fortemente conexos do grafo.</li>
    <li> Verificar se o grafo é euleriano.</li>
    <li> Encontrar o caminho mais curto entre dois vértices. Se o grafo for valorado, o problema deve ser resolvido com o algoritmo de Dijkstra.</li>
    <li> Encontrar a árvore geradora mínima (AGM) do grafo.</li>
</ol>

OBS: Entrega até dia 03/07/2019

## Projeto
### Implementação
Inicialmente o problema seria resolvido em Java, mas devido o prazo e
o conhecimento em comum entre os desenvolvedores, ficou estabelecido que
a implementação será em Python 3.

[Implementação em Python](https://gitlab.com/SousaPedro11/projeto-grafos/tree/master/pyhton)

### Requisitos Básicos do Ambiente
* Python 3
* Git
* IDE (recomendo PyCharm - estou utilizando para fazer o projeto) ou editor de texto

### Arquivos
* [Entrada.py](https://gitlab.com/SousaPedro11/projeto-grafos/blob/master/pyhton/Entrada.py) - Os grafos estão definidos aqui. É utilizada a estrutura de dicionário (dict).
* [Main.py](https://gitlab.com/SousaPedro11/projeto-grafos/blob/master/pyhton/Main.py) - Arquivo de execução personalizada. Os métodos podem ser chamados de acordo com a necessidade.
* [Utilitario.py](https://gitlab.com/SousaPedro11/projeto-grafos/blob/master/pyhton/Utilitario.py) - São definidos métodos auxiliares para a execução do projeto. É utilizado por Teste.py.
* [Grafo.py](https://gitlab.com/SousaPedro11/projeto-grafos/blob/master/pyhton/Grafo.py) - É onde se encontram todos os métodos para manipular os grafos de acordo com o esboço do projeto.
* [Teste.py](https://gitlab.com/SousaPedro11/projeto-grafos/blob/master/pyhton/Teste.py) - É um suite de teste que executa o método teste_grafo do Utilitario.py para todos os grafos 
definidos em Entrada.py. Nesta classe está a ordem dos problemas propostos e suas soluções.

## Grupo
* Edmilton Pinto Peixeira
* George Alan Kardec Monteiro de Jesus
* Hana Gabrielle dos Santos Barata
* Pedro Paulo Lisboa de Sousa
* Victor Hugo Azevedo Ferreira