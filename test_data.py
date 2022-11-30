IS_PALINDROME_DATA = [
    ("oko", True),
    ("tramwaj", False),
    ("sedes", True),
    ("Radar", True),
    ("Parapet", False),
    ("Jem sód od ósmej", True),
    ("Mamuta tu mam", True),
    ("Może jutro ta dama da tortu jeżom", True),
    ("Nie ma dowodu że wiedział", False),
]


MY_SPLIT_DATA = [
    ("text", ["text"]),
    ("   text   ", ["text"]),
    ("hobbit ma", ["hobbit", "ma"]),
    ("hobbit ma kota", ["hobbit", "ma", "kota"]),
    ("hobbit    ma    kota", ["hobbit", "ma", "kota"]),
    ("    hobbit    ma    kota   ", ["hobbit", "ma", "kota"]),
]


MIN_MAX_DATA = [
    ([1], (1, 1)),
    ([1, 1], (1, 1)),
    ([1, 2, 3], (1, 3)),
    ([1, -1, 2], (-1, 2)),
    ([2, 1, 3, 7], (1, 7)),
    ([-2, 1, 3, -7, 15, -10, 0, 0, 0, 15, -2], (-10, 15)),
]


BORDER_MAP_DATA = [
    (1, 1, [['X']]),
    (1, 2, [['X'], ['X']]),
    (2, 2, [['X', 'X'], ['X', 'X']]),
    (3, 3, [['X', 'X', 'X'], ['X', '.', 'X'], ['X', 'X', 'X']]),
    (3, 4, [['X', 'X', 'X'], ['X', '.', 'X'], ['X', '.', 'X'], ['X', 'X', 'X']]),
    (6, 9, [['X', 'X', 'X', 'X', 'X', 'X'], ['X', '.', '.', '.', '.', 'X'], ['X', '.', '.', '.', '.', 'X'], ['X', '.', '.', '.', '.', 'X'], ['X', '.', '.', '.', '.', 'X'], ['X', '.', '.', '.', '.', 'X'], ['X', '.', '.', '.', '.', 'X'], ['X', '.', '.', '.', '.', 'X'], ['X', 'X', 'X', 'X', 'X', 'X']]),
]
