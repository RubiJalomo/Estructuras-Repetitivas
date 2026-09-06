numero = int(input("Ingrese un numero entero: "))

signo = -1 if numero < 0 else 1 
numero = abs(numero)

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

    invertido = invertido * signo

    print(f"El numero invertido es {invertido}")
    