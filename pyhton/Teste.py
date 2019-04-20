import Entrada
import Grafo
import Utilitario

lista = dir(Entrada)
for x in lista:
    if 'grafo' in x:
        print(x.replace('grafo', 'Grafo '))
        graph = Grafo.Grafo(getattr(Entrada, x))
        Utilitario.teste_grafo(graph)
