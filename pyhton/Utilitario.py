import random


def __random_vertices(grafo):
    return random.choice(grafo.vertices())


def teste_grafo(grafo):
    a = __random_vertices(grafo)
    b = __random_vertices(grafo)
    if grafo.ponderado():
        while a is b:
            b = __random_vertices(grafo)
    grafo.__str__()
    print("q1.", end=' ')
    grafo.verificar_aresta(__random_vertices(grafo), __random_vertices(grafo))
    print("q2.", end=' ')
    grafo.grau_vertice(__random_vertices(grafo))
    print("q3.", end=' ')
    grafo.verificar_adjacencia(__random_vertices(grafo))
    print("q4.", end=' ')
    grafo.verificar_ciclico()
    print("q5.", end=' ')
    grafo.verificar_conexo()
    print("q6.", end=' ')
    grafo.verificar_fortemente_conexos()
    print("q7.", end=' ')
    grafo.verificar_eureliano()
    print("q8.", end=' ')
    grafo.imprime_caminho(a, b)
    print("q9.", end=' ')
    grafo.encontrar_agm(__random_vertices(grafo))
    # grafo.plotar()
    print()
