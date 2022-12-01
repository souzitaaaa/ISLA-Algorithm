a = int(input("Insira a primeira nota: "))
b = int(input("Insira a segunda nota: "))
c = int(input("Insira a terceira nota: "))
d = int(input("Insira a quarta nota: "))
e = int(input("Insira a quinta nota: "))
soma = a + b + c + d + e
media = soma / 5
if media < 10:
    print(media)
    print("Devias estudar mais, porque estás reprovado.")
else:
    print(media)
    print("Parabéns, passas-te!")