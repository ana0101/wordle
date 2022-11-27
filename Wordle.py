from Ghicitor import *
import random
import os

# deschidem fisierul cu toate cuvintele
cuvinte = open('cuvinte.txt', 'r')
cuvinte = cuvinte.readlines()

# deschidem fisierul in care dam feedback despre cuvantul ghicit
output = open('feedback.txt', 'w')
n = len(cuvinte)

for i in range(len(cuvinte)):
    cuvinte[i] = cuvinte[i].strip()

initializare()
initializareFrecv()

# alegem cuvantul de ghicit
cuv = random.choice(cuvinte)
print("cuvantul de ghicit este",cuv)


while True:
    incercare()
    # citim incercarea ghicitorului
    cuvant = open('cuvantOptim.txt', 'r')
    cuvant = cuvant.readlines()
    cuvant = ''.join(cuvant)

    print("cuvantul ghicit este", cuvant)

    # comparam incercarea si cuvantul de ghicit, punand informatile intr-un fisier feedback.txt
    if cuv == cuvant:
        output.seek(0)
        output.truncate()
        output.writelines("Ati ghicit cuvantul")
        output.flush()
        os.fsync(output.fileno())
        break
    else:
        result = ['-1', '-1', '-1', '-1', '-1']

        for i in range(5):
            if cuvant[i] == cuv[i]:
                result[i] = '2'

        for i in range(5):
            if cuvant[i] in cuv:
                if cuvant[i] != cuv[i]:
                    result[i] = '1'
            else:
                result[i] = '0'

        result = "".join(result)
        output.seek(0)
        output.truncate()
        output.writelines(result)
        output.flush()
        os.fsync(output.fileno())
        interpretare()

