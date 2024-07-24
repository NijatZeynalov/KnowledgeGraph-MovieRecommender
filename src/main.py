import pandas as pd
from data.preprocess_data import preprocess_tmdb_data,load_tmdb_data
from data.generate_knowledge_graph import generate_knowledge_graph, save_knowledge_graph
from utils.config import MOVIES_PATH, CREDITS_PATH, KNOWLEDGE_GRAPH_PATH
from utils.helpers import ensure_directory
import rdflib
from rdflib import Graph
import networkx as nx
import matplotlib.pyplot as plt
from urllib.parse import unquote


def ttl_to_graph(ttl_path):
    g = Graph()
    g.parse(ttl_path, format="turtle")
    return g


def graph_to_networkx(graph):
    nx_graph = nx.DiGraph()
    node_labels = {}
    node_counter = 1

    for subj, pred, obj in graph:
        subj_label = str(subj).split('/')[-1]
        obj_label = str(obj).split('/')[-1]
        if subj_label not in node_labels:
            node_labels[subj_label] = f'Node{node_counter}'
            node_counter += 1
        if obj_label not in node_labels:
            node_labels[obj_label] = f'Node{node_counter}'
            node_counter += 1
        nx_graph.add_edge(node_labels[subj_label], node_labels[obj_label], label=str(pred).split('/')[-1])

    reverse_node_labels = {v: unquote(k.replace('Node', '')) for k, v in node_labels.items()}
    return nx_graph, reverse_node_labels


def visualize_graph(nx_graph, reverse_node_labels, output_path):
    pos = nx.spring_layout(nx_graph, k=0.5)
    plt.figure(figsize=(16, 16))
    nx.draw(nx_graph, pos, labels=reverse_node_labels, with_labels=True, node_size=2000, node_color="lightblue",
            font_size=12, font_weight="bold", arrows=True)
    edge_labels = nx.get_edge_attributes(nx_graph, 'label')
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels, font_color='red', font_size=10)
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()


def visualize_ttl(ttl_path, output_path):
    graph = ttl_to_graph(ttl_path)
    nx_graph, reverse_node_labels = graph_to_networkx(graph)
    visualize_graph(nx_graph, reverse_node_labels, output_path)


def main():
    ensure_directory('output')

    tmdb_movies_df, tmdb_credits_df = load_tmdb_data(MOVIES_PATH, CREDITS_PATH)
    merged_df = preprocess_tmdb_data(tmdb_movies_df, tmdb_credits_df)

    kg = generate_knowledge_graph(merged_df)
    save_knowledge_graph(kg, KNOWLEDGE_GRAPH_PATH)
    print(f"Knowledge graph saved to {KNOWLEDGE_GRAPH_PATH}")

    png_output_path = KNOWLEDGE_GRAPH_PATH.replace('.ttl', '.png')
    visualize_ttl(KNOWLEDGE_GRAPH_PATH, png_output_path)
    print(f"Knowledge graph visualization saved to {png_output_path}")


if __name__ == "__main__":
    main()