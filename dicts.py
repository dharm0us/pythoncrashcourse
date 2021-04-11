d = {'color' : "green", 'points': 5}
print(d['color'], d['points'])
d['speed'] = 9
print(d)
del(d['color'])
print(d)
# safely access value in case of missing key
# print(d['color']) # keyError
print(d.get('color'))
print(d.get('color', 'missing color'))
d['color'] = 'assigned'
print(d.get('color', 'missing color'))

for key,value in d.items(): # iterae dict
  print(f"for {key} value is {value}")

for key in d.keys(): # iterae dict keys only
  print(f"for {key}")
# OR simply
for key in d: # default behavior
  print(f"for {key}")
# iterate values
for val in d.values():
  print(f"val is {val}")
# using set to get distinct vals
d['new'] = 'assigned'
print(d.values())
print(set(d.values()))
# set init
testset = {"a", "a", "b"} # sets also use braces similar to dicts but without key value pairs
print(testset)
