"""
A program for computing degree distributons for graphs
"""
import math

#the example graphs
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]),2: set([3]),
		3: set([0]), 4: set([1]), 5: set([2]),
		6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]),
		3: set([7]), 4: set([1]), 5: set([2]),
		6: set([]), 7: set([3]), 8: set([1, 2]),
		9: set([0, 3, 4, 5, 6, 7])}

def compute_in_degrees(digraph):
	"""
	take a directed graph and return a map of in-degrees of nodes to the nodes 
	"""
	in_degree = dict()
	for from_node in digraph:
		for to_node in digraph.get(from_node):
			if  to_node not in in_degree:
				in_degree[to_node] = 1
			else:
				# print to_node
				in_degree[to_node] = in_degree[to_node] + 1
	for from_node in digraph:
		if from_node not in in_degree:
			in_degree[from_node] = 0
	return in_degree

def in_degree_distribution(digraph):
	"""
	take a directed graph and return the in degree distrubution of it
	"""
	in_degree = compute_in_degrees(digraph)
	in_degree_dis = {}
	for a_node in in_degree:
		a_node_value = in_degree[a_node]
		if a_node_value not in in_degree_dis:
			in_degree_dis[a_node_value] = 1
		else:
			in_degree_dis[a_node_value] = in_degree_dis[a_node_value] + 1
	return in_degree_dis

def normalize_distribution(distribution, type = 'STANDARD'):
	"""
	normalize a distribution and return a tuple of two lists. One of them is 
	"""
	distribution_sum = 0
	for number in distribution:
		distribution_sum = distribution_sum + distribution[number]

	distribution_key = []
	distribution_value = []
	if  distribution.get(0):
		del distribution[0]
	for number in distribution:
		if type == 'STANDARD':
			distribution_key.append(number)
			distribution_value.append(float(distribution[number]) / distribution_sum)
		else:
			distribution_key.append(math.log(number))
			distribution_value.append(math.log(float(distribution[number]) / distribution_sum))
	return [list(x) for x in zip(*sorted(zip(distribution_key, distribution_value), key = lambda pair: pair[0]))]

#print in_degree_distribution(EX_GRAPH2)
#print compute_in_degrees(EX_GRAPH0)
