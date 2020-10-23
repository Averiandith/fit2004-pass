import math

class Node:
    pass

class Edge:
    pass

def bellman_ford(list_vertices: list, list_edges: list, source_vertex: Node) -> list:
    """
    Vanilla bellman ford without optimization (for you to figure it out)
    """
    inf = math.inf

    # Create distance array
    dist_arr = [inf] * len(list_vertices)

    # Initialization : O(V)
    for v in list_vertices:
        if v is source_vertex:
            dist_arr[v] = 0
        else:
            dist_arr[v] = inf
    
    # Relax edges repeatedly : O(VE)
    for _ in range(len(list_vertices)):
        for edge in list_edges:
            if dist_arr[edge.u] + dist_arr[edge.w] < dist_arr[edge.v]:
                dist_arr[edge.v] = dist_arr[edge.u] + edge.w

    # Check for negative cycles : O(E)
    for edge in list_edges:
        if dist_arr[edge.u] + dist_arr[edge.w] < dist_arr[edge.v]:
            print("Contain negative cycle!")

    return dist_arr