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

grafo03 = {"SaoPaulo": {"Curitiba": 20, "PortoAlegre": 60},
           "Florianopolis": {"Curitiba": 30, "PortoAlegre": 45},
           "Curitiba": {"SaoPaulo": 20, "PortoAlegre": 50, "Florianopolis": 30},
           "PortoAlegre": {"SaoPaulo": 60, "Curitiba": 50, "Florianopolis": 45}
           }

grafo04 = {"x1": ["x2", "x4"],
           "x2": ["x1", "x3"],
           "x3": ["x2"],
           "x4": ["x1"],
           "x5": ["x6"],
           "x6": ["x5"]
           }

grafo05 = {"0": {"1": 6, "2": 1, "3": 5},
           "1": {"0": 6, "2": 2, "4": 5},
           "2": {"0": 1, "1": 2, "3": 2, "4": 6, "5": 4},
           "3": {"0": 5, "2": 2, "5": 4},
           "4": {"1": 5, "2": 6, "5": 3},
           "5": {"2": 4, "3": 4, "4": 3}
           }

grafo06 = {"a": {"b": 4, "h": 8},
           "b": {"a": 4, "c": 8, "h": 11},
           "c": {"b": 8, "d": 7, "f": 4, "i": 2},
           "d": {"c": 7, "e": 9, "f": 14},
           "e": {"d": 9, "f": 10},
           "f": {"c": 4, "d": 14, "e": 10, "g": 2},
           "g": {"f": 2, "h": 1, "i": 6},
           "h": {"a": 8, "b": 11, "g": 1, "i": 7},
           "i": {"c": 2, "g": 6, "h": 7}
           }
