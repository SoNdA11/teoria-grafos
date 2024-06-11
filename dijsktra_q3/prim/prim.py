import heapq  # Importa o módulo heapq, que fornece funcionalidades para implementar filas de prioridade usando heaps.

def prim(graph, start):
    mst = []  # Lista para armazenar a árvore geradora mínima.
    visited = set()  # Conjunto para armazenar os nós visitados durante a busca.
    min_heap = [(0, start, None)]  # Fila de prioridade para escolher a próxima aresta com menor peso.
    total_weight = 0  # Variável para armazenar o peso total da árvore geradora mínima.

    while min_heap:  # Inicia um loop que executa enquanto a fila de prioridade não estiver vazia.
        weight, current, previous = heapq.heappop(min_heap)  # Remove o elemento com menor peso da fila de prioridade.
        if current in visited:  # Verifica se o nó atual já foi visitado.
            continue  # Se sim, passa para a próxima iteração do loop.
        visited.add(current)  # Adiciona o nó atual ao conjunto de nós visitados.

        if previous is not None:  # Verifica se não é a primeira iteração do loop.
            mst.append((previous, current, weight))  # Adiciona a aresta à árvore geradora mínima.
            total_weight += weight  # Atualiza o peso total da árvore geradora mínima.

        for neighbor, edge_weight in graph[current].items():  # Itera sobre os vizinhos do nó atual e os pesos das arestas associadas.
            if neighbor not in visited:  # Verifica se o vizinho não foi visitado ainda.
                heapq.heappush(min_heap, (edge_weight, neighbor, current))  # Adiciona o vizinho à fila de prioridade.

    return mst, total_weight  # Retorna a árvore geradora mínima e o peso total.
