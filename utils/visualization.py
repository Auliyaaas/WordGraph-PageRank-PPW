import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(G, title):
    fig, ax = plt.subplots(figsize=(12, 10))
    pos = nx.spring_layout(G, k=0.8, iterations=50)
    nx.draw(G, pos, node_size=800, with_labels=True, ax=ax)
    ax.set_title(title)
    ax.axis('off')
    return fig