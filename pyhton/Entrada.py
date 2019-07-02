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

grafo04 = {"x1": ["x2", "x4"],
           "x2": ["x1", "x3"],
           "x3": ["x2"],
           "x4": ["x1"],
           "x5": ["x6"],
           "x6": ["x5"]
           }
