import graphviz
import json
from graph import create_graph

def plot_graph(graph, path):
    dot = graphviz.Digraph(graph_attr={'splines': 'true'})

    # Adiciona nós ao gráfico, ajustando a posição para se assemelhar a um mapa
    for node, pos in node_positions.items():
        if node in path:
            dot.node(str(node), pos=pos, style='filled', fillcolor='lightblue')
        else:
            dot.node(str(node), pos=pos)

    # Adiciona arestas ao gráfico, ajustando a cor para se assemelhar a um mapa
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            if (node in path and neighbor in path and 
                path.index(node) + 1 == path.index(neighbor)):
                dot.edge(str(node), str(neighbor), label=str(weight), color='darkblue', penwidth='2')
            else:
                dot.edge(str(node), str(neighbor), label=str(weight), color='gray')

    # Salva e visualiza o gráfico
    dot.render('grafo_dijkstra.dot', format='png', view=True)

if __name__ == "__main__":
    # Carrega o grafo
    graph = create_graph()
    
    # Lê o caminho mais curto do arquivo JSON
    with open('shortest_path.json', 'r') as f:
        data = json.load(f)
        path = data['path']

    # Define as posições dos nós
    node_positions = {
        1: '100,100!', 2: '250,150!', 3: '200,250!', 4: '300,350!', 5: '400,450!', 
        6: '350,200!', 7: '450,300!', 8: '500,400!', 9: '600,500!', 10: '650,150!',
        11: '700,350!', 12: '200,450!', 13: '300,550!', 14: '250,300!', 15: '500,150!',
        16: '100,550!', 17: '150,350!', 18: '350,500!', 19: '400,100!', 20: '550,350!',
        21: '450,550!', 22: '200,650!', 23: '600,200!', 24: '700,550!', 25: '800,250!',
        26: '400,650!', 27: '550,500!', 28: '600,100!', 29: '700,400!', 30: '750,450!',
        31: '800,600!', 32: '850,200!', 33: '900,350!', 34: '950,500!', 35: '1000,650!',
        36: '1050,100!', 37: '1100,300!', 38: '1150,450!', 39: '1200,600!', 40: '1250,100!'
    }

    # Plota o grafo com o caminho mais curto destacado
    plot_graph(graph, path)









