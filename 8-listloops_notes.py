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
