"""
A program for computing degree distributons for graphs
"""

#the example graphs
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]),2: set([3]),
		3: set([0]), 4: set([1]), 5: set([2]),
		6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]),
		3: set([7]), 4: set([1]), 5: set([2]),
		6: set([]), 7: set([3]), 8: set([1, 2]),
		9: set([0, 3, 4, 5, 6, 7])}

def make_complete_graph(num_nodes):
	"""
	take a number and return complete graph of that number
	"""
	complete_graph = dict()
	for index_i in range(num_nodes):
		a_set = set([])
		for index_j in range(num_nodes):
			if not index_j  == index_i:
				a_set.add(index_j)
		complete_graph[index_i] = a_set
	return complete_graph

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

#print in_degree_distribution(EX_GRAPH2)
#print compute_in_degrees(EX_GRAPH0)
