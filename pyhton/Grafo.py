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
        """ returns the vertices of a graph """
        # print("Vertices:")
        return self.__grafo_dicionario.keys()

    def arestas(self):
        """ returns the arestas of a graph """
        # print("Arestas:")
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
        """ Método para verificar se a aresta existe"""
        (vertice1, vertice2) = tuple(aresta)
        print("Verificar existencia da aresta %s: " % aresta)
        if {vertice1, vertice2} in self.arestas():
            return "A aresta existe"
        return "A aresta não existe"

    def verificar_adjacencia(self, vertice):
        adjacencia = []
        for vizinhanca in self.__grafo_dicionario[vertice]:
            adjacencia.append(vizinhanca)
        return adjacencia

    def grau_vertice(self, vertice):
        """ The grau of a vertice is the number of arestas connecting
            it, i.e. the number of adjacencia vertices. Loops are counted
            double, i.e. every occurence of vertice in the list
            of adjacencia vertices. """
        vertices_adjacentes = self.__grafo_dicionario[vertice]
        grau = len(vertices_adjacentes) + vertices_adjacentes.count(vertice)
        return grau

    def __str__(self):
        result = "Vertices: ["
        result += ', '.join(self.vertices()) + "]"
        # for k in self.__grafo_dicionario:
        #     result += str(k) + " "
        result += "\nArestas: "
        result += ''.join(str(self.arestas()))
        # for aresta in self.arestas():
        #     result += str(aresta) + " "
        return result

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
