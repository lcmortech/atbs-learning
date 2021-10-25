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
