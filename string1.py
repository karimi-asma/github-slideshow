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
for i in (0, len(s)):
    s = s[:i] + '.' + s[i:]

print (s)