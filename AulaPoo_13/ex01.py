x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}

print(max(x))


print(x)
print(type(x))

print(x["RN"])
print(x["PB"])

x["AM"] = "Manaus"
x["RN"] = ["Natal", "Parnamirim"]
print(x)
print(*x)

y = [1, 2]
z = (1, 2)

print(type(y))
print(type(z))

for item in x.items(): print(item)

print(*x.keys())
print(*x.values())




