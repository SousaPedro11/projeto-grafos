import random


def random_vertices(Grafo):
    return random.choice(Grafo.vertices())


def teste_grafo(Grafo):
    a = random_vertices(Grafo)
    b = random_vertices(Grafo)
    if Grafo.ponderado():
        while a is b:
            b = random_vertices(Grafo)
    Grafo.__str__()
    print("q1.", end=' ')
    Grafo.verificar_aresta(random_vertices(Grafo), random_vertices(Grafo))
    print("q2.", end=' ')
    Grafo.grau_vertice(random_vertices(Grafo))
    print("q3.", end=' ')
    Grafo.verificar_adjacencia(random_vertices(Grafo))
    print("q4.", end=' ')
    Grafo.verificar_ciclico()
    print("q5.", end=' ')
    Grafo.verificar_conexo()
    print("q6.", end=' ')
    Grafo.verificar_fortemente_conexos()
    print("q7.", end=' ')
    Grafo.verificar_eureliano()
    print("q8.", end=' ')
    Grafo.imprime_caminho(a, b)
    print("q9.", end=' ')
    Grafo.encontrar_agm(random_vertices(Grafo))
    # Grafo.plotar()
    print()
