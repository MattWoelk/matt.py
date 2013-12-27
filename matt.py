from collections import deque

def _get_connected_nodes(graph, node):
    if hasattr(graph, '__call__'):
        return graph(node)
    else:
        return graph[node]

def _is_at_end(end, path):
    if hasattr(end, '__call__'):
        return end(path)
    else:
        return path[-1] == end

def bfs(graph, start, end):
    """Breadth-first search

    inspired by - http://stackoverflow.com/a/16747264/947305

    Args:
        graph: a dict where keys are the node and the value is an list of nodes
               which it connects to
            OR a function which takes in the current node and returns
               connecting nodes as a list
        start: the node to start the search
        end:   the node to end the search
            OR a function which evaluates to true when a condition is met. This
               function takes the current path represented by a list
    Returns:
        the shortest path from start to end as a list of nodes (in order of visit)

    Assumptions:
    - the edges are not weighted
    - the edges are only in the direction speficied in the graph

    >>> bfs({'a':['b'], 'b':['a','c'], 'c':['b']}, 'a', 'c')
    ['a', 'b', 'c']

    >>> def generate_connected_nodes(nod):
    ...     return [nod+1, nod+2]
    ...
    >>> bfs(generate_connected_nodes, 0, 3)
    [0, 1, 3]

    >>> def len_gt_2(path):
    ...     return len(path) > 2
    ...
    >>> bfs({'a':['b'], 'b':['c'], 'c':['d'], 'd':['a']}, 'a', len_gt_2)
    ['a', 'b', 'c']

    >>> bfs({'a':['b'], 'b':['a'], 'c':['b']}, 'a', 'c') is None
    True
    """

    q = deque()
    path = [start]
    q.append(path)
    visited = set([start])

    while not len(q) == 0:
        path = q.popleft()
        last_node = path[-1]
        if _is_at_end(end, path):
            return path
        for node in _get_connected_nodes(graph, last_node):
            if node not in visited:
                visited.add(node)
                q.append(path + [node])
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()



