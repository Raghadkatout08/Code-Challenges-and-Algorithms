from challenge04 import sort_people_by_height

def test_basic_input():
    names = ["Alice", "Bob", "Charlie"]
    heights = [165, 175, 160]
    expected = ["Bob", "Alice", "Charlie"]
    assert sort_people_by_height(names, heights) == expected

def test_duplicate_heights():
    names = ["John", "Jane", "Doe", "Alice"]
    heights = [170, 165, 170, 160]
    expected = ["John", "Doe", "Jane", "Alice"]
    assert sort_people_by_height(names, heights) == expected

def test_single_element():
    names = ["Eve"]
    heights = [150]
    expected = ["Eve"]
    assert sort_people_by_height(names, heights) == expected

def test_all_heights_same():
    names = ["Sam", "Tom", "Jerry"]
    heights = [180, 180, 180]
    expected = ["Sam", "Tom", "Jerry"]  # Order should remain the same
    assert sort_people_by_height(names, heights) == expected

def test_reversed_order():
    names = ["Zack", "Amy", "Liam", "John"]
    heights = [190, 160, 175, 180]
    expected = ["Zack", "John", "Liam", "Amy"]
    assert sort_people_by_height(names, heights) == expected

def test_large_number_of_elements():
    names = ["A", "B", "C", "D", "E"]
    heights = [150, 180, 170, 160, 155]
    expected = ["B", "C", "D", "E", "A"]
    assert sort_people_by_height(names, heights) == expected

def test_empty_lists():
    names = []
    heights = []
    expected = []
    assert sort_people_by_height(names, heights) == expected