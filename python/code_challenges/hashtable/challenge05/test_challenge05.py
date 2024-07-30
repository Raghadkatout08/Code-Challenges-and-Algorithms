from challenge05 import array_intersection

def test_basic_intersection():
    """
    Test case 1: Basic intersection.
    """
    assert array_intersection([1, 2, 2, 1], [2, 2]) == [2]

def test_multiple_intersections_with_duplicates():
    """
    Test case 2: Multiple intersections with duplicates.
    """
    assert array_intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]

def test_no_intersection():
    """
    Test case 3: No intersection.
    """
    assert array_intersection([1, 2, 3], [4, 5, 6]) == []

def test_multiple_intersections():
    """
    Test case 4: Multiple intersections.
    """
    assert array_intersection([1, 2, 2, 1, 3], [2, 2, 3, 4]) == [2, 3]

def test_single_element_intersection():
    """
    Test case 5: Single element intersection.
    """
    assert array_intersection([1], [1, 1, 1, 1]) == [1]

def test_empty_arrays():
    """
    Test case 6: Empty arrays.
    """
    assert array_intersection([], []) == []

def test_one_empty_array():
    """
    Test case 7: One empty array.
    """
    assert array_intersection([1, 2, 3], []) == []

def test_intersecting_with_empty_array():
    """
    Test case 8: Intersecting with empty array.
    """
    assert array_intersection([], [1, 2, 3]) == []

def test_identical_arrays():
    """
    Test case 9: Identical arrays.
    """
    assert array_intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3]