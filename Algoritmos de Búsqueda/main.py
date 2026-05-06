import time


def leer_archivo():
    with open("datos.txt", "r") as archivo:
        numeros = archivo.read().split()

    return [int(num) for num in numeros]


def menu_orden():
    while True:
        print("\n ")
        print(" ORDENAMIENTO Y BÚSQUEDA SECUENCIAL")
        print(" ")

        print("Seleccione el tipo de orden:")
        print("1. Ascendente")
        print("2. Descendente")

        opcion = input("\nIngrese una opción 1 o 2: ").strip()

        if opcion == "1":
            return "ascendente"
        elif opcion == "2":
            return "descendente"
        else:
            print("\nError: opción inválida, intenta de nuevo.\n")


def menu_busqueda():
    while True:
        entrada = input("\nIngrese el número a buscar: ").strip()

        if entrada.lstrip("-").isdigit():
            return int(entrada)
        else:
            print("Error: ingresa un número válido.")



def dividir_corridas(lista):
    corridas = []
    corrida_actual = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i] >= lista[i - 1]:
            corrida_actual.append(lista[i])
        else:
            corridas.append(corrida_actual)
            corrida_actual = [lista[i]]

    corridas.append(corrida_actual)
    return corridas


def mezclar(lista1, lista2):
    resultado = []
    i = j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado


def mezcla_natural(lista):
    while True:
        corridas = dividir_corridas(lista)

        if len(corridas) == 1:
            break

        nueva_lista = []

        for i in range(0, len(corridas), 2):
            if i + 1 < len(corridas):
                nueva_lista.extend(mezclar(corridas[i], corridas[i + 1]))
            else:
                nueva_lista.extend(corridas[i])

        lista = nueva_lista

    return lista



def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def guardar_resultado(lista, tiempo, tipo_orden):
    with open("numeros_ordenados.txt", "w") as archivo:
        archivo.write("NUMEROS ORDENADOS\n")
    

        for numero in lista:
            archivo.write(f"{numero}\n")



numeros = leer_archivo()
print(f"\nSe cargaron {len(numeros)} números correctamente.")

tipo_orden = menu_orden()


inicio_orden = time.time()

numeros_ordenados = mezcla_natural(numeros)

if tipo_orden == "descendente":
    numeros_ordenados.reverse()

fin_orden = time.time()

tiempo_orden = (fin_orden - inicio_orden) * 1000

print(f"\nOrdenamiento completado ({tipo_orden}).")
print(f"Tiempo de ordenamiento: {tiempo_orden:.2f} ms")



guardar_resultado(numeros_ordenados, tiempo_orden, tipo_orden)
print("Archivo generado: resultado_ordenado.txt")


numero_buscar = menu_busqueda()

inicio_busqueda = time.time()

posicion = busqueda_secuencial(numeros_ordenados, numero_buscar)

fin_busqueda = time.time()

tiempo_busqueda = (fin_busqueda - inicio_busqueda) * 1000

print("\n RESULTADOS: ")

if posicion != -1:
    print(f"Número encontrado en la posición: {posicion}")
else:
    print("El número no se encuentra en la lista.")

print(f"Tiempo de búsqueda: {tiempo_busqueda:.6f} ms")