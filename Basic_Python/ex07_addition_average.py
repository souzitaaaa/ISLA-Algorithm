a =int(input("Insira quantos números irá inserir:"))
soma = 0
b = 0
while (b < a):
    c =int(input("Insira um número:"))
    soma += c
    b += 1
media = soma / a
print("A soma desses números dá: ", soma)
print("A média desses números é: ", media)