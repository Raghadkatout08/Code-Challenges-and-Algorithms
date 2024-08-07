class Node:
    def __init__(self, value= None):
        """
        Initialize a Node with a given value.

        Args:
        value (str): The value of the node.
        """
        self.value = value

    def __str__(self):
        """
        Return the string representation of the Node's value.
        
        Returns:
        str: The value of the node.
        """
        return self.value
    
class Edge:
    def __init__(self, vertex):
        """
        Initialize an Edge that connects to a given vertex.

        Args:
        vertex (Node): The node that this edge points to.
        """
        self.vertex = vertex

    def __str__(self):
        """
        Return the string representation of the Edge's vertex.
        
        Returns:
        str: The value of the vertex that this edge points to.
        """
        return f"{self.vertex}"


class Graph:
    def __init__(self):
        """
        Initialize an empty graph with an adjacency list.
        """
        self.adj_list = {}

    def add_node(self, value):
        """
        Add a new node to the graph with the given value.

        Args:
        value (str): The value to be assigned to the new node.
        
        Returns:
        Node: The newly created node.
        """
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex
    
    def add_edge(self, node1, node2):
        """
        Add an edge between two nodes in the graph.

        Args:
        node1 (Node): The first node in the edge.
        node2 (Node): The second node in the edge.
        
        Returns:
        str: An error message if a node does not exist; otherwise, None.
        """
        if node1 not in self.adj_list:
            return "This Node Does Not Exist"
        if node2 not in self.adj_list:
            return "A Node Does Not Exist"
        
        edge1 = Edge(node2)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1)
        self.adj_list[node2].append(edge2)

    def breadth_first(self, start_value):
        """
        Perform breadth-first traversal starting from a node with the given value.

        Args:
        start_value (str): The value of the starting node.
        
        Returns:
        list: A list of node values in the order they are visited.
        str: An error message if the starting node does not exist.
        """
        start_node = None
        for node in self.adj_list.keys():
            if node.value == start_value:
                start_node = node
                break

        if start_node is None:
            return f"Node with value '{start_value}' does not exist in the graph."

        visited = set()
        queue = [start_node]
        bfs_result = []

        while queue:
            current_node = queue.pop(0)
            if current_node not in visited:
                visited.add(current_node)
                bfs_result.append(current_node.value)
                # Add neighbors to the queue
                for edge in self.adj_list[current_node]:
                    if edge.vertex not in visited:
                        queue.append(edge.vertex)

        return bfs_result
    
    def __str__(self):
        """
        Return the string representation of the graph's adjacency list.
        
        Returns:
        str: A formatted string showing each node and its edges.
        """
        result = "Graph Structure:\n"
        for node, edges in self.adj_list.items():
            edge_list = ' -> '.join(str(edge) for edge in edges)
            result += f"{node}: {edge_list}\n"
        return result
    

# Example Usage 

graph = Graph()

# Add nodes
v1 = graph.add_node("A")
v2 = graph.add_node("B")
v3 = graph.add_node("C")
v4 = graph.add_node("D")
v5 = graph.add_node("E")
v6 = graph.add_node("F")
v7 = graph.add_node("G")
v8 = graph.add_node("H")
v9 = graph.add_node("I")
v10 = graph.add_node("K")

# Add edges

graph.add_edge(v1, v2)
graph.add_edge(v1, v3)
graph.add_edge(v1, v5)
graph.add_edge(v2, v4)
graph.add_edge(v3, v6)
graph.add_edge(v4, v5)
graph.add_edge(v5, v6)
graph.add_edge(v5, v7)
graph.add_edge(v6, v8)
graph.add_edge(v6, v9)
graph.add_edge(v7, v8)
graph.add_edge(v8, v10)
graph.add_edge(v9, v10)

# Print graph
print(graph)

# Perform BFS
result = graph.breadth_first("A")
print("Breadth First Result:", result)