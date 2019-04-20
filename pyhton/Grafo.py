""" A Python Class"""
import heapq
import math

import matplotlib.pyplot as plt
import networkx as nx


class HeapEntry:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


class Grafo(object):

    def __init__(self, grafo_dicionario=None):
        """ Inicializa o grafo.
            Se não houver um dicionario, será usado um vazio
        """
        if grafo_dicionario is None:
            grafo_dicionario = {}
        self.__grafo_dicionario = grafo_dicionario
        global vertices_global
        global direcionado_global
        global arestas_global
        global conectado_global
        global ponderado_global
        # self.weight = {0}
        vertices_global = self.vertices()
        ponderado_global = self.ponderado()
        direcionado_global = self.verificar_direcionado()
        arestas_global = self.arestas()
        conectado_global = self.is_connected()

    def vertices(self):
        return list(self.__grafo_dicionario.keys())

    def arestas(self):
        if direcionado_global:
            arestas = []
            for vertice in vertices_global:
                for vertice_interno in self.__grafo_dicionario[vertice]:
                    # if ponderado_global:
                    #     arestas.append((vertice, vertice_interno[0]))
                    arestas.append((vertice, vertice_interno[0]))
            return list(arestas)
        else:
            return self.__gerar_arestas()

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
                    arestas.append({vertice, vizinho[0]})
        return list(arestas)

    def verificar_aresta(self, vertice1, vertice2):
        """Método para verificar se a aresta existe"""
        result = ["Verificar existencia da aresta ('%s', '%s'): " % (vertice1, vertice2)]
        result.append("A aresta existe") if self.aresta_existe(vertice1, vertice2) else result.append(
                "A aresta não existe")
        print(''.join(result))

    def aresta_existe(self, vertice1, vertice2):
        # if {vertice1, vertice2} in arestas:
        for v1, v2 in arestas_global:
            verif1 = vertice1 is v1 and vertice2 is v2
            verif2 = vertice1 is v2 and vertice2 is v1
            if direcionado_global:
                if verif1:
                    return True
            else:
                if verif1 or verif2:
                    return True
        return False

    def verificar_vertice(self, vertice):
        """Verifica se o vértice existe"""
        if vertice in vertices_global:
            return True
        else:
            return False

    def adjacentes(self, vertice):
        # FIXME alterar para nova entrada - solucao do problema
        adjacencia = []
        for vizinho in self.__grafo_dicionario[vertice]:
            adjacencia.append(vizinho)
        return adjacencia

    def verificar_adjacencia(self, vertice):
        result = "Adjacencia do vértice '%s': " % vertice
        # adjacencia = []
        # for vizinho in self.__grafo_dicionario[vertice]:
        #     adjacencia.append(vizinho)
        if self.verificar_vertice(vertice):
            result += str(self.adjacentes(vertice))
        else:
            result += "O vértice não existe no grafo"
        print(result)

    def grau_vertice(self, vertice):
        # FIXME alterar para incluir grafos ponderados
        """ Grau do vértice, representa o número de arestas conectadas ao vértice.
        """
        result = "Grau do vértice '%s': " % vertice
        if self.verificar_vertice(vertice):
            ocorrencias = []
            arestas = self.__gerar_arestas()
            for v in arestas:
                if len(v) > 1:
                    v1, v2 = tuple(v)
                else:
                    element = next(iter(v))
                    v1, v2 = element, element
                ocorrencias.append(v1)
                ocorrencias.append(v2)
            grau = ocorrencias.count(vertice)
            result += str(grau)
        else:
            result += "Vértice não existe"
        print(result)

    def __str__(self):
        """ Similar ao toString"""
        result = []
        result.append("Grafo direcionado") if direcionado_global else result.append("Grafo não direcionado")
        result.append("\nVertices: ")
        result.append(vertices_global)
        result.append("\nArestas: ")
        result.append(str(arestas_global))
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
        peso = 0
        result = ["Caminho do vértice '%s' para o vértice '%s': " % (vertice_inicio, vertice_fim)]
        inexistente = []
        inicio_existe = self.verificar_vertice(vertice_inicio)
        fim_existe = self.verificar_vertice(vertice_fim)
        if not inicio_existe:
            inexistente.append("'" + vertice_inicio + "'")
        if not fim_existe:
            inexistente.append("'" + vertice_fim + "'")

        if inicio_existe and fim_existe:
            if ponderado_global:
                caminho = self.encontrar_caminho_ponderado(vertice_inicio, vertice_fim)
                if 'None' not in str(caminho):
                    peso = self.caminho_ponderado_peso(caminho)
            else:
                caminho = self.encontrar_caminho(vertice_inicio, vertice_fim)
            # result.append("Caminho não existe") if 'None' in str(caminho) else result.append(str(caminho))
            if 'None' in str(caminho):
                result.append("Caminho não existe")
            else:
                result.append(str(caminho))
                if ponderado_global:
                    result.append("\n\tCusto do caminho: ")
                    result.append(str(peso))
        else:
            if len(inexistente) == 1:
                result.append("Vértice " + ''.join(inexistente))
                result.append(" não presente no grafo.")
            elif len(inexistente) > 1:
                result.append("Vértices " + ' e '.join(inexistente))
                result.append(" não presentes no grafo.")
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
        # FIXME falta ajustar
        """ Determina se o grafo é conexo """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__grafo_dicionario
        vertices = vertices_global  # "list" necessary in Python 3
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex[0] not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex[0]):
                        return True
        else:
            return True
        return False

    def verificar_conexo(self):
        """ Imprime o resultado se o grafo é conexo ou não."""
        result = ["Verificar se o grafo é conexo: "]
        result.append("O grafo é conexo") if conectado_global else result.append("O grafo não é conexo")
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
        # FIXME
        if direcionado_global:
            tarjan_graph = self.tarjan()
            cont = 0
            for i in range(0, len(tarjan_graph)):
                for _ in tarjan_graph[i]:
                    cont += 1
            print("Número de componentes fortemente conexos: %s" % cont)
            print("\tComponentes fortemente conexos: ", end='')
            print(tarjan_graph)
        else:
            print('O grafo não é fortemente conexo')

    def verificar_eureliano(self):
        # FIXME ajustar para grafo ponderado
        result = ["Verificar se o grafo é Euleriano: "]
        if not conectado_global:
            result.append("Não é eureliano")
        else:
            odd = 0
            for vertice in vertices_global:
                if len(self.__grafo_dicionario[vertice]) % 2 is not 0:
                    odd += 1
            result.append("É Euleriano") if odd is 0 else result.append("Não é Euleriano")
        print(''.join(result))

    def diameter(self):
        # FIXME falta corrigir ou substituir o algoritmo
        v = vertices_global
        pares = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]
        caminho_curto = []
        for (s, e) in pares:
            caminhos = self.encontrar_todos_caminhos(s, e)
            mais_curto = sorted(caminhos, key=len)[0]
            caminho_curto.append(mais_curto)
        caminho_curto.sort(key=len)
        return caminho_curto[-1]

    def verificar_direcionado(self):
        # FIXME falta corrigir para novo formato de entrada
        arestas = []
        arestas_invertidas = []
        v1 = ''
        peso = 0
        for vertice in vertices_global:
            vertices_internos = self.__grafo_dicionario[vertice]
            if ponderado_global:
                vertice_interno = v1, peso
            else:
                vertice_interno = v1
            for vertice_interno in vertices_internos:
                arestas.append((vertice, vertice_interno[0]))
                arestas_invertidas.append((vertice_interno[0], vertice))
        arestas.sort()
        arestas_invertidas.sort()
        if arestas == arestas_invertidas:
            return False
        return True

    def encontrar_agm(self, vertice_inicial):
        # TODO implementar para grafo ponderado
        # Grafo conectado, ponderado e não direcionado
        result = ["Arestas da AGM: "]
        vertice_existe = self.verificar_vertice(vertice_inicial)

        condicao = []
        if vertice_existe:
            if not conectado_global:
                condicao.append("deve ser conectado")
            if not ponderado_global:
                condicao.append("deve ser ponderado")
            if direcionado_global:
                condicao.append("não deve ser direcionado")
        else:
            condicao.append("não apresenta o vértice '%s'" % vertice_inicial)

        if conectado_global and ponderado_global and not direcionado_global and vertice_existe:
            # lista = self.dijkstra(vertice_inicial)
            lista, peso_total = self.prim(vertice_inicial)
            result.append(', '.join(str(x) for x in lista))
            result.append("\n\tPeso da AGM: ")
            result.append(str(peso_total))
        else:
            result.append("O grafo " + ', '.join(condicao) + ".")
        print(''.join(result))

    def aresta_peso(self):
        aresta_peso = {}
        if ponderado_global:
            for k, v in self.__grafo_dicionario.items():
                for k2, v2 in v.items():
                    if (k2, k, v2) not in aresta_peso:
                        aresta_peso[k, k2] = v2
        return aresta_peso
        # print(''.join(str(x) for x in aresta_peso))

    def plotar(self):
        # graph = nx.Graph(self.__grafo_dicionario)
        if direcionado_global:
            graph = nx.MultiDiGraph(self.__grafo_dicionario)
            # g = graphviz.Digraph(self.__grafo_dicionario)
        else:
            graph = nx.MultiGraph(self.__grafo_dicionario)
            # g = graphviz.Digraph(self.__grafo_dicionario)
        # fig = plt.figure()
        # fig.suptitle(str(self), fontsize=20)
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True)
        if ponderado_global:
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=self.aresta_peso())
        plt.axis('off')
        plt.show()
        # g.view()

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
            # FIXME falta corrigir para novas entradas
            # Empty graph object/list
            if not self:
                raise ValueError("Graph is empty.")
            edges = []
            index[vertex] = counter[0]  # Depth index v = smallest unused index
            lowlink[vertex] = counter[0]  # Computed during depth-first search from v
            counter[0] += 1  # counter++; Keep track of visits (used by stack)
            stack.append(vertex)  # Add vertex to stack = S.push(v)

            # Consider successors (edges) of v

            if ponderado_global:
                for vert in self.__grafo_dicionario[vertex]:
                    edges.append(vert[0])
            else:
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

    def ponderado(self):
        for k, v in self.__grafo_dicionario.items():
            for vi in v:
                if len(vi) < 1:
                    continue
                if isinstance(vi, tuple):
                    return True
                else:
                    return False

    @staticmethod
    def traceback_path(target, parents):
        path = []
        while target:
            path.append(target)
            target = parents[target]
        # print(str(list(reversed(path))))
        return list(reversed(path))

    def encontrar_caminho_ponderado(self, start, finish):
        aberto = [HeapEntry(start, 0.0)]
        closed = set()
        parents = {start: None}
        distance = {start: 0.0}

        while aberto:
            current = heapq.heappop(aberto).node

            if current is finish:
                return self.traceback_path(finish, parents)

            if current in closed:
                continue

            closed.add(current)

            for child in self.__grafo_dicionario[current].keys():
                if child in closed:
                    continue
                tentative_cost = distance[current] + self.__grafo_dicionario[current][child]

                if child not in distance.keys() or distance[child] > tentative_cost:
                    distance[child] = tentative_cost
                    parents[child] = current
                    heap_entry = HeapEntry(child, tentative_cost)
                    heapq.heappush(aberto, heap_entry)

    def direct_cost(self, vertex1, vertex2):
        list_v1 = self.__grafo_dicionario.items()
        custo = []
        for v, cost in list_v1:
            if v is vertex1:
                custo = [value for (key, value) in cost.items() if key is vertex2]
        valor = custo[0]
        return valor
        # if v is vertex1 and v2 is vertex2:
        #     return cost
        # else:
        #     return math.inf

    def caminho_ponderado_peso(self, caminho):
        peso = 0
        for v in range(len(caminho) - 1):
            vatual = caminho[v]
            vpos = caminho[v + 1]
            peso += self.direct_cost(vatual, vpos)
        return peso

    def prim(self, root):
        # Grafo conectado, ponderado e não direcionado
        if not direcionado_global and conectado_global and ponderado_global:
            vertex = [root]  # Lista dos vertices a partir do qual buscamos as arestas
            selected_edges = []  # Lista com as arestas selecionadas

            weight = 0  # Peso do minimum spanning tree

            remaing_vertices = list(vertices_global)  # Lista com os vertices destinos da busca
            remaing_vertices.remove(root)  # O root eh ponto de partida, entao sai da lista

            for i in range(len(remaing_vertices)):  # Devemos buscar |V| - 1 vertices
                min_cost = math.inf  # Inicializamos o custo minimo como infinito
                va, vb = None, None  # Vertices candidatos para a aresta selecionada
                for v1 in vertex:  # Para cada vertice na lista de busca origem
                    for v2 in remaing_vertices:  # Buscamos os vertices que ainda nao estao no grafo final
                        if not self.aresta_existe(v1, v2):
                            cost = math.inf
                        else:
                            cost = self.direct_cost(v1, v2)  # Calcula o custo da aresta
                        if cost < min_cost:  # Se for menor que o minimo ate entao, atualizamos os dados
                            va = v1
                            vb = v2
                            min_cost = cost

                if min_cost < math.inf:  # Depois de todas as buscas, se o custo eh finito:
                    # selected_edges.append((va, vb, min_cost))  # Adicionamos a aresta de va a vb na solucao
                    selected_edges.append((va, vb))  # Adicionamos a aresta de va a vb na solucao
                    vertex.append(vb)  # vb agora sera nova origem de busca
                    remaing_vertices.remove(vb)  # vb nao mais sera destino de busca, pois ja consta na solucao
                    weight += min_cost  # Atualiza o peso

            return selected_edges, weight  # Retorna a lista de arestas selecionadas com o peso total
