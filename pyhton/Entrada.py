grafo01 = {"Maria": ["Pedro", "Joana"],
           "Joana": ["Maria", "Pedro"],
           "Pedro": ["Maria", "Joana", "Luiz"],
           "Luiz": ["Pedro"]
           }

grafo02 = {"Isadora": ["Emerson"],
           "Alfredo": ["Emerson", "Antônio"],
           "Cecília": ["Antônio"],
           "Emerson": [],
           "Antônio": ["Renata"],
           "Renata": []
           }

grafo03 = {"São Paulo": {"Curitiba": 20, "Porto Alegre": 60},
           "Florianópolis": {"Curitiba": 30, "Porto Alegre": 45},
           "Curitiba": {"São Paulo": 20, "Porto Alegre": 50, "Florianópolis": 30},
           "Porto Alegre": {"São Paulo": 60, "Curitiba": 50, "Florianópolis": 45}
           }

# grafo03 = {"São Paulo": [("Curitiba", 20), ("Porto Alegre", 60)],
#            "Florianópolis": [("Curitiba", 30), ("Porto Alegre", 45)],
#            "Curitiba": [("São Paulo", 20), ("Porto Alegre", 50), ("Florianópolis", 30)],
#            "Porto Alegre": [("São Paulo", 60), ("Curitiba", 50), ("Florianópolis", 45)]
#            }
#
grafo04 = {"x1": ["x2", "x4"],
           "x2": ["x1", "x3"],
           "x3": ["x2"],
           "x4": ["x1"],
           "x5": ["x6"],
           "x6": ["x5"]
           }
#
# grafo05 = {"a": ["c"],
#            "b": ["c"],
#            "c": ["a", "b", "d", "e"],
#            "d": ["c", "e"],
#            "e": ["c", "d"]
#            }
#
# grafo06 = {"a": {"a": 0, 'b': 1},
#            "b": {'c': 2},
#            "c": {'a': 3},
#            "d": {"a": 1, "c": 5}
#            }
#
# grafo07 = {"0": {"1": 1, "3": 3, "4": 10},
#            "1": {"2": 5},
#            "2": {"4": 1},
#            "3": {"2": 2, "4": 6},
#            "4": {}
#            }
#
# grafo08 = {"a": {"a": 0, "c": 1},
#            "b": {"c": 3},
#            "c": {"a": 1, "b": 3, "d": 2, "e": 4},
#            "d": {"c": 2, "e": 1},
#            "e": {"c": 4, "d": 1}
#            }
#
# grafo09 = {"1": {"2": 2, "5": 1, "6": 5},
#            "2": {"1": 2, "3": 3, "5": 7},
#            "3": {"2": 3, "4": 9, "5": 3},
#            "4": {"3": 9, "5": 4},
#            "5": {"1": 1, "2": 7, "3": 3, "4": 4, "6": 4},
#            "6": {"1": 5, "5": 4}
#            }
#
# grafo10 = {"a": {"b": 3, "c": 5, "d": 1},
#            "b": {"a": 3, "e": 4},
#            "c": {"a": 5, "d": 4, "e": 8},
#            "d": {"a": 1, "c": 4, "f": 3},
#            "e": {"b": 4, "c": 8, "f": 7},
#            "f": {"d": 3, "e": 7}
#            }
#
# grafo11 = {"A": {"B": 2, "D": 7, "O": 2},
#            "B": {"A": 2, "C": 1, "D": 4, "E": 3, "O": 5},
#            "C": {"B": 1, "E": 4, "O": 4},
#            "D": {"A": 7, "B": 4, "E": 1, "T": 5},
#            "E": {"B": 3, "C": 4, "D": 1, "T": 7},
#            "O": {"A": 2, "B": 5, "C": 4},
#            "T": {"D": 5, "E": 7}
#            }
#
# grafo12 = {"a": [("b", 4), ("c", 7), ("c", 4)],
#            "b": [("c", 5)],
#            "c": [("c", 0), ("b", 2)]
#            }
#
# grafo13 = {"M1": ["M3", "M4", "M6"],
#            "M2": ["M4", "M5", "M6"],
#            "M3": ["M1"],
#            "M4": ["M1", "M2"],
#            "M5": ["M2"],
#            "M6": ["M1", "M2"]
#            }
