import networkx as nx
import pandas as pd




def build_filtered_graph(adj_df, min_weight=5):
    G = nx.from_pandas_adjacency(adj_df)
    Gf = nx.Graph()
    for u, v, d in G.edges(data=True):
        if d['weight'] >= min_weight:
            Gf.add_edge(u, v, weight=d['weight'])
    return Gf




def compute_all_centrality(G, top_n=20):
    pagerank = nx.pagerank(G)
    degree = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)

    pr_df = pd.DataFrame(pagerank.items(), columns=['Kata', 'PageRank'])\
            .sort_values(by='PageRank', ascending=False).head(top_n)


    sub_nodes = pr_df['Kata'].tolist()
    subgraph = G.subgraph(sub_nodes)


    summary = pd.DataFrame({
    'Kata': sub_nodes,
    'PageRank': [pagerank[n] for n in sub_nodes],
    'Degree': [degree[n] for n in sub_nodes],
    'Betweenness': [betweenness[n] for n in sub_nodes],
    'Closeness': [closeness[n] for n in sub_nodes]
    })

    return pr_df, summary, subgraph