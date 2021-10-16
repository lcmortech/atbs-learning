spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
#continue immediately restarts the loop, so it never gets to the print statement
