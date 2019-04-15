""" A Python Class"""
import matplotlib.pyplot as plt
import networkx as nx


# import matplotlib.pyplot as plt


class Grafo(object):

    def __init__(self, grafo_dicionario=None):
        """ Inicializa o grafo.
            Se não houver um dicionario, será usado um vazio
        """
        if grafo_dicionario is None:
            grafo_dicionario = {}
        self.__grafo_dicionario = grafo_dicionario
        self.weights = grafo_dicionario

    def vertices(self):
        return list(self.__grafo_dicionario.keys())

    def arestas(self):
        direcionado = self.verificar_direcionado()
        if direcionado:
            arestas = []
            for vertice in self.vertices():
                for vertice_interno in self.__grafo_dicionario[vertice]:
                    arestas.append((vertice, vertice_interno))
            return list(arestas)
        else:
            return self.__gerar_arestas()

    def pesos(self):
        pass

    def adicionar_vertice(self, vertice):
        """ Se o vertice não estiver presente no dicionário,
        uma chave vertice com uma lista vazia é adicionada.
            Se estiver presente, nada é feito.
        """
        if vertice not in self.__grafo_dicionario:
            self.__grafo_dicionario[vertice] = []
            print(vertice)

    def adicionar_aresta(self, aresta):
        """ A "aresta" pode ser do tipo set, tupla ou lista;
        entre dois vértices pode ter várias arestas.
        """
        aresta = set(aresta)
        (vertice1, vertice2) = tuple(aresta)
        if vertice1 in self.__grafo_dicionario:
            self.__grafo_dicionario[vertice1].append(vertice2)
        else:
            self.__grafo_dicionario[vertice1] = [vertice2]
        print(aresta)

    def __gerar_arestas(self):
        """ Método estático que gera as arestas do grafo.
            Arestas podem ser representadas como sets com
        um (se for loop) ou dois vertices.
        """
        arestas = []
        for vertice in self.__grafo_dicionario:
            for vizinho in self.__grafo_dicionario[vertice]:
                if {vizinho, vertice} not in arestas:
                    arestas.append({vertice, vizinho})
        return list(arestas)

    def verificar_aresta(self, aresta):
        """Método para verificar se a aresta existe"""
        (vertice1, vertice2) = tuple(aresta)
        result = ["Verificar existencia da aresta %s: " % aresta]
        result.append("A aresta existe") if {vertice1, vertice2} in self.arestas() else result.append(
            "A aresta não existe")
        print(''.join(result))

    def verificar_adjacencia(self, vertice):
        result = "Adjacencia do vértice '%s': " % vertice
        adjacencia = []
        for vizinho in self.__grafo_dicionario[vertice]:
            adjacencia.append(vizinho)
        result += str(adjacencia)
        print(result)

    def grau_vertice(self, vertice):
        # FIXME alterar para incluir grafos ponderados
        """ Grau do vértice, representa o número de arestas conectadas ao vértice.
        """
        result = "Grau do vértice '%s': " % vertice
        vertices_adjacentes = self.__grafo_dicionario[vertice]
        # valores = list(vertices_adjacentes.keys())
        grau = len(vertices_adjacentes) + vertices_adjacentes.count(vertice)
        result += str(grau)
        print(result)

    def __str__(self):
        # FIXME falta aprimorar
        """ Similar ao toString"""
        direcionado = self.verificar_direcionado()
        result = []
        result.append("Grafo direcionado") if direcionado else result.append("Grafo não direcionado")
        result.append("\nVertices: ")
        result.append(self.vertices())
        result.append("\nArestas: ")
        result.append(str(self.arestas()))
        print(''.join(str(e) for e in result))

    def encontrar_caminho(self, vertice_inicio, vertice_fim, caminho=None):
        """ Encontra um caminho entre dois vértices"""
        if caminho is None:
            caminho = []
        grafo = self.__grafo_dicionario
        caminho = caminho + [vertice_inicio]
        if vertice_inicio is vertice_fim:
            return caminho
        if vertice_inicio not in grafo:
            return None
        for vertice in grafo[vertice_inicio]:
            if vertice not in caminho:
                caminho_extendido = self.encontrar_caminho(vertice,
                                                           vertice_fim,
                                                           caminho)
                if caminho_extendido:
                    return caminho_extendido
        return None

    def imprime_caminho(self, vertice_inicio, vertice_fim):
        """ Imprime o caminho entre dois vertices. """
        result = ["Caminho do vértice '%s' para o vértice '%s': " % (vertice_inicio, vertice_fim)]
        caminho = str(self.encontrar_caminho(vertice_inicio, vertice_fim))
        result.append("Caminho não existe") if 'None' in caminho else result.append(caminho)
        print(''.join(result))

    def encontrar_todos_caminhos(self, vertice_inicio, vertice_fim, caminho=None):
        """ encontra todos os caminhos entre dois vértices """
        if caminho is None:
            caminho = []
        grafo = self.__grafo_dicionario
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

    def is_connected(self,
                     vertices_encountered=None,
                     start_vertex=None):
        """ Determina se o grafo é conexo """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__grafo_dicionario
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

    def verificar_conexo(self):
        """ Imprime o resultado se o grafo é conexo ou não."""
        result = ["Verificar se o grafo é conexo: "]
        result.append("O grafo é conexo") if self.is_connected() else result.append("O grafo não é conexo")
        print(''.join(result))

    def verificar_ciclico(self):
        """ Verifica se o grafo é cíclico"""
        result = ["Verificar se o grafo é cíclico: "]

        caminho = set()
        visitado = set()

        def visit(vertice):
            if vertice in visitado:
                return False
            visitado.add(vertice)
            caminho.add(vertice)
            for vizinho in self.__grafo_dicionario.get(vertice, ()):
                if vizinho in caminho or visit(vizinho):
                    return True
            caminho.remove(vertice)
            return False

        result.append("É cíclico") if any(visit(v) for v in self.__grafo_dicionario) else result.append("Não é ciclico")
        print(''.join(result))

    def verificar_fortemente_conexos(self):
        # TODO falta implementar
        if self.verificar_direcionado():
            tarjan_graph = self.tarjan()
            cont = 0
            for i in range(0, len(tarjan_graph)):
                for j in tarjan_graph[i]:
                    cont += 1
            print("Número de componentes fortemente conexos: %s" % cont)
            print("Componentes fortemente conexos: ", end='')
            print(tarjan_graph)

    def verificar_eureliano(self):
        # FIXME ajustar para grafo ponderado
        result = ["Verificar se o grafo é Euleriano: "]
        if not self.is_connected():
            result.append("Não é eureliano")
        else:
            odd = 0
            for vertice in self.vertices():
                if len(self.__grafo_dicionario[vertice]) % 2 is not 0:
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

    def verificar_direcionado(self):
        arestas = []
        arestas_invertidas = []
        v = self.vertices()
        for vertice in v:
            # print(vertice + ': ' + str(self.__grafo_dicionario[vertice]))
            for vertice_interno in self.__grafo_dicionario[vertice]:
                arestas.append((vertice, vertice_interno))
                arestas_invertidas.append((vertice_interno, vertice))
        arestas.sort()
        arestas_invertidas.sort()
        if arestas == arestas_invertidas:
            return False
        return True
        #     print("Grafo não direcionado")
        # print(arestas)
        # print(arestas_invertidas)

    def caminho_curto(self):
        # FIXME ajustar para grafo ponderado
        if self.is_connected():
            result = "O caminho mais curto é: "
            result += str(self.diameter())
            print(result)

    def encontrar_agm(self):
        # TODO implementar para grafo ponderado
        pass

    def plotar(self):
        if self.verificar_direcionado():
            graph = nx.MultiDiGraph(self.__grafo_dicionario)
        else:
            graph = nx.MultiGraph(self.__grafo_dicionario)
        # fig = plt.figure()
        # fig.suptitle(str(self), fontsize=20)
        nx.draw(graph, with_labels=True)
        plt.show()

    def tarjan(self):
        # FIXME falta revisar para grafo ponderado
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
        def strong_connect(vertex):

            # Empty graph object/list
            if not self:
                raise ValueError("Graph is empty.")

            index[vertex] = counter[0]  # Depth index v = smallest unused index
            lowlink[vertex] = counter[0]  # Computed during depth-first search from v
            counter[0] += 1  # counter++; Keep track of visits (used by stack)
            stack.append(vertex)  # Add vertex to stack = S.push(v)

            # Consider successors (edges) of v
            edges = self.__grafo_dicionario[vertex]
            # for each (v, w) in E do (iterate on graph[v])
            for w in edges:
                # If (w[index] undefined], successor hasn't been visited yet
                if w not in stack:
                    # Visit and add as successor
                    strong_connect(w)
                    lowlink[vertex] = min(lowlink[vertex], lowlink[w])
                # If w already in stack
                elif w in stack:
                    # Successor is a lowlink (smallest index reachable from v)
                    lowlink[vertex] = min(lowlink[vertex], index[w])

            # If v is a root node, pop the stack and generate an SCC
            # If current vertex = root vertex
            if lowlink[vertex] == index[vertex]:
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
                    if w == vertex:
                        break
                # Output the current strongly connected component
                # Store in tuple, immutable
                result.append(tuple(scc))

        vertices = self.__grafo_dicionario
        for v in vertices:
            # If v is unvisited, make it a SCC
            if v not in lowlink:
                strong_connect(v)

        # Return list of edges (tuples)
        return tuple(result)

    def dijsktra(self, initial):
        grafo = []
        for x in self.__grafo_dicionario.items():
            h = x[0]
            j = x[1].values()
            k = x[1].keys()
            # grafo.append(x[1])
            for y in x[1]:
                a = y
                grafo.append(y)
        print(grafo)
