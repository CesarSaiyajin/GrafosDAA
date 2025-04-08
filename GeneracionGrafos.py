import Grafo as gr

#ErdosRenyi = gr.Grafo()
#ErdosRenyi.ErdosRenyi(Nodos=30,Aristas=90)
#ErdosRenyi.archivo_grafo('ErdosRenyi30')
#print(ErdosRenyi)

#Gilbert = gr.Grafo()
#Gilbert.Gilbert(Nodos = 30, proba = .25)
#Gilbert.archivo_grafo('Gilbert30')
#print(Gilbert)

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 200, distancia_max = 25)
GeoSimple.archivo_grafo('GeoSimple30')
#print(GeoSimple)

BarabasiAlbert = gr.Grafo()
BarabasiAlbert.BarabasiAlbert(Nodos = 100, Conexiones = 14)
BarabasiAlbert.archivo_grafo('BarabasiAlbert30')
#print(BarabasiAlbert)

BarabasiAlbertInverso = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso(Nodos = 100, Conexiones = 14)
BarabasiAlbertInverso.archivo_grafo('BarabasiAlbertInverso30')
#print(BarabasiAlbertInverso)

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 100)
DorogovtsevMendes.archivo_grafo('DorogovtsevMendes30')
print(DorogovtsevMendes)