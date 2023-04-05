# Tip 1

condition = True

if condition:
    x=1
else:
    x=0

print(x)

# instead use above try this:

condition = True

x = 1 if condition else 0

print(x)

Tip 2 (counting)

num1 = 10000000000
num2 = 100000000

total = num1 + num2

print(total)

# Instead try this:
# Underscore Doesn't effect the Output

num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f'{total:,}')                            # Use of F String  (:, just add , at the place of _(underscore))

Tip 3

f = open('test.text','r')

file_contents = f.read()

f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# Instead use a context manager as:

with open('test.text','r') as f

    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# Tip 4 Enumrate Function

names = ['Akshay','Takamura','Python','Java']

for name in names:
    print(name)

# if you want to keep the count in the list :

names = ['Akshay', 'Takamura', 'Python', 'Java']

index=0
for name in names:
    print(index,name)
    index += 1

# Better way of doing from the above example is to use Enumerate Function

names = ['Akshay', 'Takamura', 'Python', 'Java']
for index,name in enumerate(names):                    # if want to start from 1 just add (start=1) in names like:
    print(index,name)                                  # enumerate(names, start=1)

# Tip 5

Artists_names = ["Eiichiro Oda", "Takehiko Inoue", "Takeshi Obata", "Akira Toriyama", "Fumiyo Kono",]
Mangas = ["One-Piece", "Vagabond", "Death_Note", "Dragon Ball Z", "In This Corner of the World"]

for index, Artists_names in enumerate(Artists_names):
    Manga = Mangas[index]
    print(f"{Manga} art is done by {Artists_names}")


# Instead try this:   Using a zip fuction

Artists_names = ["Eiichiro Oda", "Takehiko Inoue", "Takeshi Obata", "Akira Toriyama", "Fumiyo Kono",]
Mangas = ["One-Piece", "Vagabond", "Death_Note", "Dragon Ball Z", "In This Corner of the World"]

for manga, artist_name in zip(Mangas,Artists_names):
    print(f"{manga} art is done by {artist_name}")           # Prints out Tuple

# Or can write

for value in zip(Mangas,Artists_names):
    print(value)


# Tip 6
# Packing and Unpacking

Unpacking
a,b = (1,2)

print(a)
print(b)

# Instead try:

a, b, *c, d= (1, 2, 3, 4, 5, 6, 7)                            # Using Astix

print(a)
print(b)
# print(c)
print(d)


# Tip 7

class Person():
    pass

person = Person()

person.first = "Akshay"
person.last = "Sharma"

print(person.first)
print(person.last)

# Instead try this:

class Person():
    pass

person = Person()

first_key = 'first'
first_val = "Akshay"

setattr(person, first_key, first_val)

first = getattr(person, first_key)

print(person.first)

# For Looping around in a dictionary

class Person():
    pass

person = Person()
person_info = {'first': 'Akshay', 'last': 'Sharma'}
for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)

# Instead of using above prints

class Person():
    pass

person = Person()
person_info = {'first': 'Akshay', 'last': 'Sharma'}
for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

# Tip 8 (Inputing Secret Information)

from getpass import getpass

username = input('Username: ')
password = getpass("Password: ")

print('Logging In...')

# Tip 9  (gives valids attributes methods for the object we pass in) on Command Prompt

import smtpd
help(smtpd)
from datetime import datetime
dir(datetime)
datetime.today
datetime.today()
exit()