from math import log, atan2, cos, sin
import pygame
import random

WIDTH, HEIGHT   = 1020, 720
BORDER          = 15
WIN             = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
BG              = (251, 241, 199)
BLUE            = (69, 133, 136)
BLACK           = (40, 40, 40)
RED             = (157, 0, 6)

# colors black mode
BG              = (40, 40, 40)
BLUE            = (131, 165, 152)
BLACK           = (235, 219, 178) # Actually white
RED             = (251, 73, 52)

# configuration
ITERS           = 1000
FPS             = 40
NODE_RADIUS     = 5
DIST_MIN        = (min(WIDTH, HEIGHT)) // 20
NODE_MIN_WIDTH  = 5
NODE_MIN_HEIGHT = 5
NODE_MAX_WIDTH  = WIDTH - 10
NODE_MAX_HEIGHT = HEIGHT - 10

# spring constants
c1 = 1.65
c2 = 0.7
c3 = 4.8
c4 = 0.1

def fruchterman_reginold(g):
    """
        Muestra una animación del metodo de visualizacion de Furchterman y Reginold
        Parametros
        ----------
        g : Grafo
            grafo para el cual se realiza la visualizacion
    """
    run = True
    clock = pygame.time.Clock()

    init_nodes(g)
    draw_edges(g)
    draw_nodes(g)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(BG)
        update_nodes(g)
        draw_edges(g)
        draw_nodes(g)
        pygame.display.update()

    pygame.quit()
    return


def init_nodes(g):
    """
    Inicializa los nodos del grafo g en posiciones random

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for node in g.obtener_nodos():
        x = random.randrange(NODE_MIN_WIDTH, NODE_MAX_WIDTH)
        y = random.randrange(NODE_MIN_HEIGHT, NODE_MAX_HEIGHT)
        node.attrs['coords'] = [x, y]

    return


def update_nodes(g):
    """
    Actualiza las posiciones de los nodos usando el algoritmo de Fruchterman-Reingold
    con enfriamiento y convergencia básica.
    """
    C = 1
    area = (WIDTH - NODE_MIN_WIDTH) * (HEIGHT - NODE_MIN_HEIGHT)
    k = C * (area / len(g.obtener_nodos())) ** 0.5
    t = 0.95  # factor de enfriamiento
    advance = 20
    conv_threshold = max(3.0, len(g.obtener_nodos()) / 100)
    converged = False
    energy = 0

    # Inicializar desplazamientos
    disp = {node: [0.0, 0.0] for node in g.obtener_nodos()}

    # Fuerza de repulsión
    for v in g.obtener_nodos():
        for u in g.obtener_nodos():
            if v != u:
                dx = v.attrs['coords'][0] - u.attrs['coords'][0]
                dy = v.attrs['coords'][1] - u.attrs['coords'][1]
                dist = (dx ** 2 + dy ** 2) ** 0.5 or 0.01
                force = k ** 2 / dist
                disp[v][0] += (dx / dist) * force
                disp[v][1] += (dy / dist) * force

    # Fuerza de atracción
    for v in g.obtener_nodos():
        for u_valor in v.obtener_vecinos():
            u = next((n for n in g.obtener_nodos() if n.valor == u_valor), None)
            if u is None:
                continue  # o maneja el caso apropiadamente
            dx = v.attrs['coords'][0] - u.attrs['coords'][0]
            dy = v.attrs['coords'][1] - u.attrs['coords'][1]
            dist = (dx ** 2 + dy ** 2) ** 0.5 or 0.01
            force = dist ** 2 / k
            disp[v][0] -= (dx / dist) * force
            disp[v][1] -= (dy / dist) * force

    # Actualizar posiciones
    for v in g.obtener_nodos():
        dx, dy = disp[v]
        disp_mag = (dx ** 2 + dy ** 2) ** 0.5 or 0.01
        # Limitar el desplazamiento por el factor de enfriamiento
        v.attrs['coords'][0] += (dx / disp_mag) * min(advance, disp_mag)
        v.attrs['coords'][1] += (dy / disp_mag) * min(advance, disp_mag)
        # Restringir a los límites de la ventana
        v.attrs['coords'][0] = min(max(v.attrs['coords'][0], NODE_MIN_WIDTH), NODE_MAX_WIDTH)
        v.attrs['coords'][1] = min(max(v.attrs['coords'][1], NODE_MIN_HEIGHT), NODE_MAX_HEIGHT)
        energy += disp_mag ** 2

    # Enfriamiento (advance disminuye)
    advance = t * advance
    if advance < conv_threshold:
        converged = True

    return converged


def draw_nodes(g):
    """
    Dibuja los nodos del grafo g

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for node in g.obtener_nodos():
        pygame.draw.circle(WIN, BLUE, node.attrs['coords'], NODE_RADIUS - 3, 0)
        pygame.draw.circle(WIN, RED, node.attrs['coords'], NODE_RADIUS, 3)

    return


def draw_edges(g):
    """
    Dibuja las aristas del grafo g

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for edge in g.obtener_aristas():
        u, v = edge.obtener_nodos()
        u_pos = u.attrs['coords']
        v_pos = v.attrs['coords']

        pygame.draw.line(WIN, BLACK, u_pos, v_pos, 1)

    return