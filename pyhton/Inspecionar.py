import inspect

import Entrada
from Grafo import Grafo

# import Grafo as gf
graph = Grafo(Entrada.grafo01)

# for x in Grafo:
funcoes = inspect.getmembers(Grafo, predicate=inspect.isfunction)
for x in funcoes:
    nome = x[0]
    funcao = x[1]
    h = inspect.signature(funcao)
    if callable(funcao):
        # print(dir(funcao))
        print(nome, h, '\n' + str(x[1].__doc__))


# method_list = [func for func in dir(Grafo) if callable(getattr(Grafo, func))]
# metodo0 = method_list[0]
# print(metodo0)
