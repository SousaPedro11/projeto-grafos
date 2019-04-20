from pyhton.main import Entrada
from pyhton.main.Grafo import Grafo
from pyhton.util import Utilitario

lista = dir(Entrada)
for x in lista:
    if 'grafo' in x:
        print(x.replace('grafo', 'Grafo '))
        graph = Grafo(getattr(Entrada, x))
        Utilitario.teste_grafo(graph)
