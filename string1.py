s = input()
s = s.lower()
for letter in s:
    if letter == 'a':
        s = s.replace('a' , '')
    if letter == 'e':
        s = s.replace('e', '')
    if letter == 'o':
        s = s.replace('o', '')
    if letter == 'i':
        s = s.replace('i', '')
    if letter == 'u':
        s = s.replace('u', '')
s='.' + '.'.join(s)

print (s)