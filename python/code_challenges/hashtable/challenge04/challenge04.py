class HashTable:
    def __init__(self, capacity= 200):
        """
        Initialize the hash table with a given capacity.
        :param capacity: The number of buckets in the hash table.
        """
        self.capacity = capacity
        self.table = [None] * capacity 

    def _hash(self, key):
        """
        Compute the hash index for a given key.
        :param key: The key to hash.
        :return: The hash index.
        """
        return hash(key) % self.capacity
    
    def put(self, key):
        """
        Insert a key into the hash table.
        :param key: The key to insert.
        """
        hashed_index = self._hash(key)
        if self.table[hashed_index] is None:
            self.table[hashed_index] = []
        self.table[hashed_index].append(key)

    def find(self, key):
        """
        Check if a key exists in the hash table.
        :param key: The key to find.
        :return: True if the key exists, otherwise False.
        """
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        return bucket is not None and key in bucket
    

def sort_people_by_height(names, heights):
    """
    Sort names by their corresponding heights in descending order.
    :param names: List of names.
    :param heights: List of heights corresponding to each name.
    :return: List of names sorted by heights in descending order.
    """
    height_dict  = dict(zip(names, heights))

    sort_names = [name for name, heights in sorted(height_dict.items(), key= lambda item: item[1], reverse=True)]

    return sort_names


# Example Usage 

if __name__ == "__main__":
    hash_table = HashTable()

    names = ["Alice", "Bob", "Charlie"]
    heights = [165, 175, 160]

    sorted_names = sort_people_by_height(names, heights)
    print(f"names  : {names} \nheights: {heights}")
    print(f"sorted_names: {sorted_names}")

    print("*************************************")

    names1 = ["John", "Jane", "Doe", "Alice"]
    heights1 = [170, 165, 170, 160]

    sorted_names1 = sort_people_by_height(names1, heights1)
    print(f"names  : {names1} \nheights: {heights1}")
    print(f"sorted_names: {sorted_names1}")