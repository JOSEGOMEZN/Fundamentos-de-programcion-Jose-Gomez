# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 32}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)
