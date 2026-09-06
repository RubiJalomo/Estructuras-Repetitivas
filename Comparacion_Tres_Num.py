num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

if num1 > num2:
    mayor = num1
else:
    mayor = num2
if num3 > mayor:
    mayor = num3
if num1 < num2:
    menor = num1
else:
    menor = num2
if num3 < menor:
    menor = num3

print("El numero mayor es:", mayor)
print("El numero menor es:", menor)
