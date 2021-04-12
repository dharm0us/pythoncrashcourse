class Dog:
  """ Dog class """

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.breed = "default breed" # note that we set it on our own without passing in constructor
  def getDesc(self):
    return f"My name is {self.name}, age is {self.age}"
  
class SpecialDog(Dog): #inheritance
  def __init__(self, name, age):
    super().__init__(name, age) # parent constructor
    self.address = "new town" # new field in addition to parent class
  
  def getDesc(self): # method overriding
    return "special dog desc"

d = Dog("dillie", 12)
print(d.getDesc())

print(f"{d.name} is {d.age} years old")
sd = SpecialDog("willie", 13)
print(f"{sd.name} is {sd.age} years old")
print(sd.getDesc())