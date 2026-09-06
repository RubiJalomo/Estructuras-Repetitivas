calificacion = float(input("Ingrese su calificacion (0-100): "))

if calificacion >= 90:
    print("Calificacion: A")
elif calificacion >= 80:
    print("Calificacion: B")
elif calificacion >= 70:
    print("Calificacion: C")
elif calificacion >= 60:
    print("Calificacion: D")
else:
    print("Calificacion: F")
