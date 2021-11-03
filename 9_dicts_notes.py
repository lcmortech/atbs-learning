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
