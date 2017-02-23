import copy

a = [1,2]

b = [a,3]

c = copy.deepcopy(b) # shallow copy of 'b'
                    #THIS IS ANSWERING PART (iii) WITH THE EXAMPLE CODE PROVIDED IN A1

print c


a[0] = 7

b[1] = 8

print c



# THE FOLLOWING CODE BELOW IS TO ANSWER PART (iv) OF QUESTION THREE

listOne =  [[[5,6],7],9]

list_deepcopy = copy.deepcopy(listOne)

listOne [0][1] = 4



print listOne
print list_deepcopy