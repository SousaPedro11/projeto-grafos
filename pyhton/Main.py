# from pprint import pprint as pp

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

grafo1 = {"a": ["c"],
          "b": ["c", "e"],
          "c": ["b", "d", "e"],
          "d": ["c", "e", "f"],
          "e": ["c", "b", "d", "f"],
          "f": ["e"]
          }

grafo2 = {"a": ["b", "c"],
          "b": ["c", "d"],
          "c": ["a", "b"],
          "d": ["b"]
          }

grafo3 = {"a": ["c"],
          "b": ["c", "e"],
          "c": [],
          "d": ["b", "e"],
          "e": ["f"],
          "f": []
          }

grafo4 = {"a": ["b", "d"],
          "b": ["a", "c"],
          "c": ["b", "d"],
          "d": ["a", "c"]
          }

grafo5 = {"a": ["c"],
          "b": ["c"],
          "c": ["a", "b", "d", "e"],
          "d": ["c", "e"],
          "e": ["c", "d"]
          }

grafo6 = {"a": {'b': 1},
          "b": {'c': 2},
          "c": {'a': 3},
          "d": {"a": 1, "c": 5}
          }

print("GRAFO 1")
graph1 = Grafo(grafo1)
graph1.__str__()
graph1.verificar_aresta({"c", "f"})
graph1.grau_vertice("d")
graph1.verificar_adjacencia("b")
graph1.verificar_ciclico()
graph1.verificar_conexo()
graph1.verificar_fortemente_conexos()
graph1.verificar_eureliano()
graph1.caminho_curto()
graph1.encontrar_agm()
graph1.plotar()
print()
print("GRAFO 2")
graph2 = Grafo(grafo2)
graph2.__str__()
graph2.verificar_aresta({"c", "f"})
graph2.grau_vertice("d")
graph2.verificar_adjacencia("b")
graph2.verificar_ciclico()
graph2.verificar_conexo()
graph2.verificar_fortemente_conexos()
graph2.verificar_eureliano()
graph2.caminho_curto()
graph2.encontrar_agm()
graph2.plotar()
print()
print("GRAFO 3")
graph3 = Grafo(grafo3)
graph3.__str__()
graph3.verificar_aresta({"c", "b"})
graph3.grau_vertice("b")
graph3.verificar_adjacencia("b")
graph3.verificar_ciclico()
graph3.verificar_conexo()
graph3.verificar_fortemente_conexos()
graph3.verificar_eureliano()
graph3.caminho_curto()
graph3.encontrar_agm()
graph3.plotar()
print()
print("GRAFO 4")
graph4 = Grafo(grafo4)
graph4.__str__()
graph4.verificar_aresta({"c", "b"})
graph4.grau_vertice("b")
graph4.verificar_adjacencia("b")
graph4.verificar_ciclico()
graph4.verificar_conexo()
graph4.verificar_fortemente_conexos()
graph4.verificar_eureliano()
graph4.caminho_curto()
graph4.encontrar_agm()
graph4.plotar()
print()
print("Grafo 6")
graph6 = Grafo(grafo6)
graph6.__str__()
graph6.verificar_aresta({"c", "f"})
# graph6.grau_vertice("b")
graph6.verificar_adjacencia("b")
graph6.verificar_ciclico()
graph6.verificar_conexo()
graph6.verificar_fortemente_conexos()
graph6.verificar_eureliano()
graph6.caminho_curto()
graph6.encontrar_agm()
graph6.plotar()
print()
#
# tarjan_graph = graph3.tarjan()
# print('How many components are Strongly Connected')
# cont = 0
# for i in range(0, len(tarjan_graph)):
#     for j in tarjan_graph[i]:
#         cont += 1
# print(cont)
# print("What components are Strongly Connected")
# print(tarjan_graph)
