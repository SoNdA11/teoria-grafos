import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def draw_graph(screen, graph, node_positions):
    screen.fill(BLACK)
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            pygame.draw.line(screen, WHITE, node_positions[node], node_positions[neighbor], 1)
    for node, pos in node_positions.items():
        pygame.draw.circle(screen, RED, pos, 25)
        font = pygame.font.Font(None, 24)
        text = font.render(str(node), True, BLACK)
        screen.blit(text, pos)

def animate_prim(screen, mst, node_positions, line_thickness=4):
    for edge in mst:
        pygame.draw.line(screen, GREEN, node_positions[edge[0]], node_positions[edge[1]], line_thickness)
        pygame.display.flip()
        pygame.time.wait(500)
