


data = ''
# lol = 'data-notes="'

with open("landscapes_viewsource.html") as openfile:  #open the file from the document
    for line in openfile: #for every line in the openfile
        for part in line.split(): #turn it into a list
            if 'data-notes="' in part: #if "data-notes=" exists in the string

                    data += str(part) #store it



print data

print "\n\n"


result = ''
end = -1
try:
    while True:
        start = data.index('data-notes="', end+1) #if it starts at data-notes=
        end = data.index('>', start) # and ends here at >
        result += data[start:end+1] #then add what ever is inbetween

except ValueError:
    pass

print(result)

print "\n\n"


# for z in data:
#     if 'data-notes="' in data:
#



print "\n\n"






second_data =  map(int, filter(None, ''.join(map(lambda x: (x.isdigit() and x or ' '), result)).split(' '))) # Join
#them together by making sure it is a digit

# print second_data
# sorted(second_data)
# print second_data
# lol = list(reversed(second_data))
#
# print lol
#


#
sorted_data = sorted(second_data, key=int, reverse=True)
#
#
print sorted_data

high_notes = []
resp = "The top five notes in landscapes_viewsource.html are: "



for item in sorted_data[0:5]:
    high_notes.append(item)

while True:             # Loop continuously
    question = raw_input('Please enter the name of the name of a page source file: ')   # Get the input
    if question == "landscapes_viewsource.html":       # If it is a blank line...
        print resp
        print high_notes
        break


# rdata = data.replace("data-notes=", "")
# secondr = rdata.replace('"', '')
# thirdr = rdata.replace(">", " ")
# thirdr = rdata.replace('"', ''  )

# splitdata =  [int(k) for k in secondr.split(',')]


# print eval(thirdr)



