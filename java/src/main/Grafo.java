package main;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Grafo {

    private Map<Vertice, List<Vertice>> verticesAdjacentes;

    public Grafo() {

    }

    public Grafo(final Map<Vertice, List<Vertice>> verticesAdjacentes) {

        super();
        this.verticesAdjacentes = verticesAdjacentes;
    }

    public Map<Vertice, List<Vertice>> getAdjVertices() {

        return this.verticesAdjacentes;
    }

    public void setAdjVertices(final Map<Vertice, List<Vertice>> verticesAdjacentes) {

        this.verticesAdjacentes = verticesAdjacentes;
    }

    public void addVertice(final String label) {

        this.verticesAdjacentes.putIfAbsent(new Vertice(label), new ArrayList<>());
    }

    public void removeVertice(final String label) {

        final Vertice vertice = new Vertice(label);
        this.verticesAdjacentes.values()
                        .stream()
                        .map(e -> e.remove(vertice))
                        .collect(Collectors.toList());
        this.verticesAdjacentes.remove(new Vertice(label));
    }

    public void addAresta(final String label1, final String label2) {

        final Vertice vertice1 = new Vertice(label1);
        final Vertice vertice2 = new Vertice(label2);
        this.verticesAdjacentes.get(vertice1).add(vertice2);
        this.verticesAdjacentes.get(vertice2).add(vertice1);
    }
}
