def temperatura_promedio(ciudades_temperaturas):
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio

ciudades_temperaturas = {
    "Quito": [23,23,24,25,26],
    "Guayaquil": [28,29,30,30,31],
    "Cuenca": [18,19,20,22,23]
}

temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

print("Temperaturas Promedio por Ciudad")
for ciudad, promedio in temperaturas_promedio.items() :
    print(f"{ciudad} : {promedio: .2f} ºC")
