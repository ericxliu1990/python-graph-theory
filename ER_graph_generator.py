"""
A program for generating ER ramdom graph
"""
import random
from computing_degree_distribution import *
import matplotlib.pyplot as pyplot

def ER_graph_generator(node_num, probability):
	"""
	Based on the input the number of nodes and probability,
	reutrn adjacent list of the ER random graph
	"""
	graph = dict()
	for dummpy_index in xrange(node_num):
		graph[dummpy_index] = set([])
		for dummpy_index2 in xrange(node_num):
			if not dummpy_index == dummpy_index2:
				random_number = random.random()
				if random_number < probability:
					graph[dummpy_index].add(dummpy_index2)
	return graph

GRAPH_1 = ER_graph_generator(5000, 0.5)
print "ok"
plot_list = normalize_distribution(in_degree_distribution(GRAPH_1), 'STANDARD')
pyplot.plot(plot_list[0], plot_list[1], 'r-')
pyplot.show()