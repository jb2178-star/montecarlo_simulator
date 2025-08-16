class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)] #initialize table with empty buckets (chaining)
        self.count =0 #number of key-value pairs stored
    def _hash(self, key):
        return hash(key) % self.size #compute index using built-in hash and modulo table size

    def set(self, key, value):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value)) #key not found, insert new
        self.count += 1
        if self.count / self.size > 0.7: #resize if load factor > 0.7
            self._resize(self.size * 2)

    def get(self, key):
        idx = self._hash(key) #find bucket index
        for k, v in self.table[idx]:
            if k == key: #search for key in bucket
                return v #return value if found
        return None #return none if key not found
    
    def items(self):
        for bucket in self.table: #iterate over all buckets
            for k, v in bucket: #yield key-value pair
                yield k, v

    def delete(self, key):
        idx = self._hash(key)  #find bucket index
        bucket = self.table[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:  #search for key in bucket
                del bucket[i]
                self.count -= 1
                return True
        return False
    def keys(self):
        keys_list = []
        for bucket in self.table: #iterate all buckets
            for k, _ in bucket: #collect all keys
                keys_list.append(k)
        return keys_list #return list
    def _resize(self, new_size):
        old_items = list(self.items())  #get all current items
        self.size = new_size
        self.table = [[] for _ in range(new_size)]
        self.count = 0
        for key, value in old_items:
            self.set(key, value)  #reinsert items into the new table
    def __len__(self):
        return self.count
  