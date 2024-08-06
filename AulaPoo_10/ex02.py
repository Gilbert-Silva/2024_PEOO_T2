from datetime import datetime
from datetime import timedelta


x = datetime(2024, 1, 1, 10, 30, 0)
print(x)

y = datetime(2024, 8, 6)
print(y)

z = datetime(day=31, month=12, year=2024)
print(z)

a = datetime.now()
print(a)

nasc = input("Informe sua data de nascimento (dd/mm/aaaa):")
data = datetime.strptime(nasc, "%d/%m/%Y")
print(data)

hoje = datetime.now()
tempo = hoje - data
print(tempo)
print(tempo.days)
print(tempo.days/30)
print(type(tempo))

x = datetime(2024, 2, 29)
print(x)
umdia = timedelta(days=1)
print(umdia)
x = x + umdia
print(x)
x = x + umdia
print(x)




