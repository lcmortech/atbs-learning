Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
random.randint(1,10)
9
import random, sys, os, math
from random import *
#no longer have to call random., but still better to use normal format for readability
import sys
sys.exit()
import pyperclip
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    import pyperclip
ModuleNotFoundError: No module named 'pyperclip'
import pyperclip
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    import pyperclip
ModuleNotFoundError: No module named 'pyperclip'

================================ RESTART: Shell ================================
import pyperclip
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    import pyperclip
ModuleNotFoundError: No module named 'pyperclip'

================================ RESTART: Shell ================================
import pyperclip
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    import pyperclip
ModuleNotFoundError: No module named 'pyperclip'

================================ RESTART: Shell ================================
import pyperclip
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    import pyperclip
ModuleNotFoundError: No module named 'pyperclip'

================================ RESTART: Shell ================================
import os
os.getcwd()
'C:\\Program Files\\Python310'
import pyperclip
pyperclip.copy('Hi')
pyperclip.paste()
'Hi'

=== RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/5-example.py ==
Howdy!
Howdy!!!
Hello there.
Howdy!
Howdy!!!
Hello there.
Howdy!
Howdy!!!
Hello there.

== RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/5-example_2.py =
6

== RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/5-example_3.py =
HelloWorld

================================ RESTART: Shell ================================
cat dog mouse
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('cat', 'dog', 'mouse', sep='ABC')
catABCdogABCmouse

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/6-tryexcept_example.py
21.0
3.5
Traceback (most recent call last):
  File "C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/6-tryexcept_example.py", line 6, in <module>
    print(div42by(0))
  File "C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/6-tryexcept_example.py", line 2, in div42by
    return 42/ divideBy
ZeroDivisionError: division by zero
40/0
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    40/0
ZeroDivisionError: division by zero

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/6-tryexcept_example.py
21.0
3.5
Error: You FOOL! You NEVER divide by zero!!
None
42.0

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/6-tryexcept_example_2.py
How many cats do you have?
0
Not that many cats
hi
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    hi
NameError: name 'hi' is not defined

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/6-tryexcept_example_2.py
How many cats do you have?
hi
Traceback (most recent call last):
  File "C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/6-tryexcept_example_2.py", line 3, in <module>
    if int(numCats) >= 4:
ValueError: invalid literal for int() with base 10: 'hi'

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/6-tryexcept_example_2.py
How many cats do you have?
two
Enter numeiric value

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/6-tryexcept_example_2.py
How many cats do you have?
-2
Not that many cats...

==== RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/7-guess.py ===
Hello. What is your name?
Lauren
Well, Lauren, I am thinking of a number between 1 - 20
Take a guess.
7
Your guess is too low.
Take a guess.
9
Your guess is too high.
Take a guess.
8
You took 3 guesses.

==== RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/7-guess.py ===
Hello. What is your name?
Lauren
Well, Lauren, I am thinking of a number between 1 - 20
Take a guess.
9
Your guess is too high.
Take a guess.
5
Your guess is too high.
Take a guess.
3
Your guess is too high.
Take a guess.
2
You took 4 guesses.
Good job, Lauren! You guessed my number in 4 guesses!

================================ RESTART: Shell ================================
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
'cat'
spam[3]
'elephant'
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam [0][1]
'bat'
spam[-1]
[10, 20, 30, 40, 50]
'The ' + spam[0][1] + ' afraid.'
'The bat afraid.'
'The ' + spam[0][1] + ' is afraid.'
'The bat is afraid.'
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1:3]
['bat', 'rat']
#slice
spma = 'Hello'
spam = 'Hello'
spam = [10, 20, 30]
spam[1] = 'Hello'
spam
[10, 'Hello', 30]
spam[1:3] = ['cat', 'dog', 'mouse']
spam
[10, 'cat', 'dog', 'mouse']
spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2]
['cat', 'bat']
#omitting first of colon starts at the very beginning
spam[1:]
['bat', 'rat', 'elephant']
#omitting last of starts in that position
del spam[2]
spam
['cat', 'bat', 'elephant']
len('Hello')
5
len([1,2,3])
3
'Hello ' + 'world'
'Hello world'
[1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
'Hello' * 3
'HelloHelloHello'
[1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
list('42')
['4', '2']
list('Hello')
['H', 'e', 'l', 'l', 'o']
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
42 in ['hello', 'hi', 'howdy', 'heyas']
False
'howdy' not in ['hello', 'hi', 'howdy', 'heyas']
False
42 not in ['hello', 'hi', 'howdy', 'heyas']
True

================================ RESTART: Shell ================================

================================ RESTART: Shell ================================
for i in range (4):
    print(i)

    
0
1
2
3
range(4)
range(0, 4)
[0,1,2,3]
[0, 1, 2, 3]
for i in [0,1,2,3]:
    print(i)

    
0
1
2
3
list(range(4))
[0, 1, 2, 3]
list(range(0,100,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
#3rd parameter is step 2/step by
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + 'in supplies is: ' + supplies[i])

    
Index 0in supplies is: pens
Index 1in supplies is: staplers
Index 2in supplies is: flame-throwers
Index 3in supplies is: binders
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

    
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders
supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

    
Index 0 in supplies is: pens
Index 1 in supplies is: pens
Index 2 in supplies is: pens
Index 3 in supplies is: pens
Index 4 in supplies is: pens
Index 5 in supplies is: pens
Index 6 in supplies is: pens
Index 7 in supplies is: pens
Index 8 in supplies is: pens
Index 9 in supplies is: pens
Index 10 in supplies is: pens
Index 11 in supplies is: pens
Index 12 in supplies is: pens
Index 13 in supplies is: pens
Index 13 in supplies is: pens
SyntaxError: invalid syntax. Perhaps you forgot a comma?
supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

    
Index 0 in supplies is: pens
Index 1 in supplies is: pens
Index 2 in supplies is: pens
Index 3 in supplies is: pens
Index 4 in supplies is: pens
Index 5 in supplies is: pens
Index 6 in supplies is: pens
Index 7 in supplies is: pens
Index 8 in supplies is: pens
Index 9 in supplies is: pens
Index 10 in supplies is: pens
Index 11 in supplies is: pens
Index 12 in supplies is: pens
Index 13 in supplies is: pens
Index 14 in supplies is: pens
Index 15 in supplies is: pens
supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
    




supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

    
Index 0 in supplies is: pens
Index 1 in supplies is: pens
Index 2 in supplies is: pens
Index 3 in supplies is: pens
Index 4 in supplies is: pens
Index 5 in supplies is: pens
Index 6 in supplies is: pens
Index 7 in supplies is: pens
Index 8 in supplies is: pens
Index 9 in supplies is: pens
Index 10 in supplies is: pens
Index 11 in supplies is: pens
Index 12 in supplies is: pens
Index 13 in supplies is: pens
Index 14 in supplies is: pens
supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

    
Index 0 in supplies is: pens
Index 1 in supplies is: pens
Index 2 in supplies is: pens
Index 3 in supplies is: pens
Index 4 in supplies is: pens
Index 5 in supplies is: pens
Index 6 in supplies is: pens
Index 7 in supplies is: pens
Index 8 in supplies is: pens
Index 9 in supplies is: pens
Index 10 in supplies is: pens
Index 11 in supplies is: pens
Index 12 in supplies is: pens
Index 13 in supplies is: pens
Index 14 in supplies is: pens
Index 15 in supplies is: pens
supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

    
Index 0 in supplies is: pens
Index 1 in supplies is: pens
Index 2 in supplies is: pens
Index 3 in supplies is: pens
Index 4 in supplies is: pens
Index 5 in supplies is: pens
Index 6 in supplies is: pens
Index 7 in supplies is: pens
Index 8 in supplies is: pens
Index 9 in supplies is: pens
Index 10 in supplies is: pens
Index 11 in supplies is: pens
Index 12 in supplies is: pens
Index 13 in supplies is: pens
Index 14 in supplies is: pens
Index 15 in supplies is: pens
Index 16 in supplies is: pens
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

size, color, disposition = cat
size
'fat'
color
'orange'
disposition
'loud'
#multiple assignment feature
size, color, disposition = 'skinny', 'black', 'quiet'
#often used to make swap operations
sizze
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    sizze
NameError: name 'sizze' is not defined. Did you mean: 'size'?
size
'skinny'
color
'black'
disposition
'quiet'
a = 'AAA'
b = 'BBB'
a, b = b, a
a
'BBB'
b
'AAA'
#Augmented assignment operators
spam = 42
spam = spam + 1
spam += 1
spam
44

================================ RESTART: Shell ================================

================================ RESTART: Shell ================================
#list methods

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
0
index('hello')
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    index('hello')
NameError: name 'index' is not defined
spam
['hello', 'hi', 'howdy', 'heyas']
#method name comes after the value using a "dot"
spam.index('heyas')
3
#index method will find the list index for you
spam = ['zophie', 'pooka', 'fat-tail', 'pooka']
spam.index('pooka')
1
#will find the first instance
# the append method adds a value to the end of a list
# the insert method adds a value at any position
#the insert method uses the pos and the value for its arguments (1, 'value')
spam.append('moose')
spam.insert(1, 'chicken')
spam
['zophie', 'chicken', 'pooka', 'fat-tail', 'pooka', 'moose']
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam
['cat', 'rat', 'elephant']
#remove method removes specified value from anywhere
del spam[0]
spam
['rat', 'elephant']
# del keyword removes specified index from anywhere in the list
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
spam
['bat', 'rat', 'cat', 'hat', 'cat']
# remove mothod will only remove the first instance of a value
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam
[-7, 1, 2, 3.14, 5]

# sort method will order the list
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
# the sort method will order numbers numerically, and strings alphanetically
# the sort method also takes a keyword argument with a boolean
spam.sort(reverse=True)
spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
# the sort method CANNOT sort a list with a mix of numbers and strings
spam = [1, 2, 3, 'Alice', 'Bob']
spam.sort()
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    spam.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
# the sort method uses "ASCII-betical Order", meaning upper case characters will be sorted before lowercase characters
spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
spam.sort()
spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
# this means a capital "Z" will come before a lowercase "A"
spam = ['a', 'z', 'A', 'Z']
spam.sort()
spam
['A', 'Z', 'a', 'z']
# for true alphabetical sorting:
spam.sort(key=str.lower)
spam
['A', 'a', 'Z', 'z']

================================ RESTART: Shell ================================
list('Hello')
['H', 'e', 'l', 'l', 'o']
name = 'Zophie'
name[0]
'Z'
name[-2]
'i'
'Zo' in name
True
'xxx' in name
False
for letter in name:
    print(letter)

    
Z
o
p
h
i
e
# while lists and strings are similar, a list is mutable while strings are immutable
name = 'Zophie the cat'
name[7]
't'
# you cannot reassign letters in string
name[7] = 'x'
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    name[7] = 'x'
TypeError: 'str' object does not support item assignment





# the proper way to modify a string is to create a new one
# we do this by using the slice method
name = 'Zophie the cat'
new_name = name[0:7] + 'the' + name [8:12]
new_name
'Zophie thehe c'
name = 'Zophie a cat'
new_name = name[0:7] + 'the' + name [8:12]
new_name
'Zophie the cat'
spam = 42
cheese = spam
spam = 100
spamm
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    spamm
NameError: name 'spamm' is not defined. Did you mean: 'spam'?
spam
100
cheese
42




spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
cheese
[0, 'Hello', 2, 3, 4, 5]
spam
[0, 'Hello', 2, 3, 4, 5]
# when you assigned the list to spam, it assigned a reference in memory that got copied to cheese, which references the same list

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/8-lists_valref_example.py
[1, 2, 3, 'Hello']

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/8-lists_valref_example.py
[1, 2, 3, 'Hello']
import copy
# creates a brand new list that copies previous (similar to js 'map')


spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
cheese
['A', 42, 'C', 'D']
spam
['A', 'B', 'C', 'D']


spam = ['apples',
        'oranges',
        'bananas',
        'cats']

print('Four score and seven' + \
      'years ago')
Four score and sevenyears ago
print('Four score and seven' + 'years ago')
Four score and sevenyears ago

================================ RESTART: Shell ================================
myCat = {'six': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    myCat['size']
KeyError: 'size'
myCat['six']
'fat'
myCat['six'] = 'size'
myCat
{'six': 'size', 'color': 'gray', 'disposition': 'loud'}
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
[1,2,3] == [3,2,1]
False
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}
eggs == ham
True
'name' in eggs
True
'name' not in eggs
False
list(eggs.keys())
['name', 'species', 'age']
#returns list
list(eggs.items())
[('name', 'Zophie'), ('species', 'cat'), ('age', 8)]
#returns tuple
eggs.keys()
dict_keys(['name', 'species', 'age'])
for k in eggs.keys():
    print(k)

    
name
species
age
for v in eggs.values():
    print(v)

    
Zophie
cat
8
for i in eggs.items():
    print(i)

    
('name', 'Zophie')
('species', 'cat')
('age', 8)
#tuples are the same as lists, except they're immutable
'cat' in eggs.values()
True
if 'color' in eggs:
    print(eggs['color'])

    
eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
eggs.get('age',0)
8
eggs.get('color','')
''
picnicItems = {'apples': 5, 'cups':2}
print('I am bringing' + str(picnicItems.get('napkins',0)) + ' to the picnic.')
I am bringing0 to the picnic.
eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
if 'color' not in eggs:
    eggs[color] = 'black'

    
Traceback (most recent call last):
  File "<pyshell#275>", line 2, in <module>
    eggs[color] = 'black'
NameError: name 'color' is not defined
if 'color' not in eggs:
    eggs['color'] = 'black'

    
eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8, 'color': 'black'}
eggs.setdefault('color','orange')
'black'
eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8, 'color': 'black'}
#will not set if key already exists

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/9-dicts-charcount_ex.py
Traceback (most recent call last):
  File "C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/9-dicts-charcount_ex.py", line 8, in <module>
    print[count]
TypeError: 'builtin_function_or_method' object is not subscriptable

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/9-dicts-charcount_ex.py
{'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2, '.': 1}

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/9-dicts-charcount_ex.py
{'T': 806, 'h': 7159, 'e': 13886, ' ': 40775, 'P': 311, 'r': 7202, 'o': 9564, 'j': 160, 'c': 2431, 't': 10245, 'G': 268, 'u': 3995, 'n': 7173, 'b': 1687, 'g': 1992, 'E': 393, 'B': 335, 'k': 968, 'f': 2194, 'R': 484, 'm': 3432, 'a': 8532, 'd': 4284, 'J': 215, 'l': 5070, 'i': 6870, ',': 2628, 'y': 2828, 'W': 455, 'S': 400, 's': 6982, 'p': 1673, '\n': 4852, 'w': 2401, 'v': 1116, '.': 2731, 'Y': 110, '-': 322, 'L': 215, '/': 28, ':': 36, 'A': 621, 'D': 156, 'M': 380, '2': 25, '5': 15, '0': 19, '1': 94, '[': 97, '#': 2, ']': 94, 'N': 320, '9': 16, '7': 7, 'x': 157, '*': 32, 'O': 374, 'F': 283, 'H': 246, 'I': 984, 'C': 320, 'U': 94, 'K': 19, 'V': 53, '!': 491, '(': 38, ')': 38, '<': 2, '3': 16, 'X': 3, '>': 2, "'": 991, 'z': 33, ';': 393, 'q': 72, '?': 371, 'Q': 4, '"': 24, 'Z': 2, '8': 9, '4': 9, '6': 7, '%': 1, '@': 2, '$': 2}

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/9-dicts-charcount_ex.py
{'\n': 4852,
 ' ': 40775,
 '!': 491,
 '"': 24,
 '#': 2,
 '$': 2,
 '%': 1,
 "'": 991,
 '(': 38,
 ')': 38,
 '*': 32,
 ',': 2628,
 '-': 322,
 '.': 2731,
 '/': 28,
 '0': 19,
 '1': 94,
 '2': 25,
 '3': 16,
 '4': 9,
 '5': 15,
 '6': 7,
 '7': 7,
 '8': 9,
 '9': 16,
 ':': 36,
 ';': 393,
 '<': 2,
 '>': 2,
 '?': 371,
 '@': 2,
 'A': 621,
 'B': 335,
 'C': 320,
 'D': 156,
 'E': 393,
 'F': 283,
 'G': 268,
 'H': 246,
 'I': 984,
 'J': 215,
 'K': 19,
 'L': 215,
 'M': 380,
 'N': 320,
 'O': 374,
 'P': 311,
 'Q': 4,
 'R': 484,
 'S': 400,
 'T': 806,
 'U': 94,
 'V': 53,
 'W': 455,
 'X': 3,
 'Y': 110,
 'Z': 2,
 '[': 97,
 ']': 94,
 'a': 8532,
 'b': 1687,
 'c': 2431,
 'd': 4284,
 'e': 13886,
 'f': 2194,
 'g': 1992,
 'h': 7159,
 'i': 6870,
 'j': 160,
 'k': 968,
 'l': 5070,
 'm': 3432,
 'n': 7173,
 'o': 9564,
 'p': 1673,
 'q': 72,
 'r': 7202,
 's': 6982,
 't': 10245,
 'u': 3995,
 'v': 1116,
 'w': 2401,
 'x': 157,
 'y': 2828,
 'z': 33}

= RESTART: C:/Users/L-Diggy/Desktop/github-repos/atbs-learning/9-dicts-charcount_ex.py


================================ RESTART: Shell ================================
cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'}
allCats = []
allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'}
               )
allCats.append({'name': 'Pooka', 'age': 5, 'color': 'black'})
allCats.append({'name': 'Fat-tail', 'age': 5, 'color': 'gray'})
allCats.append({'name': '???', 'age': -1, 'color': 'orange'})
allCats
[{'name': 'Zophie', 'age': 7, 'color': 'gray'}, {'name': 'Pooka', 'age': 5, 'color': 'black'}, {'name': 'Fat-tail', 'age': 5, 'color': 'gray'}, {'name': '???', 'age': -1, 'color': 'orange'}]





the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
the_board
{'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
import pprint
pprint.pprint(the_board)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
#the dictionary acts as a data structure for the tic-tac-toe board
def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

    
print_board(the_board)
 | | 
-----
 | | 
-----
 | | 
type(42)
<class 'int'>
type('str')
<class 'str'>
type(3.14)
<class 'float'>
type(the_board)
<class 'dict'>
pprint.pprint(the_board)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
