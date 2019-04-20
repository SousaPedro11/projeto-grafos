import Entrada
import Utilitario
from Grafo import Grafo

lista = dir(Entrada)
for x in lista:
    if 'grafo' in x:
        print(x.replace('grafo', 'Grafo '))
        graph = Grafo(getattr(Entrada, x))
        Utilitario.teste_grafo(graph)
