n = int(input("Informe um inteiro: "))
print(2*n)
x = [1,2,3]
print(x[2])
x = { "RN" : "Natal "}
print(x["PB"])

try:
  n = int(input("Informe um inteiro: "))
  print(2*n)
except:
  print("Valor não é um inteiro")
