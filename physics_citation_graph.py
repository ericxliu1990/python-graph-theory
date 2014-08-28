"""
Plot a graph of physics citation graph
"""
from computing_degree_distribution import *
import matplotlib.pyplot as pyplot

GRAPH_FILE_NAME = "alg_phys-cite.txt"

def load_graph(graph_file_name):
	"""
	Function that loads a graph file and returns a dictionary that models a graph
	"""
	graph_file = open(graph_file_name)
	graph_text = graph_file.read()
	graph_lines = graph_text.split('\n')
	graph_lines = graph_lines[ : -1] 

	print "Loaded graph with", len(graph_lines), "nodes"
	a_graph = {}
	for a_line in graph_lines:
		neighbors = a_line.split(' ')
		a_node = int(neighbors[0])
		a_graph[a_node] = set([])
		for a_neighbor in neighbors[1 : -1]:
			a_graph[a_node].add(int(a_neighbor))

	return a_graph

#Test input graph
physic_graph = load_graph(GRAPH_FILE_NAME)
plot_list = normalize_distribution(in_degree_distribution(physic_graph), 'LOGLOG')
pyplot.plot(plot_list[0], plot_list[1], 'r-')
pyplot.show()
# print plot_list