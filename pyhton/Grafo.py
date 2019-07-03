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
        """
        Descrição
        ---------
        Inicializa o grafo. Se não houver um dicionario, será usado um vazio.

        Parametros
        ----------
        grafo_dicionario : dict
            Dicionário que representa o grafo de entrada.
        """
        if grafo_dicionario is None:
            grafo_dicionario = {}
        self.__grafo_dicionario = grafo_dicionario
        global vertices_global
        global arestas_global
        global conectado_global
        global ponderado
        vertices_global = self.vertices()
        ponderado = self.is_weighted()
        arestas_global = self.arestas()
        if not self.is_directed():
            conectado_global = self.is_connected()
        else:
            graph = Grafo(self.to_undirected())
            conectado_global = graph.is_connected()

    def vertices(self):
        """
        Descrição
        ---------
        Método que identifica os vértices do grafo.

        Retorno
        -------
        vertices : list
            Vértices identificados no dicionário (grafo de entrada)
        """
        vertices = list(self.__grafo_dicionario.keys())
        return vertices

    def arestas(self):
        """
        Descrição
        ---------
        Método que identifica as arestas do grafo

        Retorno
        -------
        listaarestas : list
            Arestas identificadas no dicionário (grafo de entrada)
        """
        if self.is_directed():
            arestas = []
            for vertice in vertices_global:
                for vertice_interno in self.adjacentes(vertice):
                    arestas.append((vertice, vertice_interno))
            listaarestas = list(arestas)
        else:
            listaarestas = self.__gerar_arestas()
        return listaarestas

    def imprime_arestas(self):
        if self.is_directed():
            return self.arestas()
        else:
            arestas = []
            for vertice in self.__grafo_dicionario:
                for vizinho in self.adjacentes(vertice):
                    if {vizinho, vertice} not in arestas:
                        arestas.append({vertice, vizinho})
            return list(arestas)

    def adicionar_vertice(self, vertice):
        """
        Descrição
        ---------
        Método que adiciona vértices ao grafo
        Se o vertice não estiver presente no dicionário,
        uma chave vertice com uma lista vazia é adicionada.
        Se estiver presente, nada é feito.

        Parametros
        ----------
        vertice : str
            Vértice que será adicionado ao grafo
        """
        if vertice not in self.__grafo_dicionario:
            self.__grafo_dicionario[vertice] = []
            print(vertice)

    def adicionar_aresta(self, aresta):
        """
        Descrição
        ---------
        Método que adiciona aresta ao grafo.
        A "aresta" pode ser do tipo set, tupla ou lista
        Entre dois vértices pode ter várias arestas.

        Parametros
        ----------
        aresta : str
            Aresta que será adicionada ao grafo
        """
        aresta = set(aresta)
        (vertice1, vertice2) = tuple(aresta)
        if vertice1 in self.__grafo_dicionario:
            self.__grafo_dicionario[vertice1].append(vertice2)
        else:
            self.__grafo_dicionario[vertice1] = [vertice2]
        print(aresta)

    def __gerar_arestas(self):
        """
        Descrição
        ---------
        Método estático que gera as arestas do grafo.
            Arestas podem ser representadas como sets com
        um (se for loop) ou dois vertices.

        Retorno
        -------
        listaarestas : list
            Arestas identificadas no dicionário (grafo de entrada)
        """
        arestas = []
        for vertice in self.__grafo_dicionario:
            for vizinho in self.adjacentes(vertice):
                if {vizinho, vertice} not in arestas:
                    arestas.append((vertice, vizinho))
        listaarestas = list(arestas)
        return listaarestas

    def aresta_existe(self, vertice1, vertice2):
        """
        Descrição
        ---------
        Metodo que verifica se a aresta existe

        Parametros
        ----------
        vertice1 : str
            Representa o vértice de origem da aresta
        vertice2 : str
            Representa o vértice de destino da aresta

        Retorno
        -------
        : bool
            Retorna True se a aresta existir ou False caso não exista
        """
        # if {vertice1, vertice2} in arestas:
        direcionado = self.is_directed()
        for v1, v2 in arestas_global:
            ver1 = vertice1 == v1
            ver2 = vertice2 == v2
            ver3 = vertice1 == v2
            ver4 = vertice2 == v1
            verif1 = ver1 and ver2
            verif2 = ver3 and ver4
            if direcionado:
                if verif1:
                    return True
            else:
                if verif1 or verif2:
                    return True
        return False

    @staticmethod
    def vertice_existe(vertice):
        """
        Descrição
        ---------
        Metodo que verifica se o vértice existe

        Parametros
        ----------
        vertice : str
            Vértice a ser verificado pelo algoritmo

        Retorno
        -------
        : bool
            Retorna True se o vértice existir ou False caso não exista
        """
        if vertice in vertices_global:
            return True
        else:
            return False

    def verificar_aresta(self, vertice1, vertice2):
        """
        Descrição
        ---------
        Metodo que imprime na tela se a aresta existe, utilizando um método auxiliar

        Parametros
        ----------
        vertice1 : str
            Representa o vértice de origem da aresta
        vertice2 : str
            Representa o vértice de destino da aresta
        """
        result = ["Verificar existencia da aresta ('%s', '%s'): " % (vertice1, vertice2)]
        result.append("A aresta existe") if self.aresta_existe(vertice1, vertice2) else result.append(
            "A aresta não existe")
        print(''.join(result))

    def adjacentes(self, vertice):
        """
        Descrição
        ---------
        Metodo se há vertices adjacentes ao vértice base

        Parametros
        ----------
        vertice : str
            Vértice base que o algoritmo buscará as adjacências

        Retorno
        -------
        adjacencia : array
            Retorna a lista de vértices adjacentes ao vértice de entrada
        """
        # FIXME alterar para nova entrada - solucao do problema
        adjacencia = []
        for vizinho in self.__grafo_dicionario[vertice]:
            if isinstance(vizinho, tuple):
                k, v = tuple(vizinho)
                adjacencia.append(k)
            else:
                adjacencia.append(vizinho)
        return adjacencia

    def verificar_adjacencia(self, vertice):
        """
        Descrição
        ---------
        Metodo imprime o resultado da verificação de adjacência do vértice base

        Parametros
        ----------
        vertice : str
            Vertice base para ser verificada as adjacências
        """
        result = "Adjacencia do vértice '%s': " % vertice
        if self.vertice_existe(vertice):
            result += str(self.adjacentes(vertice))
        else:
            result += "O vértice não existe no grafo"
        print(result)

    def calcula_grau(self, vertice):
        if self.vertice_existe(vertice):
            if self.is_directed():
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
                return grau
            else:
                return len(self.adjacentes(vertice))
        else:
            print("Vértice não existe")

    def grau_vertice(self, vertice):
        """
        Descrição
        ---------
        Metodo que imprime o grau do vértice

        Parametros
        ----------
        vertice : str
            Vértice base que terá o grau verificado
        """
        result = "Grau do vértice '%s': " % vertice
        if self.vertice_existe(vertice):
            if self.is_directed():
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
                result += str(len(self.adjacentes(vertice)))
        else:
            result += "Vértice não existe"
        print(result)

    def __str__(self):
        """
        Descrição
        ---------
        Similar ao toString
        """
        result = []
        result.append("Grafo direcionado") if self.is_directed() else result.append("Grafo não direcionado")
        result.append("\nVertices: ")
        result.append(vertices_global)
        result.append("\nArestas: ")
        result.append(str(self.imprime_arestas()))
        print(''.join(str(e) for e in result))

    def encontrar_caminho(self, vertice_inicio, vertice_fim, caminho=None):
        """
        Descrição
        ---------
        Encontra caminho mínimo entre dois vértices não ponderados

        Parametros
        ----------
        vertice_inicio : str
            Vértice de origem
        vertice_fim : str
            Vértice de destino
        caminho : array
            Vértices visitados

        Retorno
        -------
        caminho : array or None
        """
        if caminho is None:
            caminho = []
        grafo = self.__grafo_dicionario
        caminho = caminho + [vertice_inicio]
        if vertice_inicio == vertice_fim:
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
        """
        Descrição
        ---------
        Metodo que imprime o caminho mínimo entre dois vértices, utilizando dois metodos para casos específicos

        Parametros
        ----------
        vertice_inicio : str
            Vertice de origem
        vertice_fim : str
            Vértice de destino
        """
        peso = 0
        result = ["Caminho do vértice '%s' para o vértice '%s': " % (vertice_inicio, vertice_fim)]
        inexistente = []
        inicio_existe = self.vertice_existe(vertice_inicio)
        fim_existe = self.vertice_existe(vertice_fim)
        ponderado = self.is_weighted()
        if not inicio_existe:
            inexistente.append("'" + vertice_inicio + "'")
        if not fim_existe:
            inexistente.append("'" + vertice_fim + "'")

        if inicio_existe and fim_existe:
            if ponderado:
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
                if ponderado:
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
        """
        Descrição
        ---------
        Encontra todos os caminhos entre dois vértices

        Parametros
        ----------
        vertice_inicio : str
            Vértice de origem
        vertice_fim : str
            Vértice de destino
        caminho : array
            Vértices visitados

        Retorno
        -------
        caminho : array
        """
        if caminho is None:
            caminho = []
        grafo = self.__grafo_dicionario
        caminho = caminho + [vertice_inicio]
        if vertice_inicio == vertice_fim:
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
        """
        Descrição
        ---------
        Verifica se o grafo é conexo

        Parametros
        ----------
        vertices_encountered : set
            Set de vértices encontrados
        start_vertex : str

        Retorno
        -------
        : bool
        """

        if vertices_encountered is None:
            vertices_encountered = set()
        # gdict = self.__grafo_dicionario
        vertices = vertices_global  # "list" necessary in Python 3
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in self.adjacentes(start_vertex):
                if vertex not in vertices_encountered and self.is_connected(vertices_encountered, vertex):
                    return True
        else:
            return True
        return False

    def testeConexo(self):
        if not self.is_directed():
            Deg = 0
            N = len(vertices_global)
            M = len(self.imprime_arestas())
            verificador = N * (N - 1) / 2
            print('arestas: ', M, '\tverificador: ', verificador)
            if M <= verificador:
                print('Grafo conexo')
            else:
                print("Grafo desconexo")

            for x in vertices_global:
                Deg += self.calcula_grau(x)
            print(Deg)

    def verificar_conexo(self):
        """
        Descrição
        ---------
        Imprime o resultado se o grafo é conexo ou não, utilizando o método de verificação.
        """
        result = ["Verificar se o grafo é conexo: "]
        # if not direcionado_global:
        result.append("O grafo é conexo") if conectado_global else result.append("O grafo não é conexo")
        # else:
        #     graph = Grafo(self.to_undirected())
        #     # conectado_global = graph.is_connected()
        #     result.append("O grafo é conexo") if conectado_global else result.append("O grafo não é conexo")
        print(''.join(result))

    def to_undirected(self):
        if self.is_directed():
            arestas = []
            for vertice in self.__grafo_dicionario:
                for vizinho in self.adjacentes(vertice):
                    if {vizinho, vertice} not in arestas:
                        arestas.append((vertice, vizinho))
                        arestas.append((vizinho, vertice))

            grafo = {}
            for k, _ in arestas:
                arr1 = []
                for _, v in arestas:
                    if (k, v) in arestas:
                        # print(k, v)
                        arr1.append(v) if v not in arr1 else ''
                # print(k, arr1)
                grafo[str(k)] = arr1
            return grafo

    def verificar_ciclico(self):
        """
        Descrição
        ---------
        Imprime se o grafo é cíclico ou não, utilizando um método interno como auxiliar.
        """
        result = ["Verificar se o grafo é cíclico: "]

        caminho = set()
        visitado = set()

        def visit(vertice):
            if vertice in visitado:
                return False
            visitado.add(vertice)
            caminho.add(vertice)
            # for vizinho in self.__grafo_dicionario.get(vertice, ()):
            for vizinho in self.adjacentes(vertice):
                if vizinho in caminho or visit(vizinho):
                    return True
            caminho.remove(vertice)
            return False

        result.append("É cíclico") if any(visit(v) for v in self.__grafo_dicionario) else result.append("Não é ciclico")
        print(''.join(result))

    def is_cyclic(self):
        result = ["Verificar se o grafo é cíclico: "]
        arestas = set(self.arestas())
        if self.is_directed():
            tam_arestas = len(arestas)
        else:
            tam_arestas = len(arestas) / 2

        if (tam_arestas > len(vertices_global) - 1):
            # print("Grafo Cíclico por Nº Aresta : %i >= Nº Vértices: %i" % (
            #     tam_arestas, len(vertices_global)))
            result.append("É cíclico - nº arestas (%i) >= nº vertices (%i)" % (tam_arestas, len(vertices_global)))
        else:
            result.append("Não é ciclico")
        print(''.join(result))

    def verificar_fortemente_conexos(self):
        """
        Descrição
        ---------
        Imprime se o grafo é fortemente conexo e caso seja mostra os compeonentes. É utilizado o
        método tarjan como auxiliar.
        """
        # FIXME ajustar o tarjan para nova entrada
        if self.is_directed():
            tarjan_graph = self.tarjan()
            cont = 0
            for _ in tarjan_graph:
                cont += 1
            print("Número de componentes fortemente conexos: %s" % cont)
            print("\tComponentes fortemente conexos: ", end='')
            print(tarjan_graph)
        else:
            print('O grafo não é fortemente conexo')

    def verificar_eureliano(self):
        """
        Descrição
        ---------
        Verifica e imprime se o grafo é euleriano
        """
        # FIXME ajustar para grafo conectado
        result = ["Verificar se o grafo é Euleriano: "]
        if not conectado_global:
            result.append("Não é eureliano")
        else:
            odd = 0
            for vertice in vertices_global:
                a = self.adjacentes(vertice)
                # if len(a) % 2 is not 0:
                if len(a) % 2 != 0:
                    odd += 1
            result.append("É Euleriano") if odd == 0 else result.append("Não é Euleriano")
        print(''.join(result))

    def diameter(self):
        """
        MÉTODO NÃO UTILIZADO
        Descrição
        ---------
        Encontra o caminho mais curto do grafo.

        Retorno
        -------
        caminho_curto[-1] : array
        """
        v = vertices_global
        pares = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]
        caminho_curto = []
        for (s, e) in pares:
            caminhos = self.encontrar_todos_caminhos(s, e)
            mais_curto = sorted(caminhos, key=len)[0]
            caminho_curto.append(mais_curto)
        caminho_curto.sort(key=len)
        return caminho_curto[-1]

    def is_directed(self):
        """
        Descrição
        ---------
        Verifica se o grafo é direcionado

        Retorno
        -------
        : bool
        """
        # FIXME falta corrigir para novo formato de entrada e adjacencia vazia
        arestas = []
        arestas_invertidas = []
        v = self.vertices()
        for vertice in v:
            for vertice_interno in self.__grafo_dicionario[vertice]:
                arestas.append((vertice, vertice_interno))
                arestas_invertidas.append((vertice_interno, vertice))
        arestas.sort()
        arestas_invertidas.sort()
        if arestas == arestas_invertidas:
            return False
        return True

    def encontrar_agm(self, vertice_inicial):
        """
        Descrição
        ---------
        Imprime a AGM do grafo usando algoritmo de prim, se possível.

        Parametros
        ----------
        vertice_vertice_inicial : str
            Vértice base
        """
        # TODO implementar para grafo ponderado
        # Grafo conectado, ponderado e não direcionado
        result = ["Arestas da AGM: "]
        vertice_existe = self.vertice_existe(vertice_inicial)

        condicao = []
        direcionado = self.is_directed()
        if vertice_existe:
            if not conectado_global:
                condicao.append("deve ser conectado")
            if not ponderado:
                condicao.append("deve ser ponderado")
            if direcionado:
                condicao.append("não deve ser direcionado")
        else:
            condicao.append("não apresenta o vértice '%s'" % vertice_inicial)

        if conectado_global and ponderado and not direcionado and vertice_existe:
            # lista = self.dijkstra(vertice_inicial)
            lista, peso_total = self.prim(vertice_inicial)
            result.append(', '.join(str(x) for x in lista))
            result.append("\n\tPeso da AGM: ")
            result.append(str(peso_total))
        else:
            result.append("O grafo " + ', '.join(condicao) + ".")
        print(''.join(result))

    def aresta_peso(self):
        """
        Descrição
        ---------
        Identifica o peso das arestas

        Retorno
        -------
        aresta_peso : set
        """
        aresta_peso = {}
        ponderado = self.is_weighted()
        if ponderado:
            for k, v in self.__grafo_dicionario.items():
                for k2, v2 in v.items():
                    if (k2, k, v2) not in aresta_peso:
                        aresta_peso[k, k2] = v2
        return aresta_peso
        # print(''.join(str(x) for x in aresta_peso))

    def aresta_ponderada(self):
        """
        Descrição
        ---------
        Identifica o peso das arestas

        Retorno
        -------
        aresta_peso : array
        """
        aresta_peso = []
        dict_aresta = self.aresta_peso()
        for e in dict_aresta.keys():
            peso = dict_aresta[e]
            k = e[0]
            v = e[1]
            aresta_peso.append((k, v, peso))
        return aresta_peso

    def plotar(self):
        """
        Descrição
        ---------
        Plota o grafo
        """
        # graph = nx.Graph(self.__grafo_dicionario)
        if self.is_directed():
            graph = nx.MultiDiGraph()
            # graph = nx.MultiDiGraph(self.__grafo_dicionario)
            # g = graphviz.Digraph(self.__grafo_dicionario)
        else:
            # graph = nx.MultiGraph(self.__grafo_dicionario)
            graph = nx.MultiGraph()
            # g = graphviz.Digraph(self.__grafo_dicionario)
        # fig = plt.figure()
        # fig.suptitle(str(self), fontsize=20)
        graph.add_nodes_from(vertices_global)
        ponderado = self.is_weighted()
        graph.add_weighted_edges_from(self.aresta_ponderada()) if ponderado else graph.add_edges_from(
            self.arestas())
        pos = nx.spring_layout(graph)
        # nx.draw(graph, pos, with_labels=True)
        nx.draw_networkx_nodes(graph, pos)
        nx.draw_networkx_labels(graph, pos)
        nx.draw_networkx_edges(graph, pos)
        if ponderado:
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=self.aresta_peso())
        plt.axis('off')
        plt.show()
        # g.view()

    def tarjan(self):
        """
        Descrição
        ---------
        Encontra os componentes fortemente conexos do grafo

        Retorno
        -------
        tuple(resultado) : tuple
        """
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

            if ponderado:
                # for vert in self.__grafo_dicionario[vertex]:
                for vert in self.adjacentes(vertex):
                    edges.append(vert)
            else:
                edges = self.adjacentes(vertex)
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

    def is_weighted(self):
        """
        Descrição
        ---------
        Verifica se o grafo é ponderado

        Retorno
        -------
        : bool
        """
        for k, v in self.__grafo_dicionario.items():
            if isinstance(v, dict):
                return True
            else:
                return False

    @staticmethod
    def traceback_path(target, parents):
        """
        Descrição
        ---------
        Encontra caminho entre dois vértices num grafo ponderado

        Parametros
        ----------
        target : str
        parents : set

        Retorno
        -------
        list(reversed(path)) : list
        """
        path = []
        while target:
            path.append(target)
            target = parents[target]
        # print(str(list(reversed(path))))
        return list(reversed(path))

    def encontrar_caminho_ponderado(self, start, finish):
        """
        Descrição
        ---------
        Encontra caminho entre dois vértices num grafo ponderado

        Parametros
        ----------
        start : str
            Vértice de origem
        finish : str
            Vértice de destino

        Retorno
        -------
        traceback_path(finish, parents) : list
        """
        # FIXME ajustar para nova entrada
        aberto = [HeapEntry(start, 0.0)]
        closed = set()
        parents = {start: None}
        distance = {start: 0.0}

        while aberto:
            current = heapq.heappop(aberto).node

            if current == finish:
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
        """
        Descrição
        ---------
        Encontra custo entre dois vértices

        Parametros
        ----------
        vertex1 : str
            Vértice de origem
        vertex2 : str
            Vértice de destino

        Retorno
        -------
        valor : int
        """
        list_v1 = self.__grafo_dicionario.items()
        custo = math.inf
        for v, cost in list_v1:
            if v == vertex1:
                # custo = [value for (key, value) in cost.items() if key == vertex2]
                for key, value in cost.items():
                    if key == vertex2:
                        custo = value
        return custo

    def caminho_ponderado_peso(self, caminho):
        """
        Descrição
        ---------
        Encontra o custo total de um caminho

        Parametros
        ----------
        caminho : array
            Caminho a ser calculado o custo

        Retorno
        -------
        peso : int
        """
        peso = 0
        for v in range(len(caminho) - 1):
            vatual = caminho[v]
            vpos = caminho[v + 1]
            peso += self.direct_cost(vatual, vpos)
        return peso

    def prim(self, root):
        """
        Descrição
        ---------
        Encontra a AGM

        Parametros
        ----------
        root : str
            Vértice base

        Retorno
        -------
        selected_edges : array
        weight : int
        """
        # Grafo conectado, ponderado e não direcionado
        vertex = [root]  # Lista dos vertices a partir do qual buscamos as arestas
        selected_edges = []  # Lista com as arestas selecionadas

        weight = 0  # Peso do minimum spanning tree

        remaing_vertices = list(vertices_global)  # Lista com os vertices destinos da busca
        remaing_vertices.remove(root)  # O root eh ponto de partida, entao sai da lista

        tam_rem_vert = len(remaing_vertices)
        for i in range(tam_rem_vert):  # Devemos buscar |V| - 1 vertices
            min_cost = math.inf  # Inicializamos o custo minimo como infinito
            va, vb = None, None  # Vertices candidatos para a aresta selecionada
            for v1 in vertex:  # Para cada vertice na lista de busca origem
                for v2 in remaing_vertices:  # Buscamos os vertices que ainda nao estao no grafo final
                    aresta_existe = self.aresta_existe(v1, v2)
                    if not aresta_existe:
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
