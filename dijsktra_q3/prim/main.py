import pygame
from graph import create_graph, node_positions
from prim import prim
from visualization import draw_graph, animate_prim, WHITE
import json

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Prim's Algorithm Visualization")
    screen.fill(WHITE)
    graph = create_graph()

    draw_graph(screen, graph, node_positions)
    pygame.display.flip()

    mst, total_weight = prim(graph, 1)

    print("Caminho da Árvore Geradora Mínima (MST):")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]} (Peso: {edge[2]})")
    print(f"Peso total das arestas na MST: {total_weight}")

    animate_prim(screen, mst, node_positions)

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
    pygame.quit()


def save_json_to_file(json_data, filename):
    with open(filename, 'w') as file:
        json.dump(json_data, file)
        
def json_to_dot(json_data, filename):
    with open(filename, 'w') as file:
        file.write("graph MST {\n")
        for edge in json_data:
            file.write(f"  {edge[0]} -- {edge[1]} [label=\"{edge[2]}\"];\n")
        file.write("}\n")

output_filename = "prim_functions.json"


# Obtenha os dados do MST (substitua isso pelos dados reais do seu MST)
prim_functions = [
    [12, 14, 70], [32, 33, 75], [2, 3, 105], [15, 19, 105], [16, 17, 110], 
    [38, 40, 110], [20, 23, 120], [3, 4, 130], [12, 13, 150], [23, 24, 150],
    [24, 26, 150], [29, 30, 150], [39, 40, 150], [21, 22, 160], [3, 6, 165],
    [6, 7, 165], [20, 21, 165], [17, 22, 170], [18, 20, 170], [26, 28, 175],
    [30, 31, 180], [35, 37, 180], [33, 36, 185], [22, 25, 190], [13, 15, 195],
    [14, 17, 195], [16, 10, 200], [11, 15, 210], [27, 31, 210], [1, 2, 220],
    [9, 15, 220], [7, 9, 225], [8, 11, 225], [28, 33, 230], [4, 5, 240],
    [24, 29, 255], [34, 36, 260], [36, 38, 260], [34, 35, 300]
]

# Salvar o JSON em um arquivo
save_json_to_file(prim_functions, output_filename)

print(f"O JSON foi salvo no arquivo: {output_filename}")

# Nome do arquivo DOT de saída
output_dot_filename = "prim_mst.dot"

# Converter o JSON em arquivo DOT
json_to_dot(prim_functions, output_dot_filename)

print(f"O arquivo DOT foi salvo em: {output_dot_filename}")



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        pygame.quit()
        input("Pressione Enter para sair...")
