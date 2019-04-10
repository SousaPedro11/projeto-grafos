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
            for vizinhanca in self.__grafo_dicionario[vertice]:
                if {vizinhanca, vertice} not in arestas:
                    arestas.append({vertice, vizinhanca})
        return list(arestas)

    def verificar_aresta(self, aresta):
        """Método para verificar se a aresta existe"""
        (vertice1, vertice2) = tuple(aresta)
        result = "Verificar existencia da aresta %s: " % aresta
        if {vertice1, vertice2} in self.arestas():
            result += "A aresta existe"
        else:
            result += "A aresta não existe"
        print(result)

    def verificar_adjacencia(self, vertice):
        result = "Adjacencia do vértice '%s': " % vertice
        adjacencia = []
        for vizinhanca in self.__grafo_dicionario[vertice]:
            adjacencia.append(vizinhanca)
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
        # result += ', '.join(self.vertices()) + "]"
        result += str(self.vertices())
        # for k in self.__grafo_dicionario:
        #     result += str(k) + " "
        result += "\nArestas: "
        result += ''.join(str(self.arestas()))
        # for aresta in self.arestas():
        #     result += str(aresta) + " "
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
        result = "Caminho do vértice '%s' para o vértice '%s': " % (vertice_inicio, vertice_fim)
        caminho = str(self.encontrar_caminho(vertice_inicio, vertice_fim))
        if 'None' in caminho:
            result += "Caminho não existe"
        else:
            result += caminho
        print(result)
        # return None

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


if __name__ is "__main__":
    g = {"a": ["d", "f"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": ["d"]
         }

    graph = Grafo(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("arestas of graph:")
    print(graph.arestas())

    print("Add vertice:")
    graph.adicionar_vertice("z")

    print("Vertices of graph:")
    print(graph.vertices())

    print("Add an aresta:")
    graph.adicionar_aresta({"a", "z"})

    print("Vertices of graph:")
    print(graph.vertices())

    print("arestas of graph:")
    print(graph.arestas())

    print('Adding an aresta {"x","y"} with new vertices:')
    graph.adicionar_aresta({"x", "y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("arestas of graph:")
    print(graph.arestas())

    print('The path from vertice "a" to vertice "b":')
    path = graph.encontrar_caminho("a", "b")
    print(path)

    print('The path from vertice "a" to vertice "f":')
    path = graph.encontrar_caminho("a", "f")
    print(path)

    print('The path from vertice "c" to vertice "c":')
    path = graph.encontrar_caminho("c", "c")
    print(path)

    print('All paths from vertice "a" to vertice "b":')
    path = graph.encontrar_todos_caminhos("a", "b")
    print(path)

    print('All paths from vertice "a" to vertice "f":')
    path = graph.encontrar_todos_caminhos("a", "f")
    print(path)

    print('All paths from vertice "c" to vertice "c":')
    path = graph.encontrar_todos_caminhos("c", "c")
    print(path)
