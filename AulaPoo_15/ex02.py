class MeuErro(Exception):
  pass

try:
  a = int(input("Informe o dividendo: "))
  b = int(input("Informe o divisor: "))
  print(a/b)
except Exception as erro:
  print(type(erro))
  print(erro)
except ValueError:
  print("Digite um inteiro válido")

x = MeuErro()
raise x



