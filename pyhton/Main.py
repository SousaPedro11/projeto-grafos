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
          "c": {"a": 1, "b": 3, "d": 2, "e": 4},
          "d": {"c": 2, "e": 1},
          "e": {"c": 4, "d": 1}
          }

grafo9 = {"1": {"2": 2, "5": 1, "6": 5},
          "2": {"1": 2, "3": 3, "5": 7},
          "3": {"2": 3, "4": 9, "5": 3},
          "4": {"3": 9, "5": 4},
          "5": {"1": 1, "2": 7, "3": 3, "4": 4, "6": 4},
          "6": {"1": 5, "5": 4}
          }

grafo10 = {"a": {"b": 3, "c": 5, "d": 1},
           "b": {"a": 3, "e": 4},
           "c": {"a": 5, "d": 4, "e": 8},
           "d": {"a": 1, "c": 4, "f": 3},
           "e": {"b": 4, "c": 8, "f": 7},
           "f": {"d": 3, "e": 7}
           }

grafo11 = {"A": {"B": 2, "D": 7, "O": 2},
           "B": {"A": 2, "C": 1, "D": 4, "E": 3, "O": 5},
           "C": {"B": 1, "E": 4, "O": 4},
           "D": {"A": 7, "B": 4, "E": 1, "T": 5},
           "E": {"B": 3, "C": 4, "D": 1, "T": 7},
           "O": {"A": 2, "B": 5, "C": 4},
           "T": {"D": 5, "E": 7}
           }

# FIXME o grafo 12 é um multigrafo com self loop, a implementação atual não enxerga ambos
""" Como o dicionario baseia-se em Set, ele não aceita chaves repetidas, logo ('a', 'c', 7) e ('a', 'c', 4) nao conseguem
        coexistir ficando apenas o último ('a', 'c', 4), assim como ('c', 'c', 0) é reconhecido como ('c',0).
"""
# grafo12 = {"a": {"b": 4, "c": 7, "c": 4},
#            "b": {"c": 5},
#            "c": {"c": 0, "b": 2}
#            }

#Possivel solucao
# grafo12 = {'A': [('B', 1), ('B', 4)],
#            'B': [('C', 1), ('A', 4)],
#            }

print("GRAFO 1")
graph1 = Grafo(grafo1)
graph1.__str__()
graph1.verificar_aresta("f", "d")
graph1.verificar_aresta("d", "f")
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
graph2.verificar_aresta("c", "b")
graph2.verificar_aresta("b", "c")
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
graph3.verificar_aresta("c", "b")
graph3.verificar_aresta("b", "c")
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
graph4.verificar_aresta("c", "b")
graph4.verificar_aresta("b", "c")
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
graph5.verificar_aresta("c", "f")
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
graph6.verificar_aresta("c", "b")
graph6.verificar_aresta("b", "c")
graph6.grau_vertice("b")
graph6.verificar_adjacencia("b")
graph6.verificar_ciclico()
graph6.verificar_conexo()
graph6.verificar_fortemente_conexos()
graph6.verificar_eureliano()
graph6.imprime_caminho("a", "c")
graph6.encontrar_agm("a")
graph6.plotar()
print()
print("Grafo 7")
graph7 = Grafo(grafo7)
graph7.__str__()
graph7.verificar_aresta("1", "0")
graph7.verificar_aresta("0", "1")
graph7.grau_vertice("3")
graph7.verificar_adjacencia("3")
graph7.verificar_ciclico()
graph7.verificar_conexo()
graph7.verificar_fortemente_conexos()
graph7.verificar_eureliano()
graph7.imprime_caminho("1", "4")
graph7.encontrar_agm("1")
graph7.plotar()
print()
print("Grafo 8")
graph8 = Grafo(grafo8)
graph8.__str__()
graph8.verificar_aresta("c", "f")
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
print()
print("Grafo 9")
graph9 = Grafo(grafo9)
graph9.__str__()
graph9.verificar_aresta("c", "f")
graph9.grau_vertice("5")
graph9.verificar_adjacencia("5")
graph9.verificar_ciclico()
graph9.verificar_conexo()
graph9.verificar_fortemente_conexos()
graph9.verificar_eureliano()
graph9.imprime_caminho("2", "6")
graph9.encontrar_agm("1")
graph9.plotar()
graph9.aresta_peso()
print()
print("Grafo 10")
graph10 = Grafo(grafo10)
graph10.__str__()
graph10.verificar_aresta("c", "f")
graph10.grau_vertice("d")
graph10.verificar_adjacencia("d")
graph10.verificar_ciclico()
graph10.verificar_conexo()
graph10.verificar_fortemente_conexos()
graph10.verificar_eureliano()
graph10.imprime_caminho("b", "f")
graph10.encontrar_agm("a")
graph10.plotar()
graph10.aresta_peso()
print()
print("Grafo 11")
graph11 = Grafo(grafo11)
graph11.__str__()
graph11.verificar_aresta("C", "B")
graph11.grau_vertice("D")
graph11.verificar_adjacencia("D")
graph11.verificar_ciclico()
graph11.verificar_conexo()
graph11.verificar_fortemente_conexos()
graph11.verificar_eureliano()
graph11.imprime_caminho("O", "T")
graph11.encontrar_agm("A")
graph11.plotar()
graph11.aresta_peso()
print()
# FIXME o grafo 12 é um multigrafo com self loop, a implementação atual não enxerga ambos
# print("Grafo 12")
# graph12 = Grafo(grafo12)
# graph12.__str__()
# graph12.verificar_aresta("c", "b")
# graph12.grau_vertice("d")
# graph12.verificar_adjacencia("d")
# graph12.verificar_ciclico()
# graph12.verificar_conexo()
# graph12.verificar_fortemente_conexos()
# graph12.verificar_eureliano()
# graph12.imprime_caminho("o", "t")
# graph12.encontrar_agm("a")
# # graph12.plotar()
# graph12.aresta_peso()
# # <class 'dict'>: {'a': {'b': 4, 'c': 4}, 'b': {'c': 5}, 'c': {'c': 0, 'b': 2}}
