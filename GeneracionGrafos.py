import Grafo as gr

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=50,Aristas=100)
Camino_corto=ErdosRenyi.KruskalD()
Camino_corto.archivo_grafo('KruskalDErdosRenyi_50_100')

Camino_corto2=ErdosRenyi.KruskalI()
Camino_corto2.archivo_grafo('KruskalIErdosRenyi_50_100')

Camino_corto3=ErdosRenyi.Prim(0)
Camino_corto3.archivo_grafo('PrimErdosRenyi_50_100')

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=200,Aristas=400)
Camino_corto=ErdosRenyi.KruskalD()
Camino_corto.archivo_grafo('KruskalDErdosRenyi_200_400')

Camino_corto2=ErdosRenyi.KruskalI()
Camino_corto2.archivo_grafo('KruskalIErdosRenyi_200_400')

Camino_corto3=ErdosRenyi.Prim(0)
Camino_corto3.archivo_grafo('PrimErdosRenyi_200_400')

"""
ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=200,Aristas=300)
Camino_corto,distancias, inicio=ErdosRenyi.Dijkstra(100)
Camino_corto.archivo_grafo_Dijkstra('DijkstraErdosRenyi_200_100', distancias, inicio)

Gilbert = gr.Grafo()
Gilbert.Gilbert(Nodos = 50, proba = .25)
Camino_corto,distancias, inicio=Gilbert.Dijkstra(10)
Camino_corto.archivo_grafo_Dijkstra('DijkstraGilbert_50_10', distancias, inicio)
#Gilbert.archivo_grafo('Gilbert50')
#print(Gilbert)

Gilbert = gr.Grafo()
Gilbert.Gilbert(Nodos = 200, proba = .25)
Camino_corto,distancias, inicio=Gilbert.Dijkstra(100)
Camino_corto.archivo_grafo_Dijkstra('DijkstraGilbert_200_100', distancias, inicio)

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 50, distancia_max = 15)
Camino_corto,distancias, inicio=GeoSimple.Dijkstra(10)
Camino_corto.archivo_grafo_Dijkstra('DijkstraGeoSimple_50_10', distancias, inicio)

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 200, distancia_max = 25)
Camino_corto,distancias, inicio=GeoSimple.Dijkstra(100)
Camino_corto.archivo_grafo_Dijkstra('DijkstraGeoSimple_200_100', distancias, inicio)

BarabasiAlbertInverso  = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso (Nodos = 50, Conexiones = 10)
Camino_corto,distancias, inicio=BarabasiAlbertInverso .Dijkstra(10)
Camino_corto.archivo_grafo_Dijkstra('DijkstraBarabasiAlbertInverso_50_10', distancias, inicio)

BarabasiAlbertInverso  = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso (Nodos = 200, Conexiones = 20)
Camino_corto,distancias, inicio=BarabasiAlbertInverso .Dijkstra(100)
Camino_corto.archivo_grafo_Dijkstra('DijkstraBarabasiAlbertInverso_200_100', distancias, inicio)

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 50)
Camino_corto,distancias, inicio=DorogovtsevMendes.Dijkstra('10|0')
Camino_corto.archivo_grafo_Dijkstra('DijkstraDorogovtsevMendes_50_10', distancias, inicio)

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 200)
Camino_corto,distancias, inicio=DorogovtsevMendes.Dijkstra("10|0")
Camino_corto.archivo_grafo_Dijkstra('DijkstraDorogovtsevMendes_200_100', distancias, inicio)

Malla = gr.Grafo()
Malla.Malla(filas = 5, columnas=10)
Camino_corto,distancias, inicio=Malla.Dijkstra('0_0')
Camino_corto.archivo_grafo_Dijkstra('DijkstraMalla_50_10', distancias, inicio)

Malla = gr.Grafo()
Malla.Malla(filas = 20, columnas=10)
Camino_corto,distancias, inicio=Malla.Dijkstra('0_0')
Camino_corto.archivo_grafo_Dijkstra('DijkstraMalla_200_100', distancias, inicio)


ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=50,Aristas=100)
#ErdosRenyi.archivo_grafo('ErdosRenyi50')
arbol=ErdosRenyi.BFS(0)
arbol2=ErdosRenyi.DFS_R(0)
arbol3=ErdosRenyi.DFS_I(0)
arbol.archivo_grafo('BFS_ErdosRenyi50')
arbol2.archivo_grafo('DFS_R_ErdosRenyi50')
arbol3.archivo_grafo('DFS_I_ErdosRenyi50')


ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=200,Aristas=400)
#ErdosRenyi.archivo_grafo('ErdosRenyi200')
arbol=ErdosRenyi.BFS(0)
arbol2=ErdosRenyi.DFS_R(0)
arbol3=ErdosRenyi.DFS_I(0)
arbol.archivo_grafo('BFS_ErdosRenyi200')
arbol2.archivo_grafo('DFS_R_ErdosRenyi200')
arbol3.archivo_grafo('DFS_I_ErdosRenyi200')

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=500,Aristas=1000)
#ErdosRenyi.archivo_grafo('ErdosRenyi500')
arbol=ErdosRenyi.BFS(0)
arbol2=ErdosRenyi.DFS_R(0)
arbol3=ErdosRenyi.DFS_I(0)
arbol.archivo_grafo('BFS_ErdosRenyi500')
arbol2.archivo_grafo('DFS_R_ErdosRenyi500')
arbol3.archivo_grafo('DFS_I_ErdosRenyi500')

Malla = gr.Grafo()
Malla.Malla(filas = 50, columnas=10)
Malla.archivo_grafo('Malla500')
arbol=Malla.BFS('0_0')
arbol2=Malla.DFS_R('0_0')
arbol3=Malla.DFS_I('0_0')
arbol.archivo_grafo('BFS_Malla500')
arbol2.archivo_grafo('DFS_R_Malla500')
arbol3.archivo_grafo('DFS_I_Malla500')

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 500)
DorogovtsevMendes.archivo_grafo('DorogovtsevMendes500')
arbol=DorogovtsevMendes.BFS('0|0')
arbol2=DorogovtsevMendes.DFS_R('0|0')
arbol3=DorogovtsevMendes.DFS_I('0|0')
arbol.archivo_grafo('BFS_DorogovtsevMendes500')
arbol2.archivo_grafo('DFS_R_DorogovtsevMendes500')
arbol3.archivo_grafo('DFS_I_DorogovtsevMendes500')
"""

#GeoSimple = gr.Grafo()
#GeoSimple.GeoSimple(Nodos = 50, distancia_max = 15)
#GeoSimple.archivo_grafo('GeoSimple50')
#print(GeoSimple)

#GeoSimple = gr.Grafo()
#GeoSimple.GeoSimple(Nodos = 200, distancia_max = 25)
#GeoSimple.archivo_grafo('GeoSimple200')

#GeoSimple = gr.Grafo()
#GeoSimple.GeoSimple(Nodos = 500, distancia_max = 50)
#GeoSimple.archivo_grafo('GeoSimple500')

#BarabasiAlbert = gr.Grafo()
#BarabasiAlbert.BarabasiAlbert(Nodos = 50, Conexiones = 10)
#BarabasiAlbert.archivo_grafo('BarabasiAlbert30')
#print(BarabasiAlbert)

#BarabasiAlbertInverso = gr.Grafo()
#BarabasiAlbertInverso.BarabasiAlbertInverso(Nodos = 50, Conexiones = 10)
#BarabasiAlbertInverso.archivo_grafo('BarabasiAlbertInverso50')
#print(BarabasiAlbertInverso)

#BarabasiAlbertInverso = gr.Grafo()
#BarabasiAlbertInverso.BarabasiAlbertInverso(Nodos = 200, Conexiones = 20)
#BarabasiAlbertInverso.archivo_grafo('BarabasiAlbertInverso200')

#BarabasiAlbertInverso = gr.Grafo()
#BarabasiAlbertInverso.BarabasiAlbertInverso(Nodos = 500, Conexiones = 10)
#BarabasiAlbertInverso.archivo_grafo('BarabasiAlbertInverso500')

#DorogovtsevMendes = gr.Grafo()
#DorogovtsevMendes.DorogovtsevMendes(Nodos = 50)
#DorogovtsevMendes.archivo_grafo('DorogovtsevMendes50')
#print(DorogovtsevMendes)

#DorogovtsevMendes = gr.Grafo()
#DorogovtsevMendes.DorogovtsevMendes(Nodos = 200)
#DorogovtsevMendes.archivo_grafo('DorogovtsevMendes200')

#DorogovtsevMendes = gr.Grafo()
#DorogovtsevMendes.DorogovtsevMendes(Nodos = 500)
#DorogovtsevMendes.archivo_grafo('DorogovtsevMendes500')

#Malla = gr.Grafo()
#Malla.Malla(filas = 5, columnas=10)
#Malla.archivo_grafo('Malla50')
#print(Malla)

#Malla = gr.Grafo()
#Malla.Malla(filas = 20, columnas=10)
#Malla.archivo_grafo('Malla200')

#Malla = gr.Grafo()
#Malla.Malla(filas = 50, columnas=10)
#Malla.archivo_grafo('Malla500')

#print("Árbol BFS:", arbol_bfs)
#print("Nodos visitados:", visitados)

