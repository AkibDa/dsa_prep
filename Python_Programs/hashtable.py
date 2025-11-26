class HashTable:
  def __init__(self):
    self.MAX = 10
    self.arr = [[] for _ in range(self.MAX)]
    
  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
    return h % self.MAX
  
  def __setitem__(self, key, val):
    h = self.get_hash(key)
    found = False
    for idx, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0] == key:
        self.arr[h][idx] = (key, val)
        found = True
        break
    if not found:
      self.arr[h].append((key, val))
    
  def __getitem__(self, key):
    h = self.get_hash(key)
    for element in self.arr[h]:
      if element[0] == key:
        return element[1]
    
  
  def __delitem__(self, key):
    h = self.get_hash(key)
    for idx, element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][idx]
  
if __name__ == "__main__":
  t = HashTable()
  t["march 6"] = 310
  t["march 7"] = 420
  t["march 8"] = 67
  t["march 9"] = 89
  t["march 10"] = 10
  t["march 17"] = 634
  print(t.arr)
  print(t["march 6"])
  del t["march 6"]
  print(t.arr)