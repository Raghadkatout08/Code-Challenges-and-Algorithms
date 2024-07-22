class HashTable:
    def __init__(self):
        """
        Initializes an empty hash table using a set.
        """
        self.table = set()

    def put(self, key):
        """
        Adds the given key to the hash table.
        
        :param key: The key to be added to the hash table.
        """

        self.table.add(key)

    def find(self, key):
        """
        Checks if the given key exists in the hash table.
        
        :param key: The key to check for existence in the hash table.
        :return: True if the key exists, otherwise False.
        """
        return key in self.table

def first_repeated_word(s):
    """
    Finds the first repeated word in a given string using a hash table.
    
    :param s: The input string.
    :return: The first repeated word or 'No Repetition' if no word is repeated.
    """
    hash_table = HashTable()
    words = s.split()

    for word in words:
        if hash_table.find(word):
            return word
        hash_table.put(word)

    return "No Repetition"

# Example usage
if __name__ == "__main__":
    Test_Case1 = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    Test_Case2 = "I am learning programming at ASAC."

    print("Test Case 1:" , Test_Case1)
    print("Output:", first_repeated_word(Test_Case1))  # Output: ASAC

    print()

    print("Test Case 2:", Test_Case2)
    print("Output:", first_repeated_word(Test_Case2))  # Output: No Repetition
