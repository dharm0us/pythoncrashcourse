def list_modifier(l):
  l.append("added")

l = []
list_modifier(l)# pass list by ref
print(l)
list_modifier(l[:])# pass by val, no change to original list
print(l)

def variable_args(*arglist):
  print(arglist[0], arglist[2])

variable_args("a", "b", "c")

def positional_plus_variable_args(first, *variable):
  print(first)
  print(variable[2])

positional_plus_variable_args(16, "a", "b", "c")

def variable_keyword_args(**vka):
  print(vka['name'])

variable_keyword_args(name="dharam")

def mixit(first, **varied):
  print(first)
  print(varied['name'])

mixit("who is", name="dharam")
