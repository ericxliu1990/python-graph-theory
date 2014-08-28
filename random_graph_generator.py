"""
A program for generating ER ramdom graph
"""
import random

def ER_graph_generator(node_num, probability):
	"""
	Based on the input the number of nodes and probability,
	reutrn adjacent list of the ER random graph
	"""
	graph = dict()
	for dummpy_index in range(node_num):
		graph[dummpy_index] = set([])
		for dummpy_index2 in range(node_num):
			if not dummpy_index == dummpy_index2:
				random_number = random.random()
				if random_number < probability:
					graph[dummpy_index].add(dummpy_index2)
	return graph

print ER_graph_generator(5, 0)