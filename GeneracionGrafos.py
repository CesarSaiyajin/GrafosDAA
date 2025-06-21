import Grafo as gr
import Visualizar as vis
import Fruchterman_Reigold as visFR
import BarnesHut as visBH
'''
grafo = gr.Grafo()
grafo.ErdosRenyi(100, 300)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.ErdosRenyi(500,700)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Gilbert(100,.5)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Gilbert(500,.25)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.GeoSimple(100,15)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.GeoSimple(500,25)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.BarabasiAlbertInverso(100,10)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.BarabasiAlbertInverso(500,20)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.DorogovtsevMendes(100)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.DorogovtsevMendes(500)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Malla(10,10)
vis.spring(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Malla(25,20)
vis.spring(grafo)
'''
# Fruchterman-Reingold algorithm visualization
'''
grafo = gr.Grafo()
grafo.ErdosRenyi(100, 300)
visFR.Fruch_Reig(grafo)
'''
'''
grafo =gr.Grafo()
grafo.ErdosRenyi(500,700)
visFR.Fruch_Reig(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Gilbert(100,.5)
visFR.Fruch_Reig(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Gilbert(500,.25)
visFR.Fruch_Reig(grafo)
'''
'''
grafo =gr.Grafo()
grafo.GeoSimple(100,15)
visFR.Fruch_Reig(grafo)
'''
'''
grafo =gr.Grafo()
grafo.GeoSimple(500,35)
visFR.Fruch_Reig(grafo)
'''
'''
grafo =gr.Grafo()
grafo.BarabasiAlbertInverso(100,10)
visFR.Fruch_Reig(grafo)
'''
'''
grafo =gr.Grafo()
grafo.BarabasiAlbertInverso(500,20)
visFR.Fruch_Reig(grafo)
'''
'''  
grafo =gr.Grafo()
grafo.DorogovtsevMendes(100)
visFR.Fruch_Reig(grafo)
'''
'''
grafo =gr.Grafo()
grafo.DorogovtsevMendes(500)
visFR.Fruch_Reig(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Malla(10,10)
visFR.Fruch_Reig(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Malla(25,25)
visFR.Fruch_Reig(grafo)
'''
# Barnes-Hut algorithm visualization
'''
grafo = gr.Grafo()
grafo.ErdosRenyi(100, 300)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.ErdosRenyi(500,700)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Gilbert(100,.5)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Gilbert(500,.25)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.GeoSimple(100,15)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.GeoSimple(500,35)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.BarabasiAlbertInverso(100,10)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.BarabasiAlbertInverso(500,20)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.DorogovtsevMendes(100)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.DorogovtsevMendes(500)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Malla(10,10)
visBH.BarnesHut(grafo)
'''
grafo =gr.Grafo()
grafo.Malla(25,25)
visBH.BarnesHut(grafo)
'''
ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=500,Aristas=1000)
#ErdosRenyi.archivo_grafo('ErdosRenyi500')
arbol,_=ErdosRenyi.BFS(0)
arbol2=ErdosRenyi.DFS_R(0)
arbol3=ErdosRenyi.DFS_I(0)
visBH.BarnesHut(arbol)
'''