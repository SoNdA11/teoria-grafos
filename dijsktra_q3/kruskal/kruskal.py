def get_all_edges(graph):
    # Inicializa uma lista vazia para armazenar todas as arestas do grafo
    edges = []
    
    # Itera sobre cada nó do grafo
    for node, neighbors in graph.items():
        # Para cada vizinho do nó atual, adiciona uma tupla à lista de arestas
        # A tupla contém o peso da aresta, o nó atual e o vizinho
        for neighbor, weight in neighbors.items():
            edges.append((weight, node, neighbor))
    
    # Retorna a lista de todas as arestas do grafo
    return edges

def find_set(parent, i):
    # Função auxiliar para encontrar o representante do conjunto ao qual o nó i pertence
    if parent[i] == i:
        return i
    # Realiza a compressão de caminho enquanto encontra o representante do conjunto
    return find_set(parent, parent[i])

def union(parent, rank, x, y):
    # Função auxiliar para unir os conjuntos que contêm os nós x e y
    x_root = find_set(parent, x)
    y_root = find_set(parent, y)

    # Compara as alturas (ranks) dos conjuntos
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        # Se os ranks forem iguais, escolhe um nó como raiz e incrementa seu rank
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(graph):
    # Implementa o algoritmo de Kruskal para encontrar a Árvore Geradora Mínima (MST) do grafo
    
    # Obtém todas as arestas do grafo e as ordena por peso
    edges = get_all_edges(graph)
    edges.sort()
    
    # Inicializa a lista para armazenar as arestas da MST
    mst = []
    
    # Inicializa os dicionários para a estrutura de conjuntos disjuntos
    parent = {}
    rank = {}
    
    # Inicializa o peso total da MST
    total_weight = 0

    # Para cada nó do grafo, inicializa o nó como seu próprio representante
    for node in graph.keys():
        parent[node] = node
        rank[node] = 0

    # Itera sobre cada aresta do grafo
    for edge in edges:
        weight, u, v = edge
        
        # Verifica se adicionar a aresta não forma um ciclo na MST
        if find_set(parent, u) != find_set(parent, v):
            # Se não forma ciclo, adiciona a aresta à MST
            mst.append((u, v, weight))
            # Une os conjuntos dos nós u e v na estrutura de conjuntos disjuntos
            union(parent, rank, u, v)
            # Atualiza o peso total da MST
            total_weight += weight
    
    # Retorna a MST e o peso total
    return mst, total_weight 

def main():
    pygame.init()
    screen = pygame.display.set_mode((1300, 800))
    pygame.display.set_caption("Kruskal's Algorithm Visualization")
    screen.fill(BLACK) 
    graph = create_graph()

    draw_graph(screen, graph, node_positions)
    pygame.display.flip()

    mst, total_weight = kruskal(graph)
    
    print("Minimum Spanning Tree (MST) Edges:")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]} (Weight: {edge[2]})")
    print(f"Total Weight of MST: {total_weight}") 

    animate_kruskal(screen, mst, node_positions)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        input("Pressione Enter para sair...")
