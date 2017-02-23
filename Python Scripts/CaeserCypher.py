secretMessage = raw_input("Please enter message to decipher: ")


fullAlphabet = 'abcdefghijklmnopqrstuvwxyz'

key = 22 # We are choosing 22 for this program because the hint said that z is equal to v
            # The shift 4 and to the left, so 26 - 4 = 22, the key is 22
decipher = ''

#try:
#I had the try in the wrong place here, the try was moved to inside the for loop

for i in secretMessage:
        try:
            if i in secretMessage:
             decipher  += fullAlphabet[(fullAlphabet.index(i) - key) % (26)] #26 because there are 26 TOTAL letters

        except ValueError: # I kept getting a ValueError exception because the program was running into white spaces

            decipher  +=  i # If you run into a ValueError, continue on with the secret message




print "The secret message deciphered is this : " + decipher




