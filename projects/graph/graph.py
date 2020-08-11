"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Initialize a queue
        q = Queue()
        # Initialize a set of visited nodes
        visited = set()
        # Add the root node to the queue
        q.enqueue(starting_vertex)
        # Initialize final list
        visitList = []
        # While there are still items left in the queue
        while q.size() > 0:
            # V is equal to the first element in the queue
            v = q.dequeue()
            # If we have not already logged that node
            if v not in visited:
                # Add it to the visited set
                visited.add(v)
                # Print that node/vertex value
                print(v)
                # For each node in the neighboring nodes
                for next_vert in self.get_neighbors(v):
                    # Add the next vertex to the queue
                    q.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Initialze stack
        s = Stack()
        # Initialize visited set
        visited = set()
        # Place the starting node/vertex on the top of the stack
        s.push(starting_vertex)
        # initialize visit list
        visitList = []
        # while there is still items in the stack
        while s.size() > 0:
            # V equals the top value of the stack
            v = s.pop()
            # If we haven't seen this vertex/node before
            if v not in visited:
                # add it to our visited set
                visited.add(v)
                # print that vertex
                print(v)
                # for the next vertex in the list of neighbors
                for next_vert in self.get_neighbors(v):
                    # make the next vertex the top of the stack
                    s.push(next_vert)



    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Fix Python weirdness of initializing mutable default parameters
        if visited is None:
            # Set of visited values
            visited = set()
        # Add the root/starting vertex to the visited set
        visited.add(starting_vertex)
        print(starting_vertex)
        # For each neighboring vertex
        for neighbor in self.vertices[starting_vertex]:
            # Check if that neighbor vertex has been visited
            if neighbor not in visited:
                # Recurse on that neighbor vertex
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Initialize queue and visited set
        q = Queue()
        visited = set()
        # Make the starting vertex the first value in the queue
        q.enqueue([starting_vertex])
        # While there are still objects in the queue
        while q.size() > 0:
            # the path will be equal to the front value in the queue
            path = q.dequeue()
            # V equals the last value in the path
            v = path[-1]
            # If we havent seen that value yet
            if v not in visited:
                # Check if that value IS the destination
                if v == destination_vertex:
                    # If so, return the shortest path
                    return path
                # Add that value to the visited set
                visited.add(v)
                # For the next node/vertex in list of neighbors
                for next_vert in self.get_neighbors(v):
                    # the new path will be a list
                    new_path = list(path)
                    # and we'll add the next vertex/node to the end of the list
                    new_path.append(next_vert)
                    # now we'll add the new path values to the back of the queue
                    q.enqueue(new_path)

        return None # "Path not found."


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Initialize stack and visited set
        s = Stack()
        visited = set()
        # Make the starting vertex the first value in the stack
        s.push([starting_vertex])
        # While there are still objects in the stack
        while s.size() > 0:
            # the path will be equal to the top value in the stack
            path = s.pop()
            # V equals the last value in the path
            v = path[-1]
            # If we havent seen that value yet
            if v not in visited:
                # Check if that value IS the destination
                if v == destination_vertex:
                    # If so, return the shortest path
                    return path
                # Add that value to the visited set
                visited.add(v)
                # For the next node/vertex in list of neighbors
                for next_vert in self.get_neighbors(v):
                    # the new path will be a list
                    new_path = list(path)
                    # and we'll add the next vertex/node to the end of the list
                    new_path.append(next_vert)
                    # now we'll add the new path values to the top of the stack
                    s.push(new_path)

        return None # "Path not found."


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Fix Python weirdness of initializing mutable default parameters
        if visited is None:
            visited = set()
        # Fix Python weirdness of initializing mutable default parameters
        if path is None:
            path = []
        # Add starting vertex to visited set
        visited.add(starting_vertex)

        # Makes a copy of path and append the starting vertex
        path = path + [starting_vertex]
        # Line above is equivalent to:
        '''
        path = list(path) #Makes a copy of path
        path.append(starting_vert)
        '''

        # If we've made it to the destination vertex
        if starting_vertex == destination_vertex:
            # Return the shortest path
            return path
        # Otherwise, for each neighboring vertex
        for neighbor in self.get_neighbors(starting_vertex):
            # Check if we have visited that neighbor vertex
            if neighbor not in visited:
                # If not, recurse on that neighbor
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
