Echipa Tom si Jerry
Hodivoianu Anamaria - grupa 132
Uceanu Irina Alexandra - grupa 132

Proiectul este alcatuit din 2 programe: Wordle.py si Ghicitor.py,
primul care alege cuvantul si al doilea care incearca sa il 
ghiceasca. Acestea comunica prin fisierele feedback.txt si 
cuvantOptim.txt.

Ghicitor.py calculeaza prin functia "incercare" cuvantul optim si
il scrie in fisierul cuvandOptim.txt. Wordle.py citeste incercarea si o 
interpreteaza, punand in out.txt un string format din 5 caractere
din multimea {0, 1, 2} (0-gri, 1-galben, 2-verde).

Ghicitor.py va interpreta, prin functia "interpretare",acest 
raspuns si va scoate din lista, citita in variabila "cuvinte", 
toate cuvintele care nu se potrivesc, adica cele care contin o 
litera care nu se afla in cuvantul de ghicit, cele care nu contin 
o litera care se afla in cuvantul de ghicit si cele care nu 
contin o anumita litera pe o anumita pozitie. 

In functie de noua lista, Ghicitor.py va alege noul cuvant optim.
Algoritmul prin care Wordle.py incearca sa gaseasca cuvantul 
optim, care se afla in functia "incercare", se bazeaza pe entropia
lui Shannon. Astfel, pentru fiecare cuvant din lista, algoritmul 
calculeaza probabilitatea ca acel cuvant sa returneze un anumit 
feedback, facand acest lucru pentru toate feedback-urile
posibile si o adauga in formula entropiei. 
Este ales cuvantul cu cea mai mare entropie.
Pentru alegerea primului cuvant, este folosit un dictionar, 
frecvCuvinte, care este calculat in functia "initializareFrecv". 
Este un dictionar cu toate cuvintele, ce are ca valori dictionare
cu toate cele 3^5 posibile feedback-uri si de cate ori apare 
fiecare feedback pentru un anumit cuvant, raportat la toate 
celelalte cuvinte din lista. Aceasta functie a fost importanta
pentru generarea tuturor solutiilor, insa calcularea acestui
dictionar dureaza aproximativ doua minute, asa ca a fost calculat
o singura data si apoi folosit de toate cuvintele.

Primul cuvant optim este calculat de fiecare data ca fiind
"TAREI", insa dureaza aproximativ 2 minute. De aceea am adaugat
o a doua versiune de joc, gasita in programele WordleV2.py si
GhicitorV2.py in care primul cuvant optim este deja initializat
cu "TAREI". Restul algoritmului este la fel cu cel original, insa
ruleaza intr-o secunda. 
 
In momentul in care cuvantul ales de Ghicitor.py coincide cu cel
ales de Wordle.py jocul se va termina si mesajul "Ati ghicit
cuvantul." va fi afisat in fisierul feedback.txt.

Numarul mediu de incercari este 4.32836.

In fisierul solutii.txt se afla solutiile gasite pentru fiecare
cuvant, impreuna cu numarul de incercari.

Referinte:
https://markmliu.medium.com/what-in-the-wordle-5dc5ed94fe2
https://aditya-sengupta.github.io/coding/2022/01/13/wordle.html
https://towardsdatascience.com/information-theory-applied-to-wordle-b63b34a6538e
