def compareIndexOne (x, y):
  # compare two lists based on index value 1
  if x[1] < y[1]: return -1
  if x[1] == y[1]: return 0
  return 1

data = []
name = ''
while name != 'done':
  name = raw_input("Enter name, or 'done' to finish: ")
  if name != 'done':
    age = input("Enter age for " + name + ": ")
    data.append([name, age])

data.sort(compareIndexOne)
for element in data:
  print 'name:', element[0], ' age:', element[1]