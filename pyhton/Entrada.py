grafo01 = {"a": ["c"],
           "b": ["c", "e"],
           "c": ["b", "d", "e"],
           "d": ["c", "e", "f"],
           "e": ["c", "b", "d", "f"],
           "f": ["e"]
           }

grafo02 = {"a": ["b", "c"],
           "b": ["c", "d"],
           "c": ["a", "b"],
           "d": ["b"]
           }

grafo03 = {"a": ["c"],
           "b": ["c", "e"],
           "c": [],
           "d": ["b", "e"],
           "e": ["f"],
           "f": []
           }

grafo04 = {"a": ["b", "d"],
           "b": ["a", "c"],
           "c": ["b", "d"],
           "d": ["a", "c"]
           }

grafo05 = {"a": ["c"],
           "b": ["c"],
           "c": ["a", "b", "d", "e"],
           "d": ["c", "e"],
           "e": ["c", "d"]
           }

grafo06 = {"a": [('b', 1)],
           "b": [('c', 2)],
           "c": [('a', 3)],
           "d": [("a", 1), ("c", 5)]
           }

grafo07 = {"0": [("1", 1), ("3", 3), ("4", 10)],
           "1": [("2", 5)],
           "2": [("4", 1)],
           "3": [("2", 2), ("4", 6)],
           "4": [()]
           }

grafo08 = {"a": [("c", 1)],
           "b": [("c", 3)],
           "c": [("a", 1), ("b", 3), ("d", 2), ("e", 4)],
           "d": [("c", 2), ("e", 1)],
           "e": [("c", 4), ("d", 1)]
           }

grafo09 = {"1": [("2", 2), ("5", 1), ("6", 5)],
           "2": [("1", 2), ("3", 3), ("5", 7)],
           "3": [("2", 3), ("4", 9), ("5", 3)],
           "4": [("3", 9), ("5", 4)],
           "5": [("1", 1), ("2", 7), ("3", 3), ("4", 4), ("6", 4)],
           "6": [("1", 5), ("5", 4)]
           }

grafo10 = {"a": [("b", 3), ("c", 5), ("d", 1)],
           "b": [("a", 3), ("e", 4)],
           "c": [("a", 5), ("d", 4), ("e", 8)],
           "d": [("a", 1), ("c", 4), ("f", 3)],
           "e": [("b", 4), ("c", 8), ("f", 7)],
           "f": [("d", 3), ("e", 7)]
           }

grafo11 = {"A": [("B", 2), ("D", 7), ("O", 2)],
           "B": [("A", 2), ("C", 1), ("D", 4), ("E", 3), ("O", 5)],
           "C": [("B", 1), ("E", 4), ("O", 4)],
           "D": [("A", 7), ("B", 4), ("E", 1), ("T", 5)],
           "E": [("B", 3), ("C", 4), ("D", 1), ("T", 7)],
           "O": [("A", 2), ("B", 5), ("C", 4)],
           "T": [("D", 5), ("E", 7)]
           }

grafo12 = {"a": [("b", 4), ("c", 7), ("c", 4)],
           "b": [("c", 5)],
           "c": [("c", 0), ("b", 2)]
           }
