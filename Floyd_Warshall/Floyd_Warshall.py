import math


def floyd_warshall(list_vertices: list, list_edges: list) -> list:
    """
    Psuedocode for Floyd Warshall algorithm
    """
    inf = math.inf

    # Create distance array
    num_vertices = len(list_vertices)
    dist_arr = [[inf for i in range(num_vertices)] for j in range(num_vertices)]

    for v in list_vertices:
        u = v.u
        dist_arr[u][u] = 0

    for edges in list_edges:
        u = edges.u
        v = edges.v
        w = edges.w
        dist_arr[u][v] = w

    # Floyd warshall here : O(V^3)
    for jump in list_vertices:
        for source in list_vertices:
            for dest in list_vertices:
                existing_dist = dist_arr[source][dest]
                new_dist = dist_arr[source][jump] + dist_arr[jump][dest]
                dist_arr[source][dest] = min(existing_dist, new_dist)

    return dist_arr
