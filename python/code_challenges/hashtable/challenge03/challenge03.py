class HashTable:
    def __init__(self, capacity= 200):
        """
        Initializes a HashTable with the given capacity.
        
        Args:
            capacity (int): The number of buckets in the hash table.
        """
        self.capacity = capacity
        self.table = [None] * capacity 

    def _hash(self, key):
        """
        Computes the hash index for a given key.
        
        Args:
            key: The key to hash.
        
        Returns:
            int: The hash index for the key.
        """
        return hash(key) % self.capacity
    
    def put(self, key):
        """
        Inserts the given key into the HashTable. Handles collisions using chaining.
        
        Args:
            key: The key to insert into the hash table.
        """
        hashed_index = self._hash(key)
        if self.table[hashed_index] is None:
            self.table[hashed_index] = []
        self.table[hashed_index].append(key)

    def find(self, key):
        """
        Checks if the given key is present in the HashTable.
        
        Args:
            key: The key to check for presence in the hash table.
        
        Returns:
            bool: True if the key is found, otherwise False.
        """
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        if bucket is None:
            return False 
        return key in bucket 
    
    def sum_of_unique_element(self, nums):
        """
        Computes the sum of elements that appear exactly once in the given list.
        
        Args:
            nums (list): The list of integers.
        
        Returns:
            int: The sum of unique elements.
        """
        counts = HashTable(len(nums))
        for num in nums:
            counts.put(num)

        unique_sum = 0 
        seen = set()
        for num in nums:
            if num not in seen:
                if counts.find(num) and nums.count(num) == 1:
                    unique_sum += num
                seen.add(num)

        return unique_sum

# Example Usage 
if __name__ == "__main__":
    hash_table = HashTable()

    nums1 = [1, 2, 3, 2]
    print(f"input1 : {nums1}")
    print(f"output1: {hash_table.sum_of_unique_element(nums1)}") # Output: 4

    nums2 = [1, 2, 3, 4, 5]
    print(f"input2 : {nums2}")
    print(f"output2: {hash_table.sum_of_unique_element(nums2)}") # Output: 15

    nums3 = []
    print(f"input3 : {nums3}")
    print(f"output3: {hash_table.sum_of_unique_element(nums3)}") # Output: 0

    nums4 = [2, 2, 2, 3, 4, 4, 5]
    print(f"input4 : {nums4}")
    print(f"output4: {hash_table.sum_of_unique_element(nums4)}") # Output: 8