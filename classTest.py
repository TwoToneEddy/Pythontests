import sys

class Person:
  def __init__(self, name, age):

    self.errLogFlile = sys.argv[1]
    self.repoLocation = sys.argv[2]
    self.logFileDir = sys.argv[3]
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("Hello my name is " + self.errLogFlile)
    print("Hello my name is " + self.repoLocation)
    print("Hello my name is " + self.logFileDir)

p1 = Person("John", 36)
p1.myfunc()