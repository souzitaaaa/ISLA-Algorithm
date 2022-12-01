import  array as arr

vetor = arr.array('i')

for i in range(0,20):
    num = input("Introduza o número " + str(i + 1) + ": ")
    vetor.append(int(num))

search = int(input("Introduza o número a pesquisar: "))
position = 0

for j in range(0,20):
    if vetor[j] == search:
        position = j
if position >= 0:
    print("Número", search, "encontrado na posição", position)
else:
    print("Número não encontrado")