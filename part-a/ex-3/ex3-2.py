# Enter a string (Python is user friendly)
s=input("Enter a string:")
vowels=0
characters=0
spaces=0
s=s.lower()
vow='aeiou'


for i in s:
  if i in vow:
     vowels=vowels +1
  if (i>='a'and i<='z'):
      characters = characters+1
  else:
     spaces = spaces+1
print('Vowels:',vowels);
print('Characters:',characters);
print('White spaces:',spaces);
