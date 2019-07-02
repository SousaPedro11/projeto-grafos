import random


def __random_vertices(grafo):
    return random.choice(grafo.vertices())


def teste_grafo(grafo):
    a = __random_vertices(grafo)
    b = __random_vertices(grafo)
    if grafo.is_weighted():
        while a is b:
            b = __random_vertices(grafo)
    grafo.__str__()  # OK
    print("q1.", end=' ')
    grafo.verificar_aresta(a, b)  # OK
    print("q2.", end=' ')
    grafo.grau_vertice(__random_vertices(grafo))  # OK
    print("q3.", end=' ')
    grafo.verificar_adjacencia(__random_vertices(grafo))  # OK
    print("q4.", end=' ')
    grafo.is_cyclic()  # OK
    print("q5.", end=' ')
    grafo.verificar_conexo()  # OK
    # print("q6.", end=' ')
    # grafo.verificar_fortemente_conexos()  # FIXME
    print("q7.", end=' ')
    grafo.verificar_eureliano()  # OK
    print("q8.", end=' ')
    grafo.imprime_caminho(a, b)  # OK
    # print("q9.", end=' ')
    # grafo.encontrar_agm(__random_vertices(grafo))  # FIXME
    # grafo.plotar()
    print()
