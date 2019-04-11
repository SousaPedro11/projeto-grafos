""" A Python Class
A simple Python graph class, demonstrating the essential
facts and functionalities of graphs.
"""


class Grafo(object):

    def __init__(self, grafo_dicionario=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if grafo_dicionario is None:
            grafo_dicionario = {}
        self.__grafo_dicionario = grafo_dicionario

    def vertices(self):
        return list(self.__grafo_dicionario.keys())

    def arestas(self):
        return self.__gerar_arestas()

    def adicionar_vertice(self, vertice):
        """ If the vertice "vertice" is not in
            self.__graph_dict, a key "vertice" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertice not in self.__grafo_dicionario:
            self.__grafo_dicionario[vertice] = []
            print(vertice)

    def adicionar_aresta(self, aresta):
        """ assumes that aresta is of type set, tuple or list;
            between two vertices can be multiple arestas!
        """
        aresta = set(aresta)
        (vertice1, vertice2) = tuple(aresta)
        if vertice1 in self.__grafo_dicionario:
            self.__grafo_dicionario[vertice1].append(vertice2)
        else:
            self.__grafo_dicionario[vertice1] = [vertice2]
        print(aresta)

    def __gerar_arestas(self):
        """ A static method generating the arestas of the
            graph "graph". arestas are represented as sets
            with one (a loop back to the vertice) or two
            vertices
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
        """ The grau of a vertice is the number of arestas connecting
            it, i.e. the number of adjacencia vertices. Loops are counted
            double, i.e. every occurence of vertice in the list
            of adjacencia vertices. """
        result = "Grau do vértice '%s': " % vertice
        vertices_adjacentes = self.__grafo_dicionario[vertice]
        grau = len(vertices_adjacentes) + vertices_adjacentes.count(vertice)
        result += str(grau)
        print(result)

    def __str__(self):
        result = "Vertices: "
        result += str(self.vertices())
        result += "\nArestas: "
        result += ''.join(str(self.arestas()))
        print(result)

    def encontrar_caminho(self, vertice_inicio, vertice_fim, caminho=None):
        """ find a path from start_vertice to end_vertice
            in graph """
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
        result = ["Caminho do vértice '%s' para o vértice '%s': " % (vertice_inicio, vertice_fim)]
        caminho = str(self.encontrar_caminho(vertice_inicio, vertice_fim))
        result.append("Caminho não existe") if 'None' in caminho else result.append(caminho)
        print(''.join(result))

    def encontrar_todos_caminhos(self, vertice_inicio, vertice_fim, caminho=None):
        """ find all paths from start_vertice to
            end_vertice in graph """
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
        """ determines if the graph is connected """
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
        result = ["Verificar se o grafo é conexo: "]
        result.append("O grafo é conexo") if self.is_connected() else result.append("O grafo não é conexo")
        print(''.join(result))

    def verificar_ciclico(self):
        result = ["Verificar se o grafo é cíclico: "]
        # path = set()
        #
        # def visit(vertice):
        #     path.add(vertice)
        #     for vizinho in self.__grafo_dicionario.get(vertice, ()):
        #         if vizinho in path or visit(vizinho):
        #             return True
        #     path.remove(vertice)
        #     return False
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
        pass

    def verificar_eurreliano(self):
        pass

    def diameter(self):
        v = self.vertices()
        pares = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]
        caminho_curto = []
        for (s, e) in pares:
            caminhos = self.encontrar_todos_caminhos(s, e)
            mais_curto = sorted(caminhos, key=len)[0]
            caminho_curto.append(mais_curto)
        caminho_curto.sort(key=len)

        # longest path is at the end of list,
        # i.e. diameter corresponds to the length of this path
        # diameter = len(smallest_paths[-1])
        # return diameter
        return caminho_curto[-1]

    def caminho_curto(self):
        if self.is_connected():
            result = "O caminho mais curto é: "
            result += str(self.diameter())
            print(result)

    def encontrar_agm(self):
        pass

    # def cyclic(self):
    #     """Return True if the directed graph has a cycle.
    #     The graph must be represented as a dictionary mapping vertices to
    #     iterables of neighbouring vertices. For example:
    #     False"""
    #
    #     visited = set()
    #     path = [object()]
    #     path_set = set(path)
    #     stack = [iter(self.__grafo_dicionario)]
    #     while stack:
    #         for v in stack[-1]:
    #             if v in path_set:
    #                 return True
    #             elif v not in visited:
    #                 visited.add(v)
    #                 path.append(v)
    #                 path_set.add(v)
    #                 stack.append(iter(self.__grafo_dicionario.get(v, ())))
    #                 break
    #         else:
    #             path_set.remove(path.pop())
    #             stack.pop()
    #     return False

# if __name__ is "__main__":
#     g = {"a": ["d", "f"],
#          "b": ["c"],
#          "c": ["b", "c", "d", "e"],
#          "d": ["a", "c"],
#          "e": ["c"],
#          "f": ["d"]
#          }
#
#     graph = Grafo(g)
#
#     print("Vertices of graph:")
#     print(graph.vertices())
#
#     print("arestas of graph:")
#     print(graph.arestas())
#
#     print("Add vertice:")
#     graph.adicionar_vertice("z")
#
#     print("Vertices of graph:")
#     print(graph.vertices())
#
#     print("Add an aresta:")
#     graph.adicionar_aresta({"a", "z"})
#
#     print("Vertices of graph:")
#     print(graph.vertices())
#
#     print("arestas of graph:")
#     print(graph.arestas())
#
#     print('Adding an aresta {"x","y"} with new vertices:')
#     graph.adicionar_aresta({"x", "y"})
#     print("Vertices of graph:")
#     print(graph.vertices())
#     print("arestas of graph:")
#     print(graph.arestas())
#
#     print('The path from vertice "a" to vertice "b":')
#     path = graph.encontrar_caminho("a", "b")
#     print(path)
#
#     print('The path from vertice "a" to vertice "f":')
#     path = graph.encontrar_caminho("a", "f")
#     print(path)
#
#     print('The path from vertice "c" to vertice "c":')
#     path = graph.encontrar_caminho("c", "c")
#     print(path)
#
#     print('All paths from vertice "a" to vertice "b":')
#     path = graph.encontrar_todos_caminhos("a", "b")
#     print(path)
#
#     print('All paths from vertice "a" to vertice "f":')
#     path = graph.encontrar_todos_caminhos("a", "f")
#     print(path)
#
#     print('All paths from vertice "c" to vertice "c":')
#     path = graph.encontrar_todos_caminhos("c", "c")
#     print(path)
