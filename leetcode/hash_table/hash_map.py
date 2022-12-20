# Design Hash map


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = [-1] * 1000000
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.d[key] = value

        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.d[key]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.d[key] = -1


if __name__ == "__main__":
	# Your MyHashMap object will be instantiated and called as such:
	key, value = 2, 1
	obj = MyHashMap()
	obj.put(key,value)
	param_2 = obj.get(key)
	obj.remove(key)
