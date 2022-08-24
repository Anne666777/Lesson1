pr = input('Enter your profit: ')
ex = input('and expenses: ')
if pr > ex:
    print('Well done! You have a profit!')
elif pr == ex:
    print("You went to zero")
else:
    print('You have a loss :C')
