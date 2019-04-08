from Grafo import Graph

grafo1 = {"a": ["c"],
          "b": ["c", "e"],
          "c": ["a", "b", "d", "e"],
          "d": ["c"],
          "e": ["c", "b"],
          "f": []
          }

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

graph1 = Graph(grafo1)
print(graph1.vertices())
