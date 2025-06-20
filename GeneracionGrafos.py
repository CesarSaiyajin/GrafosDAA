import Grafo as gr
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
'''
grafo =gr.Grafo()
grafo.Malla(5,5)
visFR.Fruch_Reig(grafo)
'''

grafo =gr.Grafo()
grafo.Malla(20,20)
visBH.BarnesHut(grafo)
