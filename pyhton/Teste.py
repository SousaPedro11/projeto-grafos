import Entrada
import Utilitario
from Grafo import Grafo

__excluidos = ['grafo01', 'grafo02']


def executar():
    __teste(__excluidos)


def __teste(excl=None, *filtro):
    lista = dir(Entrada)
    excl.append(x for x in filtro)
    for x in lista:
        if x not in excl:
            if 'grafo' in x:
                print(x.replace('grafo', 'Grafo '))
                graph = Grafo(getattr(Entrada, x))
                Utilitario.teste_grafo(graph)


executar()
