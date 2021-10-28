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
