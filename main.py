from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        current = frontier.pop()
        frontier.update(graph[current].difference(result))
        result.update(graph[current].difference(result))
    return result

def connected(graph):
    return set(graph) == reachable(graph, set(graph).pop())

def n_components(graph):
    g = set(graph)
    count = 0
    while len(g) != 0:
        count += 1
        current = g.pop()
        comp = reachable(graph, current)
        g.difference_update(comp)
    return count