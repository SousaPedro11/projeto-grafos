import heapq


class HeapEntry:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def check_edges(self, edge):
        """ Método para verificar se as arestas existem"""
        (vertex1, vertex2) = tuple(edge)
        if {vertex1, vertex2} in self.edges():
            return print("A aresta existe")
        return print("A aresta não existe")

    def check_adjacent(self, vertex):
        adjacent = []
        for neighbour in self.__graph_dict[vertex]:
            adjacent.append(neighbour)
        return adjacent

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

    def encontrar_todos_caminhos(self, vertice_inicio, vertice_fim, caminho=None):
        """ encontra todos os caminhos entre dois vértices """
        if caminho is None:
            caminho = []
        grafo = self.__graph_dict
        caminho = caminho + [vertice_inicio]
        if vertice_inicio is vertice_fim:
            return [caminho]
        if vertice_inicio not in grafo:
            return []
        caminhos = []
        for vertice in grafo[vertice_inicio]:
            if vertice not in caminho:
                caminhos_extendidos = self.encontrar_todos_caminhos(vertice,
                                                                    vertice_fim,
                                                                    caminho)
                for p in caminhos_extendidos:
                    caminhos.append(p)
        return caminhos

    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted
            double, i.e. every occurence of vertex in the list
            of adjacent vertices. """
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def is_connected(self,
                     vertices_encountered=None,
                     start_vertex=None):
        """ determines if the graph is connected """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__graph_dict
        vertices = list(gdict.keys())  # "list" necessary in Python 3
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False

    def cyclic(self):
        """Return True if the directed graph has a cycle.
        The graph must be represented as a dictionary mapping vertices to
        iterables of neighbouring vertices. For example:
        False"""

        visited = set()
        path = [object()]
        path_set = set(path)
        stack = [iter(self.__graph_dict)]
        while stack:
            for v in stack[-1]:
                if v in path_set:
                    return True
                elif v not in visited:
                    visited.add(v)
                    path.append(v)
                    path_set.add(v)
                    stack.append(iter(self.__graph_dict.get(v, ())))
                    break
            else:
                path_set.remove(path.pop())
                stack.pop()
        return False

    def tarjan(self):
        # Declare globals
        index = {}  # Dictionary of vertices and connections
        lowlink = {}  # Dictionary of smallest indices of any node reachable from v
        stack = []  # S - stack (List)
        result = []  # List to store SCCs
        counter = [0]  # Must be list type for dictionary iteration - marks number of visits

        # onStack = []
        # onLowlink = []

        # Inner function; Python encapsulation convention
        # Depth-first search
        def strong_connect(v):

            # Empty graph object/list
            if not self:
                raise ValueError("Graph is empty.")

            index[v] = counter[0]  # Depth index v = smallest unused index
            lowlink[v] = counter[0]  # Computed during depth-first search from v
            counter[0] += 1  # counter++; Keep track of visits (used by stack)
            stack.append(v)  # Add vertex to stack = S.push(v)

            # Consider successors (edges) of v
            edges = self.__graph_dict[v]
            # for each (v, w) in E do (iterate on graph[v])
            for w in edges:
                # If (w[index] undefined], successor hasn't been visited yet
                if w not in stack:
                    # Visit and add as successor
                    strong_connect(w)
                    lowlink[v] = min(lowlink[v], lowlink[w])
                # If w already in stack
                elif w in stack:
                    # Successor is a lowlink (smallest index reachable from v)
                    lowlink[v] = min(lowlink[v], index[w])

            # If v is a root node, pop the stack and generate an SCC
            # If current vertex = root vertex
            if lowlink[v] == index[v]:
                # Start a new SCC list
                scc = []

                # Repeat while successor < current scc
                # True: lowlink[v] == index[v]
                # v must be left on the stack if v.lowlink < v.index
                while True:
                    w = stack.pop()
                    # Add w to SCC list
                    scc.append(w)
                    # If already visited (and are same), break
                    # v must be removed as the root of a strongly connected component if v.lowlink == v.index
                    if w == v:
                        break
                # Output the current strongly connected component
                # Store in tuple, immutable
                result.append(tuple(scc))

        vertices = self.__graph_dict
        for v in vertices:
            # If v is unvisited, make it a SCC
            if v not in lowlink:
                strong_connect(v)

        # Return list of edges (tuples)
        return tuple(result)

    def verificar_eureliano(self):
        # FIXME ajustar para grafo ponderado
        result = ["Verificar se o grafo é Euleriano: "]
        if not self.is_connected():
            result.append("Não é eureliano")
        else:
            odd = 0
            for vertice in self.vertices():
                if len(self.__graph_dict[vertice]) % 2 is not 0:
                    odd += 1
            result.append("É Euleriano") if odd is 0 else result.append("Não é Euleriano")
        print(''.join(result))

    def diameter(self):
        # FIXME falta corrigir ou substituir o algoritmo
        v = self.vertices()
        pares = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]
        caminho_curto = []
        for (s, e) in pares:
            caminhos = self.encontrar_todos_caminhos(s, e)
            mais_curto = sorted(caminhos, key=len)[0]
            caminho_curto.append(mais_curto)
        caminho_curto.sort(key=len)
        return caminho_curto[-1]

    def caminho_curto(self):
        # FIXME ajustar para grafo ponderado
        if self.is_connected():
            result = "O caminho mais curto é: "
            result += str(self.diameter())
            print(result)

    def traceback_path(self, target, parents):
        path = []
        while target:
            path.append(target)
            target = parents[target]
        return list(reversed(path))

    def shortest_path(self, start, finish):
        OPEN = [HeapEntry(start, 0.0)]
        CLOSED = set()
        parents = {start: None}
        distance = {start: 0.0}

        while OPEN:
            current = heapq.heappop(OPEN).node

            if current is finish:
                return self.traceback_path(finish, parents)

            if current in CLOSED:
                continue

            CLOSED.add(current)

            for child in self.__graph_dict[current].keys():
                if child in CLOSED:
                    continue
                tentative_cost = distance[current] + self.__graph_dict[current][child]

                if child not in distance.keys() or distance[child] > tentative_cost:
                    distance[child] = tentative_cost
                    parents[child] = current
                    heap_entry = HeapEntry(child, tentative_cost)
                    heapq.heappush(OPEN, heap_entry)
