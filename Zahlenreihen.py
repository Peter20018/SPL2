# Zahlenreihe

#n = input ("Bitte n eingeben")
#n = int(n)
n = 100

for i in range(1,n+1):
    if (i<n):
       print(i, end=" < ")
    else:
        print(i)


for i in range(1,n+1):
    if(i % 2 == 0):
        print(i, end ="  gerade ")
    
