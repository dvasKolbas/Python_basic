class MyDict(dict):
  def get(self, key):
      value = super(MyDict, self).get(key)
      if value == None:
          return 0
      return value

dct = MyDict({1:2, 2:3, 3:4})
print(dct.get(4))