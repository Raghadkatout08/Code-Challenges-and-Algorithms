import pytest
from challenge01 import Graph

@pytest.fixture
def setup_graph():
    """Fixture to set up a graph with nodes and edges for testing."""
    graph = Graph()

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
    
    return graph

def test_breadth_first(setup_graph):
    """Test breadth-first traversal from node 'A'."""
    graph = setup_graph
    expected_result = ['A', 'B', 'C', 'E', 'D', 'F', 'G', 'H', 'I', 'K']
    bfs_result = graph.breadth_first("A")
    assert bfs_result == expected_result

def test_breadth_first_single_node():
    """Test breadth-first traversal starting from a node with no edges."""
    single_node_graph = Graph()
    single_node = single_node_graph.add_node("Z")
    expected_result = ['Z']
    bfs_result = single_node_graph.breadth_first("Z")
    assert bfs_result == expected_result

def test_breadth_first_nonexistent_node(setup_graph):
    """Test breadth-first traversal starting from a non-existent node."""
    graph = setup_graph
    expected_message = "Node with value 'X' does not exist in the graph."
    bfs_result = graph.breadth_first("X")
    assert bfs_result == expected_message

def test_empty_graph():
    """Test breadth-first traversal on an empty graph."""
    empty_graph = Graph()
    expected_message = "Node with value 'A' does not exist in the graph."
    bfs_result = empty_graph.breadth_first("A")
    assert bfs_result == expected_message 

def test_breadth_first_disconnected_graph():
    """Test breadth-first traversal in a disconnected graph."""
    disconnected_graph = Graph()
    v1 = disconnected_graph.add_node("A")
    v2 = disconnected_graph.add_node("B")
    v3 = disconnected_graph.add_node("C")
    disconnected_graph.add_edge(v1, v2)
    # Node "C" is disconnected
    expected_result = ['A', 'B']
    bfs_result = disconnected_graph.breadth_first("A")
    assert bfs_result == expected_result