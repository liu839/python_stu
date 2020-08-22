class MyHashSet(set):
    def __init__(self):
        super().__init__(self)
    def remove(self,k):
        if k in self:
            super().remove(k)
    def contains(self, key: int) -> bool:
        return key in self       



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)