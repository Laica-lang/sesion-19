#Parte 3

calificaciones={"Maria":3.0,"Jose":5.0,"Andres":3.5}

nombre_max = max(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación de {calificaciones[nombre_max]}.")
