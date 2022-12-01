a = int(input("Insira um número inteiro: "))
b = int(input("Insira um número inteiro: "))
c = int(input("Insira um número inteiro: "))
if a > b and a > c:
    print("O maior número é", a)
if b > a and b > c:
    print("O maior número é", b)
if c > a and c > b:
    print("O maior número é", c)