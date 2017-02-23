print("cd /D S:")

n= 0

while(n <=158):
    print('Icacls S::"\%folder%" /inheritance:d /remove:g domain\user1 /grant:r "%user%":(IO)(CI)F /T ')
    n+=1
