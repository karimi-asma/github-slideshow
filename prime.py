number = int (input('Please enter the number: '))
c = 0
for i in range (1,number) : 
    if (number % i) == 0:
        c = c +1
if c == 1 :
    print ('prime')
else:
    print ('not prime')