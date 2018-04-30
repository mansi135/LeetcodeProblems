class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.head = Node('dummy', 'dummy')
        self.tail = Node('dummy', 'dummy')

        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.hash_map = {}

    # begginning of DLL is always oldest , this way there is no need to maintain timestamp and we achieve O(n)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        n = self.hash_map.get(key)

        if not n:
            return -1

        # remove n from where it is currently
        self._remove(n)

        # add it to the end
        self._add(n)

        return n.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash_map:  # key-overwrite case
            n = self.hash_map[key]
            self._remove(n)
            # no need to delete this key from hashmap since it will overwritten

        n = Node(key, value)
        self.hash_map[key] = n
        self._add(n)

        if len(self.hash_map) > self.capacity:  # overflow case
            first_node = self.head.next
            del self.hash_map[first_node.key]  # remove key from hash_map also
            self._remove(first_node)

    # '-' just means its an internal api and not really exposed to outside world
    def _remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):

        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


# If we want O(n), we need to store key, value in the LL, so we know which key to remove from dict
class Node:
    def __init__(self, key, value, next_node=None, prev_node=None):
        self.key = key
        self.value = value
        self.next = next_node
        self.prev = prev_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
