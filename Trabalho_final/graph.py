from graphs import Graph

g = {"a": ["d"],
     "b": ["c"],
     "c": ["b", "c", "d", "e"],
     "d": ["a", "c"],
     "e": ["c"],
     "f": []
     }
g2 = {"a": ["b", "c"],  # Directed graph
      "b": ["d"],
      "c": ["d"],
      "d": ["e"],
      "e": ["c"]}

g3 = {1: [4],
      2: [3],
      3: [2, 3, 4, 5],
      4: [1, 3],
      5: [3],
      6: []
      }

g4 = {'a': {'w': 14, 'x': 7, 'y': 9},
      'b': {'w': 9, 'z': 6},
      'w': {'a': 14, 'b': 9, 'y': 2},
      'x': {'a': 7, 'y': 10, 'z': 15},
      'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
      'z': {'b': 6, 'x': 15, 'y': 11}}

graph = Graph(g)
graph2 = Graph(g2)
graph1 = Graph(g2)
graph3 = Graph(g4)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print('The path from vertex "a" to vertex "b":')
path = graph.find_path("a", "b")
print(path)

print('The path from vertex "a" to vertex "f":')
path = graph.find_path("a", "f")
print(path)

print('The path from vertex "c" to vertex "c":')
path = graph.find_path("c", "c")
print(path)
print('Check if an edge exists')
graph.check_edges({"c", "e"})
print('The degree of a vertex')
print(graph.vertex_degree("d"))
print('Check adjacents')
print(graph.check_adjacent("a"))
print('Check if Graph is connected')
if graph.is_connected():
    print('O Grafo é conexo')
else:
    print('O Grafo não é conexo')
print('Check if Graph is ciclic')
if graph1.cyclic():
    print('O grafo é cíclico')
else:
    print('O grafo não é cíclico')
tarjan_graph = graph2.tarjan()
print('How many components are Strongly Connected')
cont = 0
for i in range(0, len(tarjan_graph)):
    for j in tarjan_graph[i]:
        cont += 1
print(cont)
print("What components are Strongly Connected")
print(tarjan_graph)

graph1.verificar_eureliano()

graph1.caminho_curto()

print("Caminho mais curto entre os vétices 'a' e 'b' para grafo valorado, usando Dijkstra")
print(graph3.shortest_path("a", "b"))
