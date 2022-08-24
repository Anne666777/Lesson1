num = int(input('Enter a number greater the 10: '))
a = -1
while num > 10:
    b = num % 10
    num //= 10
    if b > a:
        a = b
print(f'{a} is the largest number')

