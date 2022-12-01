idade = int(input("Quantos anos têns?: "))
if idade < 65:
    dif = 65 - idade
    print("Faltam", dif, "anos para a reforma")
elif idade > 65:
    dif = idade - 65
    print("Já ultrapassou a idade da reforma em", dif, "anos")
else:
    print("Atingiu a idade da reforma.")
