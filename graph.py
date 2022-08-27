"""
Graph implementation
"""
from math import inf
from q import Queue
import heapq as hq


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

    # T: O(1)
    def is_edge(self, src, dst):
        if src < 0 or src >= self.vertices or dst < 0 or dst >= self.vertices:
            print("Invalid src or destination edge")
            return False
        return self.adj_matrix[src][dst] == 1


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
        self.adJ_list[dst].append(src)
        return True

    def remove_edge(self, src, dst):
        if src < 0 or src >= self.vertices or dst < 0 or dst >= self.vertices:
            print("Invalid src or destination edge")
            return False

        self.adJ_list[src].remove(dst)
        self.adJ_list[dst].remove(src)
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

    # T : O(N). Each vertex can have max N-1 as vertex as connections
    def is_edge(self, src, dst):
        if src < 0 or src >= self.vertices or dst < 0 or dst >= self.vertices:
            print("Invalid src or destination edge")
            return False
        for v in self.adJ_list[src]:
            if v == dst:
                return True
        return False


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

    # T : O(N). Each vertex can have max N-1 as vertex as connections
    def is_edge(self, src, dst):
        if src not in self.adj_list:
            return False
        for v in self.adj_list[src]:
            if v == dst:
                return True
        return False

    def get_min_distance(self, distances, visited):
        min_distance = inf
        vertex = None
        for key, value in distances:
            if not visited[key]:
                min_distance = min(min_distance, value)
                vertex = key
        return vertex

    # Dijkstra Algorithm
    # T: O(v + e)* log(v) | S: O(v)
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


def main():

    g3= Graph3()

    g3.add_edge("delhi", "lucknow", 500)
    g3.add_edge("delhi", "mumbai", 1000)
    g3.add_edge("lucknow", "kolkata", 800)
    g3.add_edge("mumbai", "hyderabad", 400)
    g3.add_edge("kolkata", "hyderabad", 600)

    g3.add_edge("shimla", "manali", 300)
    g3.add_edge("manali", "laddakh", 450)
    g3.print()
    #g3.remove_edge("delhi", "mumbai")
    #g3.print()

    g3.dfs("kolkata")
    g3.bfs("kolkata")

    print(g3.is_edge("mumbai", "hyderabad"))

    g3.shortest_path("kolkata")
    return


    g2= Graph2(7)
    g2.print()

    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(0, 3)
    g2.add_edge(1, 3)

    g2.add_edge(4, 5)
    g2.add_edge(4, 6)

    g2.print()
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
