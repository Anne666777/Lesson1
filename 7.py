f_km = float(input("Enter km in first day: "))
l_km = float(input("Enter km in last day: "))
days = 1
km = f_km
print(f'1 day: {f_km}')
while km < l_km:
    f_km = 0.1 * f_km + f_km
    days += 1  # days = days + 1
    km += f_km
    km = float('{:.2f}'.format(km))
    print(f'{days} day: {km} km')
print(f'You will reach the goal on {days} day')
