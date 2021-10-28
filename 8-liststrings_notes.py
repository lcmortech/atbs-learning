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
# \ allows you to continue the line
