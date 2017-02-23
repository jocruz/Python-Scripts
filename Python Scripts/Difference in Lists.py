

def difference(x,y): #i
     return list( set(x)-set(y))

def union (a,b): #ii
   return a + list(set(b) - set(a))

#iii
firstList = []
length = int(raw_input("Please enter how many items you want in the list: "))

while len(firstList) < length:
    item = input("Enter your items to the List: ")
    firstList.append(item)
    print firstList

secondList = []

s_length= int(raw_input("Please enter how many items you want in the second list: "))

while len(secondList) < s_length:
    item = input("Enter your items to the List: ")
    secondList.append(item)
    print secondList

print "The difference of both lists are as follows: "
print difference(firstList,secondList)

print "\n\n"


print union(firstList,secondList)
