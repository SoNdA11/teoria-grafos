import pygame
from dijkstra import dijkstra

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

node_positions = {
    1: (50, 50), 2: (150, 100), 3: (200, 200), 4: (300, 300), 5: (400, 400), 
    6: (350, 150), 7: (450, 250), 8: (500, 350), 9: (600, 450), 10: (650, 100),
    11: (700, 300), 12: (200, 400), 13: (300, 500), 14: (250, 250), 15: (500, 100),
    16: (100, 500), 17: (150, 300), 18: (350, 450), 19: (400, 100), 20: (550, 300),
    21: (450, 500), 22: (200, 600), 23: (600, 150), 24: (700, 500), 25: (800, 200),
    26: (400, 600), 27: (550, 450), 28: (600, 100), 29: (700, 350), 30: (750, 400),
    31: (800, 550), 32: (850, 150), 33: (900, 300), 34: (950, 450), 35: (1000, 600),
    36: (1050, 100), 37: (1100, 250), 38: (1150, 400), 39: (1200, 550), 40: (1250, 100)
}

def draw_graph(screen, graph, node_positions):
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            pygame.draw.line(screen, BLACK, node_positions[node], node_positions[neighbor], 1)
    for node, pos in node_positions.items():
        pygame.draw.circle(screen, RED, pos, 5)
        font = pygame.font.Font(None, 24)
        text = font.render(str(node), True, BLACK)
        screen.blit(text, pos)

def animate_dijkstra(screen, graph, start, end, line_thickness=2):
    distances, shortest_path = dijkstra(graph, start)
    path = []
    current = end
    while current in shortest_path:
        path.append(current)
        current = shortest_path[current]
    path.append(start)
    path = path[::-1]

    for i in range(len(path) - 1):
        pygame.draw.line(screen, BLUE, node_positions[path[i]], node_positions[path[i + 1]], line_thickness)
        pygame.display.flip()
        pygame.time.wait(500)
