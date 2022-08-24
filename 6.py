pr = float(input('Enter your profit: '))
ex = float(input('and expenses: '))
profitability = pr / ex
if pr > ex:
    print(f'Well done! Profitability of revenue: {profitability}')
    em = int(input('How many employees do you have? '))
    print(f'Profit per employee: {pr / em}')
elif pr == ex:
    print("You went to zero")
else:
    print('You have a loss :C')


