foutput = open("announce_output.html", "w")

lol = ""
with open('announce.html') as fp:
    for line in fp:

        lol += str(line)


for n in lol:
    if "<span>" and "</span>" in lol:
        r = lol.replace("<span>", "")
        n = r.replace("</span>", "")


foutput.write(n)
foutput.close()



# f = open('Q1-input.html', 'r')
# fout = open("Q1-output.html", "w")
#
# line = f.readline()
# print line # I wrote this print statement so when the code runs you can see what is happening before any changes.
#
#
#
# openSpan = "<span>"
# closeSpan = "</span>"
# rOpen = ""
# rClose = ""
# k = ""
#
#
# for line in f:
#
#         rOpen = line.replace(openSpan, "")
#
#
#         rClose = rOpen.replace(closeSpan, "")
#         print rClose
#
#
# print rClose # Similar to above, I wanted to print out the final result to show in the console the after changes.
#
#
#
# fout.write(rClose)
#
# fout.close()
#
# f.close()
#
#



