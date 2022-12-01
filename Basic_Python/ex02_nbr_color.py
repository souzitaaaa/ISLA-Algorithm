a = int(input("Insira um número: "))
if  a >= 0 and a < 10:
    print("Azul")
elif a >= 10 and a < 20:
    print("Vermelho")
elif a >= 20 and a <= 30:
    print("Verde")
else:
    print("O valor não é válido")