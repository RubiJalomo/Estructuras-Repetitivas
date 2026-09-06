n = int(input("Ingrese un numero: "))

suma_pares = 0
suma_Impares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_Impares += i

        print (f"Suma de pares: {suma_pares}")
        print(f"Suma de impares: {suma_Impares} ")
        