import os
import math

def initializare():
    # punem cuvintele in lista cuvinte
    global cuvinte
    cuvinte = open("cuvinte.txt", "r")
    cuvinte = cuvinte.readlines()
    for i in range(len(cuvinte)):
        cuvinte[i] = cuvinte[i].strip()


def incercare():
    global frecvCuvinte
    entropieMax = 0
    entropieCuv = 0
    global cuvOptim
    global cuvinte
    n = len(cuvinte)

    if n > 1:
        if n != 11454:
            # calculam entropiile cuvintelor
            for i in range(n):
                entropieCuv = 0

                # facem un dictionar cu 3^5 elemente, anume toate feedback-urile posibile
                frecv = {}
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            for m in range(3):
                                for o in range(3):
                                    frecv[str(j) + str(k) + str(l) + str(m) + str(o)] = 0

                # calculam frecventele posibilelor feedback-uri
                for j in range(n):
                    rel = ""
                    for k in range(5):
                        if cuvinte[i][k] == cuvinte[j][k]:
                            rel += "2"
                        else:
                            if cuvinte[i][k] in cuvinte[j]:
                                rel += "1"
                            else:
                                rel += "0"
                    frecv[rel] += 1

                # calculam probabilitatile feedback-urilor
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            for m in range(3):
                                for o in range(3):
                                    p = frecv[str(j) + str(k) + str(l) + str(m) + str(o)] / n
                                    if p != 0:
                                        entropieCuv += p * math.log2(1/p)
                                        entropieCuv = round(entropieCuv, 10)

                # verficam daca entropia cuvantului este mai mare decat cea maxima curenta
                if entropieCuv > entropieMax:
                    entropieMax = entropieCuv
                    cuvOptim = cuvinte[i]

        else:
            cuvOptim = "TAREI"
    else:
        cuvOptim = cuvinte[0]

    # punem cuvantul optim in cuvantOptim.txt
    cuvOptim = cuvOptim.strip()
    output = open("cuvantOptim.txt", "w")
    output.write(cuvOptim)
    output.flush()
    os.fsync(output.fileno())


def interpretare():
    global cuvinte
    global cuvOptim

    # citim feedbak-ul despre cuvantul pe care l-am trimis in feedback.txt
    feedback = open("feedback.txt", "r")
    feedback = (feedback.readlines())
    feedback = ''.join(feedback)

    if feedback == "Ati ghicit cuvantul":
        feedback.close()
    else:
        cuvinte.remove(cuvOptim)

        # eliminam toate cuvintele din lista de cuvinte care nu se potrivesc cu feedback-ul primit
        j = 0
        while j < len(cuvinte):
            for i in range(5):

                if feedback[i] == '0':
                    if cuvOptim[i] in cuvinte[j] and cuvinte[j] in cuvinte:
                        cuvinte.remove(cuvinte[j])
                        break

                elif feedback[i] == '1':
                    if cuvOptim[i] not in cuvinte[j] and cuvinte[j] in cuvinte:
                        cuvinte.remove(cuvinte[j])
                        break

                    elif cuvOptim[i] == cuvinte[j][i] and cuvinte[j] in cuvinte:
                        cuvinte.remove(cuvinte[j])
                        break

                elif feedback[i] == '2':
                    if cuvOptim[i] != cuvinte[j][i] and cuvinte[j] in cuvinte:
                        cuvinte.remove(cuvinte[j])
                        break
            else:
                j += 1
