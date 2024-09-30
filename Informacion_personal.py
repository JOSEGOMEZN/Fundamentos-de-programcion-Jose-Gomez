# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Diego Lopez",
    "edad": 30,
    "ciudad": "Cuenca",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Riobamba"

# Agregar una nueva clave-valor para representar la "profesion"
informacion_personal["profesion"] = "Diseñador grafico"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0993891219"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)