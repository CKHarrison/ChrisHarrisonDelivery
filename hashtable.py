"""
Hashtable module to store the package data and distance data. Comes with the ability
to insert, search, and remove items from the hashtable.
"""


class HashTable:
    """HashTable data structure for holding package and distance information"""

    # Sets up the initial size of the hashTable and sets it to a list with None which represents empty buckets
    def __init__(self):
        self.size = 64
        self.table = [None] * self.size

    # This is the hashing function which takes the id of the package and determines where to store the package
    def _create_hash(self, key):
        hash_index = key
        return hash_index % self.size

    # add a new key,value pair to the hashtable. First check if the bucket in hashtable is empty if so put the value in
    # if not, add it to the list of values that are contained in that bucket
    def add(self, key, value):
        key_hash = self._create_hash(key)
        key_value = [key, value]

        # If the value is empty at the key we want add it by creating a list holding the value and return True
        # Else add it to the list of values
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for item in self.table[key_hash]:
                if item[0] == key:
                    item[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    # Looking up a particular key and returning it, if the item in the table is None, then it is empty
    def get(self, key):
        key_hash = self._create_hash(key)
        if self.table[key_hash] is not None:
            for item in self.table[key_hash]:
                if item[0] == key:
                    return item[1]
        return None

    def print(self):
        for item in self.table:
            if item is not None:
                print(str(item[0][0]), ':', item[0][1])
