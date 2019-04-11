# import matplotlib.pyplot as plt
import networkx as nx
from pprint import pprint as pp

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
          "c": ["a", "b", "d", "e"],
          "d": ["c", "e"],
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

graph = Grafo([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
               ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
               ("e", "f", 9)])

print("GRAFO 1")
graph1 = Grafo(grafo1)
graph1.__str__()
graph1.verificar_aresta({"c", "f"})
graph1.grau_vertice("d")
graph1.verificar_adjacencia("b")
graph1.verificar_ciclico()
graph1.verificar_conexo()
graph1.verificar_fortemente_conexos()
graph1.verificar_eurreliano()
graph1.caminho_curto()
graph1.encontrar_agm()
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
graph2.verificar_eurreliano()
graph2.caminho_curto()
graph2.encontrar_agm()
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
graph3.verificar_eurreliano()
graph3.caminho_curto()
graph3.encontrar_agm()
# print(nx.is_eulerian(nx.DiGraph(grafo3)))

# G1 = nx.DiGraph(grafo1)
# # print(G1.neighbors("b"))
# # print(G1.edges)
# # print(G1.nodes)
# # print(G1.has_edge("a", "b"))
# # print(G1.has_edge("a", "c"))
# fig = plt.figure()
# fig.suptitle('Grafo 1 ', fontsize=20)
# nx.draw(G1, with_labels=True)
# plt.show()
#
# G2 = nx.DiGraph(grafo2)
# # print(G2.neighbors("b"))
# fig = plt.figure()
# fig.suptitle('Grafo 2 ', fontsize=20)
# nx.draw(G2, with_labels=True, )
# plt.show()
#
# G3 = nx.DiGraph(grafo3)
# # print(G3.neighbors("b"))
# # print(G3.is_directed())
# fig = plt.figure()
# fig.suptitle('Grafo 3 ', fontsize=20)
# nx.draw(G3, with_labels=True, )
# plt.show()
