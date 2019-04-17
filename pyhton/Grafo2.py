import heapq


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distance[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    entry_lookup = {}
    pq = []

    for vertex, distance in distances.items():
        entry = [distance, vertex]
        entry_lookup[vertex] = entry
        heapq.heappush(pq, entry)

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, neighbor_distance in graph[current_vertex].items():
            distance = distances[current_vertex] + neighbor_distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                entry_lookup[neighbor][0] = distance

    return distances


def direct_cost(self, vertex1, vertex2):
    list_v1 = self.__graph_dict[vertex1]
    for (v, cost) in list_v1:
        if v is vertex2:
            return cost
        else:
            return math.inf


def prim(graph, root):
    vertex = [root]  # Lista dos vertices a partir do qual buscamos as arestas
    selected_edges = []  # Lista com as arestas selecionadas

    weight = 0  # Peso do minimum spanning tree

    remaing_vertices = list(graph.vertices())  # Lista com os vertices destinos da busca
    remaing_vertices.remove(root)  # O root eh ponto de partida, entao sai da lista

    for i in range(len(remaing_vertices)):  # Devemos buscar |V| - 1 vertices
        min_cost = inf  # Inicializamos o custo minimo como infinito
        va, vb = None, None  # Vertices candidatos para a aresta selecionada
        for v1 in vertex:  # Para cada vertice na lista de busca origem
            for v2 in remaing_vertices:  # Buscamos os vertices que ainda nao estao no grafo final
                cost = graph.direct_cost(v1, v2)  # Calcula o custo da aresta
                if cost < min_cost:  # Se for menor que o minimo ate entao, atualizamos os dados
                    va = v1
                    vb = v2
                    min_cost = cost

        if min_cost < inf:  # Depois de todas as buscas, se o custo eh finito:
            selected_edges.append((va, vb, min_cost))  # Adicionamos a aresta de va a vb na solucao
            vertex.append(vb)  # vb agora sera nova origem de busca
            remaing_vertices.remove(vb)  # vb nao mais sera destino de busca, pois ja consta na solucao
            weight += min_cost  # Atualiza o peso

    return selected_edges, weight  # Retorna a lista de arestas selecionadas com o peso total

    # def dijkstra(self, vertice_inicial):
    #     arestas_agm = []
    #     distancias = {vertice: float('infinity') for vertice in self.__grafo_dicionario}
    #     distancias[vertice_inicial] = 0
    #
    #     bloqueio_entrada = {}
    #     heap = []
    #
    #     # path = []
    #     for vertice, distancia in distancias.items():
    #         entrada = [distancia, vertice]
    #         bloqueio_entrada[vertice] = entrada
    #         heapq.heappush(heap, entrada)
    #
    #     while len(heap) > 0:
    #         distancia_atual, vertice_atual = heapq.heappop(heap)
    #         # print(vertice_atual, distancia_atual)
    #         # path.append((distancia_atual, vertice_atual))
    #         for vizinho, distancia_vizinho in self.__grafo_dicionario[vertice_atual].items():
    #             distancia = distancias[vertice_atual] + distancia_vizinho
    #             distancias_vizinho = distancias[vizinho]
    #             if distancia < distancias_vizinho:
    #                 distancias[vizinho] = distancia
    #                 bloqueio_entrada[vizinho][0] = distancia
    #                 # print(bloqueio_entrada)
    #                 arestas_agm.append((vertice_atual, vizinho))
    #                 # print(vertice_atual, vizinho)
    #
    #     # ----------------------------------------------------
    #     path = []
    #     do = [(k, distancias[k]) for k in
    #           sorted(distancias, key=distancias.get, reverse=True)]
    #     for x in range(len(do) - 1):
    #         if (do[x + 1][0], do[x][0]) in self.arestas():
    #             path.append((do[x + 1][0], do[x][0]))
    #
    #     # print(path)
    #     # print(do)
    #     # print(arestas_agm)
    #     return arestas_agm
    #     # ----------------------------------------------------
    #     # return distancias
    #
    # # def print_caminhos(self, inicial):
    # #     caminho_desordenado = self.dijkstra(inicial)
    # #     s = [(k, caminho_desordenado[k]) for k in
    # #          sorted(caminho_desordenado, key=caminho_desordenado.get, reverse=False)]
    # #     caminho_ordenado = []
    # #     distancia = 0
    # #     for k, v in s:
    # #         if isinstance(v, int):
    # #             caminho_ordenado.append(k)
    # #     lista = list((k, v) for k, v in s)
    # #     custo = max(s, key=operator.itemgetter(1))[1]
    # #     print(inicial, end=': ')
    # #     print(caminho_ordenado)
    # #     print("Custo = " + str(custo))