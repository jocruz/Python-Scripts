

keys = ['lastname', 'firstname', 'email', 'id', 'phone']



dicts = []
second_dicts = []
third_dicts = []
#intersection = []
common = []




while True:

    prompt = raw_input("Please enter which file you'd like to open: old, new, current: ")

    if prompt == "end":
        break

    if prompt == "old":

        with open("oldFile.txt") as f:
            for line in f:

                line = line.strip().split()

                d = dict(zip(keys, line))


                print d


                dicts.append(d)





    if prompt == "new":


        with open ("newFile.txt") as n:
            for line in n:

                line = line.strip().split()
                r = dict(zip(keys, line))
                print r
                second_dicts.append(r)




    if prompt == "current" :

       for x in dicts:
        if x in second_dicts:
            print x




