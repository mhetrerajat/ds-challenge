# Design a Hash set


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = 10
        self.d = {k:[] for k in range(1, self.bucket+1)}
        
    def _get_hash_key(self, key):
        return key % self.bucket


    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashed_key = self._get_hash_key(key)
        pv = self.d.get(hashed_key, [])
        if key not in pv:
            pv.append(key)
        self.d.update({ hashed_key: pv })
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashed_key = self._get_hash_key(key)
        try:
           self.d.get(hashed_key, []).remove(key) 
        except ValueError as _:
            pass
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hashed_key = self._get_hash_key(key)
        return key in self.d.get(hashed_key, [])
        


if __name__ == "__main__":
    # Your MyHashSet object will be instantiated and called as such:
    key = 3
    obj = MyHashSet()
    obj.add(key)
    obj.remove(key)
    param_3 = obj.contains(key)
