"""
Plot a graph of physics citation graph
"""
from computing_degree_distribution import *
import matplotlib.pyplot as pyplot
import math

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

def normalize_distribution(distribution, type = 'STANDARD'):
	"""
	normalize a distribution and return a tuple of two lists. One of them is 
	"""
	distribution_sum = 0
	for number in distribution:
		distribution_sum = distribution_sum + distribution[number]

	distribution_key = []
	distribution_value = []
	del distribution[0]
	for number in distribution:
		if type == 'STANDARD':
			distribution_key.append(number)
			distribution_value.append(float(distribution[number]) / distribution_sum)
		else:
			distribution_key.append(math.log(number))
			distribution_value.append(math.log(float(distribution[number]) / distribution_sum))
	return [list(x) for x in zip(*sorted(zip(distribution_key, distribution_value), key = lambda pair: pair[0]))]

#Test input graph
physic_graph = load_graph(GRAPH_FILE_NAME)
plot_list = normalize_distribution(in_degree_distribution(physic_graph), 'STANDARD')
pyplot.plot(plot_list[0], plot_list[1], 'r-')
pyplot.show()
# print plot_list