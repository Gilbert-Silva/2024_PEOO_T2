from datetime import timedelta
from datetime import datetime

x = input("Informe a duração da música mm:ss: ")
d = x.split(":")
m = int(d[0])
s = int(d[1])
duracao = timedelta(minutes=m, seconds=s)
print(duracao)

m, s = map(int, input("Informe a duração da música mm:ss: ").split(":"))
duracao = timedelta(minutes=m, seconds=s)
print(duracao)

#int(input())
#float(input())
#datetime.strptime(input(), "%d/%m/%Y")

