# 代码生成时间: 2025-10-10 21:02:55
import streamlit as st
# FIXME: 处理边界情况
import networkx as nx
from networkx.algorithms import is_directed_acyclic_graph
import matplotlib.pyplot as plt
# NOTE: 重要实现细节
import pandas as pd
import re
# 扩展功能模块

"""
Dependency Analyzer
==================

This Streamlit application allows users to upload a graph representation of dependencies
and visualize the result. It can determine if the dependency graph is acyclic.
"""

@st.cache(allow_output_mutation=False)
def load_graph(edges):
    """
    Load the graph from a list of tuples representing edges.
    Each tuple is a directed edge (from_node, to_node).
    """
    G = nx.DiGraph()
    G.add_edges_from(edges)
    return G

def visualize_graph(G):
    """
    Visualize the graph using NetworkX and Matplotlib.
    """
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()

def check_cyclic(G):
    """
    Check if the graph is a Directed Acyclic Graph (DAG).
    Returns True if it is acyclic, False otherwise.
    """
    return is_directed_acyclic_graph(G)

def parse_edge_list(edge_list):
    """
    Parse a string input into a list of edges.
    Edges are expected to be in the format 'node1,node2,weight'.
# 改进用户体验
    """
# 扩展功能模块
    edges = []
    for line in edge_list.split('
'):
        match = re.match(r'([^\s]+)\s+([^\s]+)\s*(\d+)?', line)
        if match:
            from_node, to_node, weight = match.groups()
            weight = int(weight) if weight else 1
            edges.append((from_node, to_node, weight))
        else:
            st.error(f"Invalid edge format: {line}")
    return edges

def main():
    st.title('Dependency Analyzer')
    st.write('Upload a text file containing the dependency graph edges.')
    file = st.file_uploader('Choose a file', type=['txt'])
# 添加错误处理
    if file is not None:
        try:
            edge_list = file.read().decode('utf-8')
# 增强安全性
            edges = parse_edge_list(edge_list)
# NOTE: 重要实现细节
            G = load_graph(edges)
            st.header('Visualized Graph')
# TODO: 优化性能
            visualize_graph(G)
            st.header('Cyclic Check')
            is_cyclic = check_cyclic(G)
            if is_cyclic:
                st.success('The graph is a Directed Acyclic Graph (DAG).')
            else:
# 增强安全性
                st.error('The graph contains cycles.')
        except Exception as e:
            st.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()