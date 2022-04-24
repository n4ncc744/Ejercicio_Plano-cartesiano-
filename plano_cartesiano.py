"""Ejercicio del plano cartesiano"""

print("-----------------------------------")
print("----Coordenadas, ejes,origen-------")
print("-----------------------------------")

#input
X = int(input("Digite el valor de x: "))
Y = int(input("Digite el valor de y: "))

#processing

if X > 0 and Y > 0:
    msj = ("Esta en el primer cuadrante")
elif X < 0 and  Y  < 0:
    msj = ("Esta en el segundo cuadrante")
elif X < 0 and Y > 0:
    msj = ("Esta en el  cuadrante")
elif X > 0 and Y < 0: 
    msj = ("Esta en el cuarto cuadrante")
elif X == 0 and Y != 0:
    msj = ("se encuentra en el eje Y")
elif X != 0 and Y == 0:
    msj = ("se encuentra en el eje X")
else:
    msj = ("esta en el origen")

# output 

print("\nLa coordenada " + msj + "\n ")
