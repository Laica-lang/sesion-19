n = int(input("Ingrese la cantidad de estudiantes: "))
calificaciones = {}
for _ in range(n):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    calificaciones[nombre] = nota
print(f"Estudiantes: {calificaciones}")
