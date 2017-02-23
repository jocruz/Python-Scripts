def main():
  # compute average, standard deviation of a list of numbers
  print "enter values to be analyzed, use -1 to end list"
  data = []  # out list of values starts empty

  num = input("enter your number:")
  while num != -1:
    data.append(num)  # add value to the data list
    num = input("enter your number:")

  avg = average(data)
  print 'average of data values is ', avg

  std = stddev(data, avg)
  print 'standard deviation is ', std


def average(data):
  # compute average of a list of numbers
  sum = 0.0
  for x in data:
      sum = sum + x
  if len(data) == 0: return 0
  else: return sum / len(data)


import math

def stddev(data, avg):
  # compute standard deviation of values from average
  diffs = 0.0
  for x in data:
    xdiff = x - avg   # compute difference from average
    diffs = diffs + xdiff * xdiff  # squared
  if len(data) == 0: return 0
  else: return math.sqrt(diffs/len(data))


main()
