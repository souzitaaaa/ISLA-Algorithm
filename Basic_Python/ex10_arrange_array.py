import array as arr
from datetime import datetime
#import random

start_time = datetime.now()
vetor = arr.array('i')
dimensao = 10

#This was for a side exercise the professor proposed
#for i in range(dimensao):
#    num = random.randint(0,500)
#    print(num, end = "\n")
#    vetor.append(int(num))

for i in range(dimensao):
    num = input("Introduza o número " + str(i + 1) + ": ")
    vetor.append(int(num))
    print(vetor, end = "\n")
    print(vetor[i], sep = " ", end = "\n\n")

print(end ="\n")
print("Organização da Array:")

for k in range(dimensao):
    for j in range(dimensao - 1):
        if vetor[j] > vetor[j + 1]:
            hold = vetor[j]
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = hold
            print(vetor)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
