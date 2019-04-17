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

grafo7 = {"0": {"1": 1, "3": 3, "4": 10},
          "1": {"2": 5},
          "2": {"4": 1},
          "3": {"2": 2, "4": 6},
          "4": {}
          }

grafo8 = {"a": {"c": 1},
          "b": {"c": 3},
          "c": {"a": 5, "b": 4, "d": 2, "e": 1},
          "d": {"c": 2, "e": 1},
          "e": {"c": 4, "d": 7}
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
graph1.imprime_caminho("a", "d")
graph1.encontrar_agm("a")
graph1.plotar()
print()
print("GRAFO 2")
graph2 = Grafo(grafo2)
graph2.__str__()
graph2.verificar_aresta({"c", "f"})
graph2.grau_vertice("b")
graph2.verificar_adjacencia("b")
graph2.verificar_ciclico()
graph2.verificar_conexo()
graph2.verificar_fortemente_conexos()
graph2.verificar_eureliano()
graph2.imprime_caminho("a", "d")
graph2.encontrar_agm("a")
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
graph3.imprime_caminho("a", "d")
graph3.encontrar_agm("a")
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
graph4.imprime_caminho("a", "d")
graph4.encontrar_agm("a")
graph4.plotar()
print()
print("Grafo 5")
graph5 = Grafo(grafo5)
graph5.__str__()
graph5.verificar_aresta({"c", "f"})
graph5.grau_vertice("c")
graph5.verificar_adjacencia("b")
graph5.verificar_ciclico()
graph5.verificar_conexo()
graph5.verificar_fortemente_conexos()
graph5.verificar_eureliano()
graph5.imprime_caminho("a", "d")
graph5.encontrar_agm("a")
graph5.plotar()
print()
print("Grafo 6")
graph6 = Grafo(grafo6)
graph6.__str__()
graph6.verificar_aresta({"c", "f"})
graph6.grau_vertice("b")
graph6.verificar_adjacencia("b")
graph6.verificar_ciclico()
graph6.verificar_conexo()
graph6.verificar_fortemente_conexos()
graph6.verificar_eureliano()
graph6.imprime_caminho("a", "d")
graph6.encontrar_agm("a")
graph6.plotar()
print()
print("Grafo 7")
graph7 = Grafo(grafo7)
graph7.__str__()
graph7.verificar_aresta({"c", "f"})
graph7.grau_vertice("3")
graph7.verificar_adjacencia("3")
graph7.verificar_ciclico()
graph7.verificar_conexo()
graph7.verificar_fortemente_conexos()
graph7.verificar_eureliano()
graph7.imprime_caminho("a", "d")
graph7.encontrar_agm("a")
graph7.plotar()
print()
print("Grafo 8")
graph8 = Grafo(grafo8)
graph8.__str__()
graph8.verificar_aresta({"c", "f"})
graph8.grau_vertice("d")
graph8.verificar_adjacencia("d")
graph8.verificar_ciclico()
graph8.verificar_conexo()
graph8.verificar_fortemente_conexos()
graph8.verificar_eureliano()
graph8.imprime_caminho("a", "d")
graph8.encontrar_agm("a")
# print(graph8.prim("a"))
graph8.plotar()
