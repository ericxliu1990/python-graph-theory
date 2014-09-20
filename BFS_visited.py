"""
a BFS visited test file
"""
from collections import deque
# from test_case import *

def bfs_visited(ugraph, start_node):
	"""
	Takes the undirected graph ugraph and the node start_node and 
	returns the set consisting of all nodes that are visited by a 
	breadth-first search that starts at start_node.
	"""
	if not start_node in ugraph:
		raise Exception
	queue = deque()
	visited = set([start_node])
	queue.append(start_node)
	while not len(queue) == 0:
		next_node = queue.pop()
		print next_node
		for neigboor in ugraph[next_node]:
			if not neigboor in visited:
				visited.add(neigboor)
				queue.append(neigboor)
	return visited
def  cc_visited(ugraph):
	"""
	Takes the undirected graph ugraph and returns a list of sets, 
	where each set consists of all the nodes (and nothing else) in
	a connected component, and there is exactly one set in the list for 
	each connected component in ugraph and nothing else.
	"""
	remaining_nodes = set([key for key in ugraph])
	component_list = list()
	while not len(remaining_nodes) == 0:
		node = next(iter(remaining_nodes))
		a_component = bfs_visited(ugraph, node)
		component_list.append(a_component)
		remaining_nodes = remaining_nodes - a_component
	return component_list

def largest_cc_size(ugraph):
	"""
	akes the undirected graph ugraph and returns the size (an integer) 
	of the largest connected component in ugraph
	"""
	component_list = cc_visited(ugraph)
	max_cc_size = 0
	for a_component in component_list:
		max_cc_size = max(max_cc_size, len(a_component))
	return max_cc_size

def compute_resilience(ugraph, attack_order):
	"""
	Takes the undirected graph ugraph, a list of nodes attack_order and 
	iterates through the nodes in attack_order. For each node in the list, 
	the function removes the given node and its edges from the graph 
	and then computes the size of the largest connected component for 
	the resulting graph.
	"""
	def remove_nodes(a_node):
		"""remove a node from an undirected graph"""
		for a_neighboor in ugraph[a_node]:
			ugraph[a_neighboor].remove(a_node)
		del ugraph[a_node]

	a_graph = ugraph
	largest_component_list = list()
	largest_component_list.append(largest_cc_size(a_graph))
	for an_order in attack_order:
		if an_order in a_graph:
			remove_nodes(an_order)
			largest_component_list.append(largest_cc_size(a_graph))
		else:
			print an_order
			raise Exception
	return largest_component_list
# def main():
# 	attack_order = [1, 2, 3]
# 	for a_graph in GRAPH_LIST:
# 		print a_graph
# 		print "compute_resilience: ", compute_resilience(a_graph, attack_order)
# 		print "---------------------"

# if __name__ == '__main__':
# 	main()
