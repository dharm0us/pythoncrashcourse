cars = ["santro", "astra", "i10", "i20"]
print(cars)
print(cars[0].title())
cars.append("verna")
print(cars)
cars.insert(1,"nexa")
print(cars)
print(cars.pop())
print(cars.pop(1))
cars.remove("santro")
print(cars)
del(cars[1])
print(cars)
cars = ["santro", "astra", "i10", "i20"]
cars.sort() #permanent sort
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ["santro", "astra", "i10", "i20"]
print(sorted(cars)) #temp sort
print(cars)
cars.reverse()
print(cars)
print(len(cars))
print(cars[-2])
######################
#more list stuff
###############
for car in cars:
  print(f"{car.title()} is good!")
for i in range(1,5):
  print(i)

numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print(min(even_numbers))
print(max(even_numbers))
print(sum(even_numbers))
# list comprehension - for loop and list creation combined
squares = [value**2 for value in range(1, 11)] # notice no colon
print(squares)
# list slicing - first index inc, second index ex - same as range function
print(cars)
print(cars[0:2])
# first index 0 by default, second index = len - 1 by default
print(cars[:2])
print(cars[1:])
# slice with negative first index, last 2 items here
print(cars[-2:])
print(cars[:-2]) #neg second index which is exclusive, so all items before the second from last item will be printed
print(cars[-3:-1])
print(cars[-1:-3])#empty since the indexing isn't proper
cars1 = cars # reference assignment, no copying of the list
cars.append("nano")
print(cars1)
print(cars)
cars2 = cars[:] # new list created
cars.append("alto")
print(cars2)
print(cars)

# Tuple - an immutable list
cart = ("nano", "alto")
print(cart)
#cart[0] = "new nano" #error
cart = ("i10", "i20") #but assigning a new tuple is fine
print(cart)
