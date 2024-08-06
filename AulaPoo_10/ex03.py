from datetime import datetime
from datetime import timedelta

x = datetime(2024, 2, 28)
print(x)
umdia = timedelta(days=1)
print(umdia)
x = x + umdia
print(x)
x = x + umdia
print(x)

print(x.day)
print(x.month)
print(x.year)

hoje = datetime.now()
print(hoje)
print(hoje.date())
print(hoje.time())
print(hoje.weekday())

s = hoje.strftime("%A, %d/%B/%Y")
print(s)
print(type(s))
s = hoje.strftime("%a, %d/%b/%y")
print(s)





