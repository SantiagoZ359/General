# Implementa una tabla hash donde las colisiones se manejen utilizando linear probing. 
# Toma la implementación de la tabla hash que utiliza 
# encadenamiento y modifica los métodos para utilizar linear probing. 
# Mantén el tamaño máximo de arr en la tabla hash como 10.

class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.arr = [None] * size

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)

        while self.arr[index] is not None:
            index = (index + 1) % self.size

        self.arr[index] = (key, value)

    def search(self, key):
        index = self._hash(key)

        while self.arr[index] is not None:
            stored_key, value = self.arr[index]
            if stored_key == key:
                return value
            index = (index + 1) % self.size

        raise KeyError(f"Key {key} not found.")

    def delete(self, key):
        index = self._hash(key)

        while self.arr[index] is not None:
            stored_key, _ = self.arr[index]
            if stored_key == key:
                self.arr[index] = None
                return
            index = (index + 1) % self.size

        raise KeyError(f"Key {key} not found.")



hash_table = HashTableLinearProbing()

hash_table.insert(3, "A")
hash_table.insert(13, "B")
hash_table.insert(23, "C")
hash_table.insert(33, "D")

print(hash_table.search(13))  

hash_table.delete(13)
# print(hash_table.search(13))  
