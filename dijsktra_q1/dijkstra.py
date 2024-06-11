import heapq

def dijkstra(graph, start):
    
    # Inicializa as distâncias para todos os nós como infinito, exceto para o nó de início
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Inicializa a fila de prioridade com a tupla (distância, nó)
    priority_queue = [(0, start)]
    
    # Dicionário para armazenar o caminho mais curto de cada nó até o nó inicial
    shortest_path = {}

    # Enquanto houver nós na fila de prioridade
    while priority_queue:
        # Remove o nó com menor distância da fila de prioridade
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Se a distância atual for maior do que a distância já conhecida, ignore este nó
        if current_distance > distances[current_node]:
            continue

        # Para cada vizinho do nó atual
        for neighbor, weight in graph[current_node].items():
            # Calcula a distância até o vizinho passando pelo nó atual
            distance = current_distance + weight
            
            # Se a nova distância for menor do que a distância já conhecida para o vizinho
            if distance < distances[neighbor]:
                # Atualiza a distância para o vizinho
                distances[neighbor] = distance
                
                # Adiciona o vizinho à fila de prioridade com a nova distância
                heapq.heappush(priority_queue, (distance, neighbor))
                
                # Atualiza o caminho mais curto para o vizinho
                shortest_path[neighbor] = current_node

    # Retorna as distâncias mínimas e o caminho mais curto
    return distances, shortest_path
