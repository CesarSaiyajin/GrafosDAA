import random
import Grafo as gr
import Arista as ar

Malla = gr.Grafo()
Malla.Malla(filas = 5, columnas=10)
print(ar.Arista)


BFS = gr.Grafo()
BFS.BFS(grafo=ar.Arista, inicio=1_7)
#BFS.archivo_grafo('BFSMalla500')
print(BFS)