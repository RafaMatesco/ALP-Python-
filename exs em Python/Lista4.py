#EXERCICIO 1 =====================================================================
import random

lista = []

for y in range(0,10):
    valorRand = random.randint(0, 100)
    lista.append(valorRand)

for x in range(0,10):
    for index, item in enumerate(lista):
        if lista[x] < item:
            aux = item
            lista[index] = lista[x]
            lista[x] = aux

print(lista)         
print(f"Menor: {lista[0]}\nMaior: {lista[-1]}")
input()

#EXERCICIO 2 =====================================================================
import random

lista = []
listaPAR = []
listaIMPAR = []

for y in range(0,20):
    valorRand = random.randint(0, 100)
    lista.append(valorRand)
    
for item in lista:
    if item % 2 == 0:
        listaPAR.append(item)
    else:
        listaIMPAR.append(item)
        
print(lista, listaPAR, listaIMPAR)
input()

#EXERCICIO 3 =====================================================================
import random

vetor1 = []
vetor2 = []
vetor3 = []

for y in range(0,10):
    rand = random.randint(0, 100)
    vetor1.append(rand)
    
    rand = random.randint(0, 100)
    vetor2.append(rand)
    
for x in range(0,20):
    if x % 2 == 0:
        vetor3.append(vetor1[int(x/2)])
    else:
        vetor3.append(vetor2[int(x/2)])

print(vetor1)
print(vetor2)
print(vetor3)
input()

#EXERCICIO 4 =====================================================================
statement = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''

caracteres_especiais = '()\.,:;!?"'
for c in caracteres_especiais:
    statement = statement.replace(c, "")

statement = statement.lower()
statementList = statement.split()

letras_python = "python"
palavras_filtradas = []
for word in statementList:
    if word[0] in letras_python or word[-1] in letras_python:
        palavras_filtradas.append(word)
        
print(palavras_filtradas)

#EXERCICIO 5 =====================================================================
statement = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''

caracteres_especiais = '()\.,:;!?"'
for c in caracteres_especiais:
    statement = statement.replace(c, "")

statement = statement.lower()
statementList = statement.split()

letras_python = "python"
palavras_filtradas = []
for word in statementList:
    if len(word) > 4:
        for letter in word:
            if letter in letras_python:
                palavras_filtradas.append(word)
                break
        
print(palavras_filtradas)