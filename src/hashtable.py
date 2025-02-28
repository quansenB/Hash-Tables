# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hash = self._hash_mod(key)
        self.storage[hash] = LinkedPair(key, value, self.storage[hash])



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash = self._hash_mod(key)
        if self.storage[hash].key is key:
            self.storage[hash] = self.storage[hash].next
        else:
            current = self.storage[hash]
            while current.next is not None:
                if(current.next.key is key):
                    current.next = current.next.next
                    return
                current = current.next
        print("key not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash = self._hash_mod(key)
        current = self.storage[hash]
        while current is not None:
            if current.key is key:
                return current.value
            current = current.next
        print("key not found")


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity*2
        temp = self.storage
        self.storage = [None] * self.capacity
        for element in temp:
            current = element
            while current is not None:
                self.insert(current.key, current.value)
                current = current.next
        

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
