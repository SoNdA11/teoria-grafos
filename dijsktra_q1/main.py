import pygame
import sys
import json
from graph import create_graph
from visualization import draw_graph, animate_dijkstra, node_positions, WHITE
from dijkstra import dijkstra

# Dicionário para mapear os vértices para os nomes das cidades
vertex_to_city = {
    1: 'CHICAGO', 2: 'PEORIA', 3: 'SPRINGFIELD, ILLINOIS', 4: 'ST LOUIS', 
    5: 'POPLAR BLUFF', 6: 'HANNIBAL', 7: 'JEFFERSON CITY', 8: 'LITTLE ROCK', 
    9: 'SPRINGFIELD, MISSOURI', 10: 'DES MOINES', 11: 'FT. SMITH', 
    12: 'KANSAS CITY', 13: 'FT SCOTT', 14: 'ST JOSEPH',15: 'TULSA', 16: 'OMAHA', 
    17: 'BEATRICE', 18: 'WICHITA', 19: 'OKLAHOMA', 20: 'GREAT BEND', 
    21: 'PHILLIPSBURG', 22: 'GRAND ISLAND', 23: 'DOGDE CITY', 24: 'GUYMON', 
    25: 'NORTH PLATTE', 26: 'AMARILLO', 27: 'KIT CARSON', 28: 'TUCUMCARI', 
    29: 'RATON', 30: 'PUEBLO', 31: 'DENVER', 32: 'SANTA FE', 33: 'ALBUQUERQUE', 
    34: 'DURANGO', 35: 'GRAND JUNCTION', 36: 'GALLUP', 37: 'GREEN RIVER', 
    38: 'FLAGSTAFF', 39: 'MT. CARMEL JUNCTION', 40: 'GRAND CANYON'
}

def convert_path_to_cities(path):
    return [vertex_to_city[vertex] for vertex in path]

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((1300, 800))
    pygame.display.set_caption('Dijkstra Visualization')

    graph = create_graph()

    # Executa o algoritmo de Dijkstra para encontrar o caminho mais curto
    start = 1
    end = 40
    distances, shortest_path = dijkstra(graph, start)

    # Reconstroi o caminho mais curto do start ao end
    path = []
    current = end
    while current in shortest_path:
        path.append(current)
        current = shortest_path[current]
    path.append(start)
    path = path[::-1]


    # Converte o caminho de vértices para nomes de cidades
    city_path = convert_path_to_cities(path)


    # Calcula a soma total dos pesos das arestas do caminho mais curto
    total_weight = sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))

    # Imprime o caminho mais curto e o peso total no terminal
    print(f"Caminho mais curto do vértice {start} ao vértice {end}: {city_path}")

    print(f"Caminho mais curto do vértice {start} ao vértice {end}: {path}")

    print(f"Soma total dos pesos das arestas: {total_weight}")

    # Salva o caminho e o peso total em um arquivo JSON
    with open('shortest_path.json', 'w') as f:
        json.dump({'path': path, 'total_weight': total_weight}, f)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_graph(screen, graph, node_positions)
        animate_dijkstra(screen, graph, start, end, line_thickness=4)  # Espessura da linha ajustada

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
