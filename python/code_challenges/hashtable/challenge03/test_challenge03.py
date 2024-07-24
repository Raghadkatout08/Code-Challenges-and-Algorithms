import pytest
from challenge03 import HashTable

@pytest.fixture
def hash_table():
    return HashTable()

def test_sum_of_unique_element_no_unique(hash_table):
    nums = [1, 1, 2, 2, 3, 3]
    assert hash_table.sum_of_unique_element(nums) == 0

def test_sum_of_unique_element_all_unique(hash_table):
    nums = [1, 2, 3, 4, 5]
    assert hash_table.sum_of_unique_element(nums) == 15

def test_sum_of_unique_element_single_element(hash_table):
    nums = [5]
    assert hash_table.sum_of_unique_element(nums) == 5

def test_sum_of_unique_element_multiple_unique(hash_table):
    nums = [1, 2, 2, 3, 3, 4, 4, 5, 6]
    assert hash_table.sum_of_unique_element(nums) == 12  

def test_sum_of_unique_element_empty_list(hash_table):
    nums = []
    assert hash_table.sum_of_unique_element(nums) == 0

def test_sum_of_unique_element_duplicates(hash_table):
    nums = [2, 2, 2, 3, 4, 4, 5]
    assert hash_table.sum_of_unique_element(nums) == 8  