n = int(input("Ingrese la altura de la piramide: "))

for i in range(1, n + 1):
    espacios = " " * (n - 1)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)
    