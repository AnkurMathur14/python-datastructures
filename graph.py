"""
Graph implementation
"""
import copy
import heapq
from math import inf
from q import Queue
from stack import Stack
import heapq as hq
from collections import deque


class Graph:
    """
    Graph using adjacency matrix
    Data in Vertices can only have 0 to vertices-1
    Here, index itself represent data
    """
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]

    def print(self):
        print()
        for row in self.adj_matrix:
            print(row)
        print()

    def add_edge(self, src, dst):
        if src < 0 or src >= self.vertices or dst < 0 or dst >= self.vertices:
            print("Invalid src or destination edge")
            return False

        self.adj_matrix[src][dst] = 1
        self.adj_matrix[dst][src] = 1
        return True

    def remove_edge(self, src, dst):
        if src < 0 or src >= self.vertices or dst < 0 or dst >= self.vertices:
            print("Invalid src or destination edge")
            return False

        self.adj_matrix[src][dst] = 0
        self.adj_matrix[dst][src] = 0
        return True

    def dfs_util(self, start_vertex, visited):

        visited[start_vertex] = True
        print(start_vertex, end=" ")
        for i, connection in enumerate(self.adj_matrix[start_vertex]):
            if connection == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex):
        visited = [False] * self.vertices
        self.dfs_util(start_vertex, visited)

        # For disconnected components
        connected_components = 1
        for i in range(self.vertices):
            if not visited[i]:
                connected_components += 1
                self.dfs_util(i, visited)
        print("\nConnected components: ", connected_components)

    def bfs_utils(self, start_vertex, visited):
        q = Queue()
        print()
        visited[start_vertex] = True
        q.push(start_vertex)
        while not q.empty():
            vertex = q.pop()
            print(vertex, end=" ")
            for i, connection in enumerate(self.adj_matrix[vertex]):
                if connection == 1 and not visited[i]:
                    visited[i] = True
                    q.push(i)

    def bfs(self, start_vertex):
        visited = [False] * self.vertices
        self.bfs_utils(start_vertex, visited)

        # For disconnected components
        connected_components = 1
        for i in range(self.vertices):
            if not visited[i]:
                connected_components += 1
                self.bfs_utils(i, visited)
        print("\nConnected components: ", connected_components)



class Graph2:
    """
    Graph using adjacency list
    Data in Vertices can only have 0 to vertices-1
    Here, index itself represent data
    """
    def __init__(self, vertices):
        self.vertices = vertices
        self.adJ_list = [[] for _ in range(self.vertices)]

    def print(self):
        print()
        for row in self.adJ_list:
            print(row)
        print()

    def add_edge(self, src, dst):
        if src < 0 or src >= self.vertices or dst < 0 or dst >= self.vertices:
            print("Invalid src or destination edge")
            return False

        self.adJ_list[src].append(dst)
        #self.adJ_list[dst].append(src)
        return True

    def remove_edge(self, src, dst):
        if src < 0 or src >= self.vertices or dst < 0 or dst >= self.vertices:
            print("Invalid src or destination edge")
            return False

        self.adJ_list[src].remove(dst)
        #self.adJ_list[dst].remove(src)
        return True

    def dfs_util(self, start_vertex, visited):
        visited[start_vertex] = True
        print(start_vertex, end=" ")
        for connection in self.adJ_list[start_vertex]:
            if not visited[connection]:
                self.dfs_util(connection, visited)

    def dfs(self, start_vertex):
        visited = [False] * self.vertices
        self.dfs_util(start_vertex, visited)

        # For disconnected components
        connected_components = 1
        for i in range(self.vertices):
            if not visited[i]:
                connected_components += 1
                self.dfs_util(i, visited)
        print("\nConnected components: ", connected_components)

    def bfs_utils(self, start_vertex, visited):
        q = Queue()
        print()
        visited[start_vertex] = True
        q.push(start_vertex)
        while not q.empty():
            vertex = q.pop()
            print(vertex, end=" ")
            for connection in self.adJ_list[vertex]:
                if not visited[connection]:
                    visited[connection] = True
                    q.push(connection)

    def bfs(self, start_vertex):
        visited = [False] * self.vertices
        self.bfs_utils(start_vertex, visited)

        # For disconnected components
        connected_components = 1
        for i in range(self.vertices):
            if not visited[i]:
                connected_components += 1
                self.bfs_utils(i, visited)
        print("\nConnected components: ", connected_components)

    def count_paths_utils(self, src, dst, visited, count, paths, current_path):

        # Visit
        visited[src] = True
        current_path.append(src)

        # Explore its neighbours
        for neighbour in self.adJ_list[src]:
            if neighbour == dst:
                count[0] += 1
                current_path.append(dst)
                paths.append(copy.deepcopy(current_path))
                current_path.pop()
            if not visited[neighbour]:
                self.count_paths_utils(neighbour, dst, visited, count, paths, current_path)

        # Unvisit
        if current_path:
            current_path.pop()
        visited[src] = False

    def count_paths(self, src, dst):
        count = [0]
        paths = []
        current_path = []
        visited = [False] * self.vertices
        self.count_paths_utils(src, dst, visited, count, paths, current_path)
        return count[0], paths

    def is_cycle_present_utils(self, start_vertex, colours):
        colours[start_vertex] = "GREY"
        for neighbor in self.adJ_list[start_vertex]:
            if colours[neighbor] == "BLACK":
                continue
            if colours[neighbor] == "GREY":
                return True

            if self.is_cycle_present_utils(neighbor, colours):
                return True

        colours[start_vertex] = "BLACK"
        return False

    def is_cycle_present(self):
        colours = ["WHITE"] * self.vertices
        for i in range(self.vertices):
            if colours[i] == "WHITE":
                if self.is_cycle_present_utils(i, colours):
                    return True
        return False

    def is_cycle_present_undirected_utils(self, start_vertex, visited, parent):
        visited[start_vertex] = True
        for neighbour in self.adJ_list[start_vertex]:
            if not visited[neighbour]:
                if self.is_cycle_present_undirected_utils(neighbour, visited, start_vertex):
                    return True
            else:
                if neighbour != parent:
                    return True
        return False

    # T: O(V + E) | S: O(V)
    def is_cycle_present_undirected(self):
        visited = [False] * self.vertices
        for i, visit in enumerate(visited):
            if not visit:
                if self.is_cycle_present_undirected_utils(i, visited, -1):
                    return True
        return False

    """
    PROGRAM to check if graph is a valid tree or not
    1. Graph must be undirected
    2. Graph must be acyclic
    3. Graph must be connected

    # Find loop
    def valid_tree_utils(self, start_vertex, adj_list, visited, parent):
        visited[start_vertex] = True
        for n in adj_list[start_vertex]:
            if visited[n]:
                if n != parent:
                    return True
            if self.valid_tree_utils(n, adj_list, visited, n):
                return True
        return False
                
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
    
        # Create afj_list frm list of edges
        adj_list = defaultdict(list)
        for s, d in edges:
            adj_list[s].append(d)

        visited = [False] * n
        if self.valid_tree_utils(0, adj_list, visited, None):
            return False # If cycle found, not a  tree

        for v in visited:
            if not v:
                return False # If any node is not reachable, not a tree
        return True
    """



class Graph3:
    """
    Graph using adjacency list
    Here, Data of node can be anything, not limiting to 0 to vertices-n
    Data of node can be int, string etc
    """
    def __init__(self):
        self.adj_list = {}
        # Here, it is like {v0 : [v1, v2, v3], v1: [vo, v3]} etc
        # We can also use hash table (set) in place of list above.
        # This will make searching n O(1)

    def print(self):
        print()
        for vertex, connections in self.adj_list.items():
            print("{} -> ".format(vertex), end=" ")
            for connection in connections:
                print(connection, end=" ")
            print()
        print()

    def add_edge(self, src, dst, distance):
        if src in self.adj_list:
            self.adj_list[src].append((dst, distance))
        else:
            self.adj_list[src] = [(dst, distance)]

        if dst in self.adj_list:
            self.adj_list[dst].append((src, distance))
        else:
            self.adj_list[dst] = [(src, distance)]

    def remove_edge(self, src, dst):
        if src in self.adj_list:
            for i, connection in enumerate(self.adj_list[src]):
                if connection[0] == dst:
                    self.adj_list[src].pop(i)
                    break
        if dst in self.adj_list:
            for i, connection in enumerate(self.adj_list[dst]):
                if connection[0] == dst:
                    self.adj_list[dst].pop(i)
                    break

    def dfs_utils(self, start_vertex, visited):
        visited[start_vertex] = True
        print(start_vertex, end=" ")
        for connection in self.adj_list[start_vertex]:
            if not visited[connection[0]]:
                self.dfs_utils(connection[0], visited)

    def dfs(self, start_vertex):
        visited = {}
        for vertex in self.adj_list:
            visited[vertex] = False

        self.dfs_utils(start_vertex, visited)

        # For disconnected components
        connected_components = 1
        for vertex, visit in visited.items():
            if not visit:
                connected_components += 1
                self.dfs_utils(vertex, visited)
        print("\nConnected components: ", connected_components)

    def bfs_utils(self, start_vertex, visited):
        q = Queue()
        visited[start_vertex] = True
        q.push(start_vertex)

        while not q.empty():
            vertex = q.pop()
            print(vertex, end=" ")
            for connection in self.adj_list[vertex]:
                if not visited[connection[0]]:
                    visited[connection[0]] = True
                    q.push(connection[0])

    def bfs(self, start_vertex):
        print()
        visited = {}
        for vertex in self.adj_list:
            visited[vertex] = False

        self.bfs_utils(start_vertex, visited)

        # For disconnected components
        connected_components = 1
        for vertex, visit in visited.items():
            if not visit:
                connected_components += 1
                self.bfs_utils(vertex, visited)
        print("\nConnected components: ", connected_components)
        print()

    """
    Dijkstra Algorithm

    The time complexity of dijkstra's algorithm can be reduced to O((V+E)logV) using adjacency list representation of
    the graph and a min-heap to store the unvisited vertices,
    where E is the number of edges in the graph and V is the number of vertices in the graph.


    Time for visiting all vertices =O(V+E)
    
    Time required for processing one vertex=O(logV)
    
    Time required for visiting and processing all the vertices = O(V+E)*O(logV) = O((V+E)logV)
    
    The space complexity in this case will also improve to O(V) as both the adjacency list and min-heap require O(V) space.
     So the total space complexity becomes
    
    O(V)+O(V)=O(2V) = O(V)
    """
    def shortest_path(self, start_vertex):

        # Create a visited map
        visited = {}
        for vertex in self.adj_list.keys():
            visited[vertex] = False

        # Create a distance map
        distances = {}
        for vertex in self.adj_list.keys():
            distances[vertex] = inf

        # Self distance is 0
        distances[start_vertex] = 0

        # Create a MIN heap
        heap = []
        hq.heappush(heap, (distances[start_vertex], start_vertex))
        while heap:  # T: O(E)
            curr_distance, min_distance_vertex = hq.heappop(heap)  # T: O(logv)
            visited[min_distance_vertex] = True
            # T: Since each vertices will be visited only  once, hence, T for this loop is none
            # as it is included in outer loop
            for neighbours in self.adj_list[min_distance_vertex]:
                neighbour_name = neighbours[0]
                neighbour_distance = neighbours[1]
                if not visited[neighbour_name]:
                    distances[neighbour_name] = min(distances[neighbour_name], (curr_distance + neighbour_distance))
                    hq.heappush(heap, (distances[neighbour_name], neighbour_name)) # T: O(logv)

        for city, distance in distances.items():
            if distance == inf:
                distance = "No route found"
            print("Shortest distance from {} to {} : {}".format(start_vertex, city, distance))

"""
Graph1:

    v0 --------- v1
    |   \         | 
    |      \      |
    |          \  |
    v2           v3
    
    
Graph2: 
        laddakh
            \
             \450
              \
             manali
             /
            /300
        shimla
        

        delhi                   
        /	\
       /     \500
      /       \
 1000/	    lucknow             
    /		    \800             
   /             \
 mumbai	          \
   \              kolkata
    \           /             
  400\	       /600
      \       /              
     hyderabad  

delhi ->  ('lucknow', 500) ('mumbai', 1000) 
lucknow ->  ('delhi', 500) ('kolkata', 800) 
mumbai ->  ('delhi', 1000) ('hyderabad', 400) 
kolkata ->  ('lucknow', 800) ('hyderabad', 600) 
hyderabad ->  ('mumbai', 400) ('kolkata', 600) 
shimla ->  ('manali', 300) 
manali ->  ('shimla', 300) ('laddakh', 450) 
laddakh ->  ('manali', 450) 


Shortest distance from kolkata to delhi : 1300
Shortest distance from kolkata to lucknow : 800
Shortest distance from kolkata to mumbai : 1000
Shortest distance from kolkata to kolkata : 0
Shortest distance from kolkata to hyderabad : 600
Shortest distance from kolkata to shimla : No route found
Shortest distance from kolkata to manali : No route found
Shortest distance from kolkata to laddakh : No route found

"""

from collections import defaultdict


class MyGraph4:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, src, dst, wt):
        if dst not in self.adj_list[src]:
            self.adj_list[src].append((dst, wt))
        # if src not in self.adj_list[dst]:
        #     self.adj_list[dst].append((src, wt))

    def remove_edge(self, src, dst):
        if dst in self.adj_list[src]:
            self.adj_list[src].remove(dst)

        # if src in self.adj_list[dst]:
        #     self.adj_list[dst].remove(src)

    def print(self):
        for src, neigbours in self.adj_list.items():
            print("{} :".format(src), end=" ")
            for neigbour in neigbours:
                print(neigbour, end=" ")
            print()

    def make_union(self, vertex1, vertex2, parent):
        if parent[vertex1] <= parent[vertex2]:
            parent[vertex2] = vertex1
            parent[vertex1] -= 1
        else:
            parent[vertex1] = vertex2
            parent[vertex2] -= 1

    def find_parent(self, vertex, parent):
        while parent[vertex] >= 0:
            vertex = parent[vertex]
        return vertex

    # NOTE: This method only works for undirected graph
    def is_cycle(self):
        parent = defaultdict(lambda : -1)
        for src, neighbours in self.adj_list.items():
            for neighbour, wt in neighbours:
                src_parent = self.find_parent(src, parent)
                nei_parent = self.find_parent(neighbour, parent)
                if src_parent == nei_parent:
                    print(parent)
                    return True
                self.make_union(src_parent, nei_parent, parent)
        print(parent)
        return False

    # kruskal | Minimum spanning tree | only for undirected graphs
    # T : O(ElogE) + O(E(LogV))
    # Sorting of edges takes O(ELogE) time.
    # After sorting, we iterate through all edges and apply the find-union algorithm.
    # The find and union operations can take at most O(LogV) time. So overall complexity is O(ELogE + ELogV) time.
    # This ques will be asked mostly for undirected graph
    def kruskal(self):

        parent = [-1] * self.num_vertices

        # Create edge list
        edge_list = []
        for src, neighbours in self.adj_list.items():
            for neighbour, wt in neighbours:
                edge_list.append((src, neighbour, wt))

        # Sort edge list
        edge_list.sort(key=lambda x:x[2])
        print(edge_list)

        valid_edges = []
        valid_edges_taken = 0
        mst_cost = 0
        for src, dst, wt in edge_list:

            src_parent = self.find_parent(src, parent)
            dst_parent = self.find_parent(dst, parent)
            if src_parent == dst_parent:
                continue

            mst_cost += wt
            valid_edges.append((src, dst, wt))
            print("Taking: ", src, dst, wt)

            self.make_union(src_parent, dst_parent, parent)

            valid_edges_taken += 1
            if valid_edges_taken == self.num_vertices - 1:
                break

        print(parent)
        print(valid_edges)
        print(mst_cost)
        return False

    # dijkstra | Single source shortest path | Greedy algorithm
    # T: O((V + E)*logV)
    # S: O(V)+O(V)=O(2V) = O(V) visited + heap
    # Greedy Algorithm
    # Does not work for negative weights
    def dijkstra(self):
        distance = defaultdict(lambda: float('inf'))
        visited = defaultdict(lambda: False)

        src = 1
        distance[src] = 0
        heap = [(distance[src], src)]
        heapq.heapify(heap)

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)
            visited[current_vertex] = True
            for neighbour_vertex, neighbour_distance in self.adj_list[current_vertex]:
                if not visited[neighbour_vertex]:
                    distance[neighbour_vertex] = min(distance[neighbour_vertex], current_distance + neighbour_distance)
                    heapq.heappush(heap, (distance[neighbour_vertex], neighbour_vertex))

        for dst, dis in distance.items():
            print("Vertex {} is at {} distance from {}".format(dst, dis, src))

    # Bellman ford | Single source shortest path | DP algorithm
    # T: O((v-1)*E)
    # Works for negative weights
    # Does not work if there is a negative weight cycle.
    # The first iteration guarantees to give all shortest paths which are at most 1 edge long.
    # The second iteration guarantees to give all shortest paths which are at most 2 edges long.
    # The V-1 th iteration guarantees to give all shortest paths which are at most V - 1 edges long.
    def bellman_ford(self):
        # Create edge list
        edge_list = []
        for src, neighbours in self.adj_list.items():
            for neighbour_vertex, neighbour_distance in neighbours:
                edge_list.append((src, neighbour_vertex, neighbour_distance))

        distance = defaultdict(lambda: inf)

        src = 1
        distance[src] = 0

        i = 0
        while i < self.num_vertices - 1:
            for src, dst, dis in edge_list:
                if distance[dst] > distance[src] + dis:
                    distance[dst] = distance[src] + dis
            i += 1

        for dst, dis in distance.items():
            print("Vertex {} is at {} distance from {}".format(dst, dis, src))

    # Recursive DFS
    # T: O(V+E)
    # Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.
    # Space Complexity: O(V).
    # There can be atmost V elements in the stack. So the space needed is O(V).
    def is_path_exists_utils(self, src, dst, visited, path):

        path.append(src)
        if src == dst:
            return True

        # Visit the node
        visited[src] = True

        # Explore its neighbours
        for neighbour, wt in self.adj_list[src]:
            if not visited[neighbour]:
                if self.is_path_exists_utils(neighbour, dst, visited, path):
                    return True

        path.pop()
        return False

    # Iterative DFS
    # T: O(V+E)
    # Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.
    # Space Complexity: O(V).
    # There can be atmost V elements in the stack. So the space needed is O(V).
    def is_path_exists_utils2(self, src, dst, visited, path):

        if src == dst:
            return True

        stack = []
        # Visit the node
        visited[src] = True
        stack.append(src)

        while stack:
            vertex = stack.pop()

            if vertex == dst:
                return True

            for neighbour, wt in self.adj_list[vertex]:
                if not visited[neighbour]:
                    stack.append(neighbour)
                    visited[neighbour] = True

        return False

    # Iterative BFS
    # Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.
    # Space Complexity: O(V).
    def is_path_exists_utils3(self, src, dst, visited):
        if src == dst:
            return True

        q = deque()
        q.append(src)
        visited[src] = True

        while q:
            vertex = q.popleft()
            if vertex == dst:
                return True
            for neighbour, wt in self.adj_list[vertex]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    visited[neighbour] = True
        return False

    # This ques will be mostly asked for directed graph
    # because in undirected graph, from each node we can reach to any other node.
    # if src and dst are not in same connected component then only, dst can not be reached from src
    def is_path_exists(self, src, dst):
        path = []
        visited = defaultdict(lambda: False)
        if self.is_path_exists_utils(src, dst, visited, path):
            return True, path
        return False, path

    # Recursive DFS
    def find_all_paths_utils(self, src, dst, visited, path, result):

        # Visit the node
        path.append(src)
        visited[src] = True

        if src == dst:
            result.append(path.copy())
        else:
            # Explore its neighbours
            for neighbour, wt in self.adj_list[src]:
                if not visited[neighbour]:
                    self.find_all_paths_utils(neighbour, dst, visited, path, result)

        # Unvisit the node
        path.pop()
        visited[src] = False

    # Iterative DFS
    def find_all_paths_utils2(self, src, dst):
        path = []
        result = []
        stack = []

        visited = defaultdict(lambda: False)

        stack.append(src)
        visited[src] = True

        while stack:
            vertex = stack.pop()
            # Visit the node
            path.append(vertex)
            if vertex == dst:
                result.append(path.copy())
            else:
                # Explore its neighbours
                for neighbour, wt in self.adj_list[vertex]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        stack.append(neighbour)

            # Unvisit the node
            #path.pop()
            #visited[src] = False

        return result

    def find_all_paths(self, src, dst):
        result = self.find_all_paths_utils2(src, dst)
        if result:
            return True, result
        return False, []


# Undirected weighted graph
class Graph5:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, src, dst, wt):
        if dst not in self.adj_list[src]:
            self.adj_list[src].append((dst, wt))
        # if src not in self.adj_list[dst]:
        #     self.adj_list[dst].append((src, wt))

    def remove_edge(self, src, dst):
        if src in self.adj_list and dst in self.adj_list[src]:
            self.adj_list[src].remove(dst)
        if dst in self.adj_list and src in self.adj_list[dst]:
            self.adj_list[dst].remove(src)

    def print_graph(self):
        for src, neighbours in self.adj_list.items():
            print("{} -> ".format(src), end=" ")
            for neighbour in neighbours:
                print(neighbour, end=" ")
            print()

    def dfs_utils(self, start_vertex, visited):
        print(start_vertex, end=" ")
        visited[start_vertex] = True
        for neighbour, wt in self.adj_list[start_vertex]:
            if not visited[neighbour]:
                self.dfs_utils(neighbour, visited)

    def dfs(self):
        print()
        visited = defaultdict(lambda: False)
        for src in list(self.adj_list.keys()):
            if not visited[src]:
                self.dfs_utils(src, visited)
        print()

    def bfs_utils(self, start_vertex, visited):
        q = deque()
        q.append(start_vertex)
        visited[start_vertex] = True

        while q:
            vertex = q.popleft()
            print(vertex, end=" ")
            for neighbour, wt in self.adj_list[vertex]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    visited[neighbour] = True

    def bfs(self):
        print()
        visited = defaultdict(lambda : False)
        for src in list(self.adj_list.keys()):
            if not visited[src]:
                self.bfs_utils(src, visited)
        print()

    # DFS recursive
    def path_exists_utils(self, src, dst, visited):
        if src == dst:
            return True
        visited[src] = True
        for neighbour, wt in self.adj_list[src]:
            if neighbour == dst:
                return True
            if not visited[neighbour]:
                if self.path_exists_utils(neighbour, dst, visited):
                    return True
        return False


    # DFD iterative
    def path_exists_utils2(self, src, dst):

        if src == dst:
            return True
        visited = defaultdict(lambda : False)
        stack = [src]
        visited[src] = True

        while stack:
            vertex = stack.pop()
            if vertex == dst:
                return True
            for neighbour, wt in self.adj_list[vertex]:
                if not visited[neighbour]:
                    stack.append(neighbour)
                    visited[neighbour] = True
        return False

    # BFS iterative
    def path_exists_utils3(self, src, dst):
        if src == dst:
            return True

        visited = defaultdict(lambda : False)
        q = deque()

        q.append(src)
        visited[src] = True

        while q:
            vertex = q.popleft()
            if vertex == dst:
                return True
            for neighbour, wt in self.adj_list[vertex]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    visited[neighbour] = True

        return False

    def path_exists(self, src, dst):
        visited = defaultdict(lambda : False)
        if self.path_exists_utils3(src, dst):
            return True
        return False

    def find_paths_utils(self, src, dst, visited, path, result):

        # Visit the node
        path.append(src)
        visited[src] = True

        if src == dst:
            result.append(path.copy())
        else:
            # Explore its neighbours
            for neighbour, wt in self.adj_list[src]:
                if not visited[neighbour]:
                    self.find_paths_utils(neighbour, dst, visited, path, result)

        # Unvisit the node
        path.pop()
        visited[src] = False

    # Iterative DFS
    def find_path_utils2(self, src, dst):

        path = []
        result = []
        visited = defaultdict(lambda: False)
        stack = []

        path.append(src)
        stack.append((src, path))
        visited[src] = True

        while stack:
            vertex, p = stack.pop()
            if vertex == dst:
                result.append(p)
            else:
                for neighbour, wt in self.adj_list[vertex]:
                    if not visited[neighbour]:
                        new_path = p.copy()
                        new_path.append(neighbour)
                        stack.append((neighbour, new_path))
                        visited[neighbour] = True


        return result


    def find_paths(self, src, dst):
        path = []
        result = []
        visited = defaultdict(lambda : False)
        #self.find_paths_utils(src, dst, visited, path, result)
        result = self.find_path_utils2(src, dst)
        return result

    # To find shortest path
    def dijkistra(self):

        start_vertex = 1
        distances = defaultdict(lambda : float('inf'))
        distances[start_vertex] = 0
        heap = [(0, start_vertex)]
        heapq.heapify(heap)
        visited = defaultdict(lambda : False)

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)
            visited[current_vertex] = True
            for neighbour_vertex, neighbour_distance in self.adj_list[current_vertex]:
                if not visited[neighbour_vertex]:
                    distances[neighbour_vertex] = min(distances[neighbour_vertex], current_distance + neighbour_distance)
                    heapq.heappush(heap, (distances[neighbour_vertex], neighbour_vertex))

        for dst, distance in distances.items():
            print("{} to {} : {}".format(start_vertex, dst, distance))

    # T: O((V-1)*E)
    def bellman_ford(self):
        edge_list = []
        for src, neighbours in self.adj_list.items():
            for dst, wt in neighbours:
                edge_list.append((src, dst, wt))
        print(edge_list)
        start_vertex = 1
        distances = defaultdict(lambda : float('inf'))
        distances[start_vertex] = 0

        i = 0

        while i < self.num_vertices - 1:
            for src, dst, w in edge_list:
                if distances[dst] > distances[src] + w:
                    distances[dst] = distances[src] + w
            i += 1


        for dst, distance in distances.items():
            print("{} to {} : {}".format(start_vertex, dst, distance))

    # https://www.youtube.com/watch?v=wU6udHRIkcc&list=PLL_Rr0-eLWmOMccWWU5CL_suJRjGaZdxq
    def make_union(self, vertex1, vertex2, parent):
        if parent[vertex1] <= parent[vertex2]:
            parent[vertex2] = vertex1
            parent[vertex1] -= 1
        else:
            parent[vertex1] = vertex2
            parent[vertex2] -= 1

    def find_parent(self, vertex, parent):
        while parent[vertex] > -1:
            vertex = parent[vertex]
        return vertex

    # O(E) + O(E*logE)
    def kruskal(self):

        edge_list = []
        for src, neighbours in self.adj_list.items():
            for dst, wt in neighbours:
                edge_list.append((wt, src, dst))

        print(edge_list)

        parent = defaultdict(lambda: -1)

        heapq.heapify(edge_list)
        min_cost = 0
        valid_edges = []

        count = 0
        while edge_list:
            wt, src, dst = heapq.heappop(edge_list)
            src_parent = self.find_parent(src, parent)
            dst_parent = self.find_parent(dst, parent)
            if src_parent == dst_parent:
                continue
            min_cost += wt
            valid_edges.append((wt, src, dst))
            print("Taking src {} dst {} wt {}".format(src, dst, wt))

            self.make_union(src_parent, dst_parent,parent)
            count += 1

            if count == self.num_vertices -1:
                break


def Anagrams(words):
    myhash = defaultdict(list)
    for w in words:
        myhash[''.join(sorted(w))].append(w)
    return myhash


class ListNode:
    def __init__(self, data, pnext=None):
        self.val = data
        self.next = pnext

# T: O(n)
def get_numbers(l):
    if not l:
        return 0

    pcurr = l
    n = 0
    while pcurr:
        n = n * 10 + pcurr.val
        pcurr = pcurr.next

    return n


def subLinkedList(l1, l2):
    n1 = get_numbers(l1)
    n2 = get_numbers(l2)
    r = abs(n1 - n2)
    print(r)
    dummy = ListNode(-1)
    pcurr = dummy
    while r:
        v = r % 10
        pcurr.next = ListNode(v)
        pcurr = pcurr.next
        r = r // 10

    return dummy.next


def print_list(l):
    if not l:
        return None
    print()
    pcurr = l
    while pcurr:
        print(pcurr.val , end=' ')
        pcurr = pcurr.next
    print()


def subsets(i, candidates, subset, result):

    if len(subset) == 4:
        result.append("".join(subset.copy()))
        return

    if i == len(candidates):
        return

    # Include char
    subset.append(candidates[i])
    subsets(i, candidates, subset, result)

    # Do not include char
    subset.pop()
    subsets(i + 1, candidates, subset, result)



def combinationSum(candidates, index, result):

    if index == len(candidates):
        subsets(0, candidates, [], result)
        return

    for i in range(index, len(candidates)):
        candidates[0], candidates[i] = candidates[i], candidates[0]
        combinationSum(candidates, index+1, result)
        candidates[0], candidates[i] = candidates[i], candidates[0]


def main():
    candidates = ['N', 'P', 'R']
    result = []
    combinationSum(candidates, 0, result)
    print(result)
    return
    l1 = ListNode(0)
    l1.next = ListNode(0)
    l1.next.next = ListNode(0)
    l1.next.next.next = ListNode(8)
    print_list(l1)

    l2 = ListNode(1)
    l2.next = ListNode(2)
    print_list(l2)

    l = subLinkedList(l1, l2)
    print_list(l)
    return




    print(Anagrams(["act","god","cat","dog","tac"]))
    return
    edge_list = [
        (1, 2, 2),
        (1, 3, 4),
        (2, 3, 1),
        (2, 4, 7),
        (3, 5, 3),
        (5, 4, 2),
        (4, 6, 1),
        (5, 6, 5)
    ]

    g5 = Graph5(6)

    for u, v, w in edge_list:
        g5.add_edge(u, v, w)

    g5.print_graph()
    g5.dfs()
    g5.print_graph()
    g5.bfs()
    g5.print_graph()

    print(g5.path_exists(6, 1))

    print(g5.find_paths(1, 6))

    g5.dijkistra()
    g5.bellman_ford()
    g5.kruskal()
    return
    g4 = MyGraph4(4)
    # g4.add_edge(0, 1, 50)
    # g4.add_edge(1, 2, -20)
    # g4.add_edge(2, 3, 70)
    # g4.add_edge(3, 0, 60)
    # g4.add_edge(0, 3, 60)
    # g4.add_edge(2, 4, -100)
    # g4.add_edge(3, 4, 35)

    # g4.add_edge(1, 2, 4)
    # g4.add_edge(1, 4, 5)
    # g4.add_edge(4, 3, 3)
    # g4.add_edge(3, 2, -10)

    g4.add_edge(1, 2, 1)
    g4.add_edge(2, 3, 1)
    g4.add_edge(2, 4, 1)
    g4.add_edge(3, 1, 1)
    g4.add_edge(3, 4, 1)

    g4.print()
    #print(g4.is_cycle())
    #print(g4.kruskal())
    #print(g4.dijkstra())
    #print(g4.bellman_ford())
    #print(g4.is_path_exists(1, 4))
    print(g4.find_all_paths(1, 4))
    return


    # g3= Graph3()
    #
    # g3.add_edge("delhi", "lucknow", 500)
    # g3.add_edge("delhi", "mumbai", 1000)
    # g3.add_edge("lucknow", "kolkata", 800)
    # g3.add_edge("mumbai", "hyderabad", 400)
    # g3.add_edge("kolkata", "hyderabad", 600)
    #
    # g3.add_edge("shimla", "manali", 300)
    # g3.add_edge("manali", "laddakh", 450)
    # g3.print()
    # #g3.remove_edge("delhi", "mumbai")
    # #g3.print()
    #
    # g3.dfs("kolkata")
    # g3.bfs("kolkata")
    #
    # print(g3.is_edge("mumbai", "hyderabad"))
    #
    # g3.shortest_path("kolkata")
    # return


    g2= Graph2(7)
    g2.print()

    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(0, 3)
    g2.add_edge(1, 3)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)

    g2.add_edge(4, 5)
    g2.add_edge(4, 6)
    g2.add_edge(5, 6)
    g2.print()

    print(g2.is_cycle_present())
    #return

    src, dst = 0, 2
    print("No of paths from {} to {}: ".format(src, dst))
    print(g2.count_paths(src, dst))
    return
    g2.remove_edge(1, 3)
    g2.print()

    g2.dfs(1)
    g2.bfs(1)
    return

    g = Graph(7)
    g.print()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 3)

    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.print()
    # g.remove_edge(1, 3)
    # g.print()

    g.dfs(1)
    g.bfs(1)

    print(g.is_edge(1, 5))


if __name__ == '__main__':
    main()
