def fatorial(x):
    p = 1
    for k in range(1, x + 1):
        p *= k
    return(p)    

x = int(input("Informe um número para o cálculo do fatorial: "))
for k in range(1, x + 1):
    print(f"{k}! = {fatorial(k)}")
    



