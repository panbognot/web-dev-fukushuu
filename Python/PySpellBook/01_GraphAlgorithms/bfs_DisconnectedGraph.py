'''
Generic Function for BFS traversal of a Graph
 (valid for directed as well as undirected graphs
 which can have multiple disconnected components)
-- Inputs --
-> V - represents number of vertices in the Graph
-> adj[] - represents adjacency list for the Graph
-- Output --
-> bfs_traversal - a vector containing bfs traversal
for entire graph
'''
 
 
def bfsOfGraph(V, adj):
 
    bfs_traversal = []
    vis = [False]*V
    for i in range(V):
 
        # To check if already visited
        if (vis[i] == False):
            q = []
            vis[i] = True
            q.append(i)
 
            # BFS starting from ith node
            while (len(q) > 0):
                g_node = q.pop(0)
 
                bfs_traversal.append(g_node)
                for it in adj[g_node]:
                    if (vis[it] == False):
                        vis[it] = True
                        q.append(it)
 
    return bfs_traversal