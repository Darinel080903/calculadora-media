import statistics
from collections import Counter

def main():

    numeros = []

    while True:
        print("======================")
        print("---------Menu---------")
        print("1. Agregar número")
        print("2. Calcular la media")
        print("3. Calcular la mediana")
        print("4. Calcular la moda")
        print("5. Calcular la frecuencia")
        print("6. Guardar el archivo")
        print("7. Salir")
        print("======================")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            numero = float(input("Ingrese un número: "))
            numeros.append(numero)
            print("Número agregado")
        elif opcion == 2:
            media = statistics.mean(numeros)
            print("La media es:", media)
        elif opcion == 3:
            mediana = statistics.median(numeros)
            print("La mediana es:", mediana)
        elif opcion == 4:
            moda = statistics.mode(numeros)
            print("La moda es:", moda)
        elif opcion == 5:
            frecuencia = Counter(numeros)
            print("Frecuencia:")
            for numero, cantidad in frecuencia.items():
                print(numero, ":", cantidad)
        elif opcion == 6:
            with open("resultados.txt", "w") as archivo:
                archivo.write("=================================" + "\n")
                archivo.write("--Los resultados guardados son--"  + "\n")
                archivo.write("la media es: " + str(media) + "\n")
                archivo.write("la mediana es: " + str(mediana) + "\n")
                archivo.write("la moda es: " + str(moda) + "\n")
                archivo.write("la moda es: " + str(frecuencia) + "\n")
                archivo.write("=================================")
            print("Datos guardados en el archivo resultados.txt")
        elif opcion == 7:
            break
        else:
            print("Opción inválida")
main()