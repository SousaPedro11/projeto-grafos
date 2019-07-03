import Entrada
from Grafo import Grafo

"""
    1. Verificar a existência de uma determinada aresta.
    2. Informar o grau de um dado vértice.
    3. Informar a adjacência de um dado vértice.
    4. Verificar se o grafo é cíclico.
    5. Verificar se o grafo é conexo.
    6. Informar quantos e quais são os componentes fortemente conexos do grafo.
    7. Verificar se o grafo é euleriano.
    8. Encontrar o caminho mais curto entre dois vértices. Se o grafo for valorado, o problema deve ser resolvido com o
    algoritmo de Dijkstra.
    9. Encontrar a árvore geradora mínima (AGM) do grafo.
"""

# print("GRAFO 1")
# graph1 = Grafo(Entrada.grafo01)
# graph1.__str__()
# print("q1.", end=' ')
# graph1.verificar_aresta("a", "b")  # OK
# graph1.verificar_aresta("b", "a")  # OK
# graph1.verificar_aresta("a", "i")  # OK
# print("q2.", end=' ')
# graph1.grau_vertice("i")  # OK
# print("q3.", end=' ')
# graph1.verificar_adjacencia("h")  # OK
# print("q4.", end=' ')
# graph1.is_cyclic()  # OK
# print("q5.", end=' ')
# graph1.verificar_conexo()  # OK
# # print("q6.", end=' ')
# # grafo.verificar_fortemente_conexos()  # FIXME
# print("q7.", end=' ')
# graph1.verificar_eureliano()  # OK
# print("q8.", end=' ')
# graph1.imprime_caminho("a", "e")  # FIXME
# print("q9.", end=' ')
# graph1.encontrar_agm("a")  # OK
# # grafo.plotar()
# print()

# print("GRAFO 2")
# graph02 = Grafo(Entrada.grafo02)
# graph02.__str__()
# print("q1.", end=' ')
# graph1.verificar_aresta("a", "b")  # OK
# graph1.verificar_aresta("b", "a")  # OK
# graph1.verificar_aresta("a", "i")  # OK
# print("q2.", end=' ')
# graph1.grau_vertice("i")  # OK
# graph02.grau_vertice("Antônio")  # OK
# print("q3.", end=' ')
# graph1.verificar_adjacencia("h")  # OK
# print("q4.", end=' ')
# graph1.is_cyclic()  # OK
# print("q5.", end=' ')
# graph1.verificar_conexo()  # OK
# # print("q6.", end=' ')
# # grafo.verificar_fortemente_conexos()  # FIXME
# print("q7.", end=' ')
# graph1.verificar_eureliano()  # OK
# print("q8.", end=' ')
# graph02.imprime_caminho("Cecília", "Antônio")  # OK
# graph02.imprime_caminho("Alfredo", "Renata")  # OK
# print("q9.", end=' ')
# graph1.encontrar_agm("a")  # OK
# grafo.plotar()
# print()

# print("GRAFO 3")
# graph03 = Grafo(Entrada.grafo03)
# graph03.__str__()
# print("q1.", end=' ')
# graph03.verificar_aresta("Curitiba", "SaoPaulo")  # OK
# graph03.verificar_aresta("Curitiba", "Florianopolis")  # OK
# graph03.verificar_aresta("Curitiba", "PortoAlegre")  # OK
# print("q2.", end=' ')
# graph03.grau_vertice("PortoAlegre")  # OK
# print("q3.", end=' ')
# graph03.verificar_adjacencia("SaoPaulo")  # OK
# print("q4.", end=' ')
# graph03.is_cyclic()  # OK
# print("q5.", end=' ')
# graph03.verificar_conexo()  # OK
# # print("q6.", end=' ')
# # grafo.verificar_fortemente_conexos()  # FIXME
# print("q7.", end=' ')
# graph03.verificar_eureliano()  # OK
# print("q8.", end=' ')
# graph03.imprime_caminho("Florianopolis", "SaoPaulo")  # FIXME
# print("q9.", end=' ')
# graph03.encontrar_agm("PortoAlegre")  # OK
# # grafo.plotar()
# print()
#
# print("GRAFO 6")
# graph06 = Grafo(Entrada.grafo06)
# graph06.__str__()
# print("q1.", end=' ')
# graph06.verificar_aresta("a", "b")  # OK
# graph06.verificar_aresta("b", "a")  # OK
# graph06.verificar_aresta("a", "i")  # OK
# print("q2.", end=' ')
# graph06.grau_vertice("i")  # OK
# print("q3.", end=' ')
# graph06.verificar_adjacencia("h")  # OK
# print("q4.", end=' ')
# graph06.is_cyclic()  # OK
# print("q5.", end=' ')
# graph06.verificar_conexo()  # OK
# # print("q6.", end=' ')
# # grafo.verificar_fortemente_conexos()  # FIXME
# print("q7.", end=' ')
# graph06.verificar_eureliano()  # OK
# print("q8.", end=' ')
# graph06.imprime_caminho("a", "e")  # FIXME
# graph06.imprime_caminho("a", "d")  # FIXME
# graph06.imprime_caminho("i", "e")  # FIXME
# graph06.imprime_caminho("h", "e")  # FIXME
# graph06.imprime_caminho("a", "a")  # FIXME
# graph06.imprime_caminho("a", "b")  # FIXME
# print("q9.", end=' ')
# graph06.encontrar_agm("a")  # OK
# graph06.encontrar_agm("g")  # OK
# graph06.encontrar_agm("c")  # OK
# # graph06.plotar()
# print()
#
# print("GRAFO 8")
# graph08 = Grafo(Entrada.grafo08)
# graph08.__str__()
# graph08.imprime_caminho("0", "4")
graph09 = Grafo(Entrada.grafo09)
graph09.verificar_fortemente_conexos()
# graph09.scg()
graph09.scc()
