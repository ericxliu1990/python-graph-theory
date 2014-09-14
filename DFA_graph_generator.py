"""
A graph for generating DFA random graph
"""
import random
from computing_degree_distribution import *

def make_complete_graph(node_number):
	"""
	take a number and return complete graph of that number
	"""
	complete_graph = dict()
	for index_i in xrange(node_number):
		a_set = set([])
		for index_j in range(node_number):
			if not index_j  == index_i:
				a_set.add(index_j)
		complete_graph[index_i] = a_set
	return complete_graph

def DFA_degree_generator(node_number, complete_node_num):
	"""
	"""
	if node_number < complete_node_num:
		raise ArithmeticError
	graph  = make_complete_graph(complete_node_num)
	for index_i in xrange(complete_node_num, node_number - 1):
		a_set = set([])
		for dummy_index_j in xrange(0, complete_node_num):
			a_set.add(random.choice(graph.keys()))
		graph[index_i] = a_set
	return graph

# print make_complete_graph(5)
print DFA_degree_generator(27770, 1)