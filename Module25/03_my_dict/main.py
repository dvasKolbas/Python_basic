class MyDict(dict):
  def get(self, key, default= 0):
      return super(MyDict, self).get(key, default)

dct = MyDict({1:2, 2:3, 3:4})
print(dct.get(4))