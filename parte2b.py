cant1=0
cant2=0
cant3=0
cant4=0
n=int(input("Cantidad de puntos:"))
for f in range(n):
    x=int(input("Ingrese coordenada x:"))
    y=int(input("Ingrese coordenada y:"))
    if x>0 and y>0:
        cant1=cant1+1 
    elif x<0 and y>0:
        cant2=cant2+1 
    elif x<0 and y < 0:
        cant3=cant3+1 
    elif x>0 and y < 0:
        cant4=cant4+1 
print(f"Hay {cant1} puntos en el primer cuadrante")
print(f"Hay {cant2} puntos en el segundo cuadrante")
print(f"Hay {cant3} puntos en el tercer cuadrante")
print(f"Hay {cant4} puntos en el cuarto cuadrante")