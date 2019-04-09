from Grafo import Grafo


def questoes(grafo):
    print(grafo)
    # print("Vertices:")
    # print(grafo.vertices())
    # print("\nArestas:")
    # print(grafo.arestas())
    print('The path from vertex "a" to vertex "b":')
    path = grafo.encontrar_caminho("a", "b")
    print(path)
    print('The path from vertex "c" to vertex "b":')
    path = grafo.encontrar_caminho("c", "b")
    print(path)
    print('The path from vertex "b" to vertex "f":')
    path = grafo.encontrar_caminho("b", "f")
    print(path)
    print('Check if an edge exists')
    print(grafo.verificar_aresta({"c", "e"}))
    print('The degree of a vertex')
    print(grafo.grau_vertice("d"))
    print('Check adjacents')
    print(grafo.verificar_adjacencia("a"))


# def generate_edges(graph):
#     edges = []
#     for node in graph:
#         for neighbour in graph[node]:
#             edges.append((node, neighbour))
#     # return edges
#     print("vertices conexos: ", edges)
#
# def find_isolated_nodes(graph):
#     """ returns a list of isolated nodes. """
#     isolated = []
#     for node in graph:
#         if not graph[node]:
#             isolated += node
#     # return isolated
#     print("vertices isolados:", isolated)

'''
    1. Verificar a existência de uma determinada aresta.
    2. Informar o grau de um dado vértice.
    3. Informar a adjacência de um dado vértice.
    4. Verificar se o grafo é cíclico.
    5. Verificar se o grafo é conexo.
    6. Informar quantos e quais são os componentes fortemente conexos do grafo.
    7. Verificar se o grafo é euleriano.
    8. Encontrar o caminho mais curto entre dois vértices. Se o grafo for valorado, o problema deve ser resolvido com o algoritmo de Dijkstra.
    9. Encontrar a árvore geradora mínima (AGM) do grafo.
'''

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
          "d": ["e"],
          "e": ["f"],
          "f": []
          }

grafos = []
grafos.append(Grafo(grafo1))
grafos.append(Grafo(grafo2))
grafos.append(Grafo(grafo3))
i = 0
for grafo in grafos:
    i += 1
    print("Grafo %s" % str(i))
    questoes(grafo)
    print()
