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

print("GRAFO 1")
graph1 = Grafo(Entrada.grafo01)
graph1.__str__()
print("q1.")
print("a.", end=' ')
graph1.verificar_aresta("1", "2")  # OK
graph1.verificar_aresta("4", "3")  # OK
graph1.verificar_aresta("1", "3")  # OK
graph1.verificar_aresta("0", "4")
# print("q.", end=' ')
# graph1.grau_vertice("i")  # OK
# print("q3.", end=' ')
# graph1.verificar_adjacencia("h")  # OK
# print("q6.", end=' ')
# grafo.verificar_fortemente_conexos()  # FIXME
# print("q7.", end=' ')
# graph1.verificar_eureliano()  # OK
print("\nb.", end=' ')
graph1.encontrar_caminho_minimo("2", "1")
#print(graph1.encontrar_todos_caminhos("2", "1"))
print("\nc.", end=' ')
graph1.verificar_conexo()  # OK
graph1.verificar_fortemente_conexos()
print("\nd.", end=' ')
#graph1.is_cyclic()  # OK
graph1.verificar_ciclico()
#print(graph1.encontrar_caminho("2", "1"))
# print("q9.", end=' ')
# graph1.encontrar_agm("a")  # OK
# grafo.plotar()
print()

#print("GRAFO 2")
graph3 = Grafo(Entrada.grafo03)
#graph1.__str__()
print("q2.")
print("a.", end=' ')
graph3.verificar_adjacencia("1")  # OK
#graph1.verificar_aresta("4", "3")  # OK
#graph1.verificar_aresta("1", "3")  # OK
print("\nb.", end=' ')
graph3.grau_vertice("3")  # OK
# print("q3.", end=' ')
# graph1.verificar_adjacencia("h")  # OK
# print("q6.", end=' ')
# grafo.verificar_fortemente_conexos()  # FIXME
# print("q7.", end=' ')
#print("\nb.", end=' ')
#graph1.encontrar_caminho_minimo("2", "1")
#print(graph1.encontrar_todos_caminhos("2", "1"))
print("\nc.", end=' ')
graph3.verificar_conexo()  # OK
print("\nd.", end=' ')
graph3.verificar_eureliano()  # OK
#graph1.is_cyclic()  # OK
#graph1.verificar_ciclico()
#print(graph1.encontrar_caminho("2", "1"))
# print("q9.", end=' ')
# graph1.encontrar_agm("a")  # OK
# grafo.plotar()
print()

print("GRAFO 2")
graph2 = Grafo(Entrada.grafo02)
graph2.__str__()
print("q3.")
print("a.", end=' ')
graph2.imprime_caminho("A", "D")
#graph1.verificar_aresta("1", "2")  # OK
#graph1.verificar_aresta("4", "3")  # OK
#graph1.verificar_aresta("1", "3")  # OK
print("\nb.", end=' ')
# graph1.grau_vertice("i")  # OK
# print("q3.", end=' ')
# graph1.verificar_adjacencia("h")  # OK
# print("q6.", end=' ')
# grafo.verificar_fortemente_conexos()  # FIXME
# print("q7.", end=' ')
# graph1.verificar_eureliano()  # OK
#print("\nb.", end=' ')
#graph1.encontrar_caminho_minimo("2", "1")
#print(graph1.encontrar_todos_caminhos("2", "1"))
#print("\nc.", end=' ')
#graph1.verificar_conexo()  # OK
#print("\nd.", end=' ')
#graph1.is_cyclic()  # OK
#graph1.verificar_ciclico()
#print(graph1.encontrar_caminho("2", "1"))
# print("q9.", end=' ')
graph4 = Grafo(Entrada.grafo04)
graph2.__str__()
graph4.encontrar_agm("A")  # OK
# grafo.plotar()
#print()