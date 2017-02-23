n=2
statement = ":NEXTITEM"
while (n <= 25):
    print(":NEXTITEM",n)
    print("start /wait ")
    print ("IF %ERRORLEVEL% == 0 goto", statement,n+1)
    print("timeout /T 700 ")
    n+=1

