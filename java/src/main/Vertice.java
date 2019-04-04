package main;

import java.util.Objects;

public class Vertice {

    String label;

    public Vertice(final String label) {

        this.label = label;
    }

    @Override
    public int hashCode() {

        return Objects.hash(this.label);
    }

    @Override
    public boolean equals(final Object obj) {

        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (!(obj instanceof Vertice)) {
            return false;
        }
        final Vertice other = (Vertice) obj;
        return Objects.equals(this.label, other.label);
    }

}
