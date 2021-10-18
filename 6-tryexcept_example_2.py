print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lotta cats!')
    else:
        print('Not that many cats...')
except ValueError:
    print('Please enter numeric value.')
