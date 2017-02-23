
string_one = raw_input("please enter first string")
print string_one
string_two= raw_input("please enter second string")
string_three= raw_input("please enter third string")
string_four= raw_input("please enter fourth string")

sorted_strings = sorted([string_one, string_two, string_three, string_four], key=lambda z: z.lower())

for item in sorted_strings:
    print item
    print "\n"


print sorted_strings







# firstString = raw_input("Please enter a String ")
#
#
# print "This is the sorted ordered of all the letters: " + "".join(sorted(firstString))
#
# first_String = " ".join(''.join(sorted(word)) for word in firstString.split())
#
# print "This is the sorted ordered of all letters per word: " + " " + first_String
#
#
#
# secondString = raw_input("please enter a second String ")
#
#
# print "This is the sorted ordered of all the letters: " +  ''.join(sorted(secondString))
#
# second_String = " ".join(''.join(sorted(word)) for word in secondString.split())
#
# print "This is the sorted ordered of all letters per word: " + " " + second_String
#
#
# thirdString = raw_input("Please enter a third String ")
#
# print "This is the sorted ordered of all the letters: " +  ''.join(sorted(thirdString))
#
#
# third_String = " ".join(''.join(sorted(word)) for word in thirdString.split())
#
# print "This is the sorted ordered of all letters per word: " + " " + third_String
#
#
#
# fourthString = raw_input("Please enter a fourth String ")
#
# print "This is the sorted ordered of all the letters: " +  ''.join(sorted(fourthString))
#
# fourth_String = " ".join(''.join(sorted(word)) for word in thirdString.split())
#
# print "This is the sorted ordered of all letters per word: " + " " + fourth_String
#



# words= []
# length = str(raw_input("Please enter how many items you want in the list: "))
#
# while len(words) <= 4:
#     item = input("Enter your items to the List: ")
#     words.append(item)
#     words = sorted(words, key=str.lower)
#     print words
#     print "\n"
#



































