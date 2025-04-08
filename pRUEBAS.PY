import random

a=random.random()
print(a)

    
    # Crear las aristas para formar un triángulo entre los 3 nodos
for i in range(3):  # Los 3 nodos (0, 1, 2)
    for j in range (i+1,3):  # Conectar los nodos entre sí
        print(i, j)

Nodo=[0,1,2]

for i in range(len(Nodo)):
    if i < 2:  # Si el nodo actual es menor que 2
        print(Nodo[i], Nodo[i+1])  # Conectar el nodo con el siguiente
    else:
        print(Nodo[i], Nodo[0])
        
for i in range (1,4):
    print(i)
    
a=[(0,1),(1,2)]
b=random.choice(a)
print (b)
print(b[1])
print('holas')