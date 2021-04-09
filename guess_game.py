import random
i = 1
j = 99
guess = random.randint(i , j)
print (guess)
answer = input ('Is that number correct? (b,k,d) ')
while answer != 'd':
    if answer == 'b':
        i = guess
    if answer == 'k':
        j = guess
    guess = random.randint(i , j)
    print (guess)
    answer = input ('Is that number correct? ')
print ('WOWWWW, you found the number, Great Job!!!')