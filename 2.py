t = int(input("Enter the time in seconds:"))
h = str(t//3600)
m = (t//60) % 60
s = t % 60
if m < 10:
    m = '0'+str(m)
else:
    m = str(m)
if s < 10:
    s = '0'+str(s)
else:
    s = str(s)
print(f'{h}:{m}:{s}')
