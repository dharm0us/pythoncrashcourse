car = 'bmw'
print(car == 'bmw')
print(car == 'audi' or car == 'santro')
a = 3
print(car == "bmw" and a == 3)
cars = ["santro","xing"]
print(car in cars) # list containment
print(car not in cars) # not in list

if a == 4:
  print("4")
elif a == 2:
  print("2")
else:
  print(a)

k = True
j = False
print(k,j)

l = []
if not l:
  print("empty list")

if a < 5: #   styling note, it's better than a<5
  print("yes")