#EXERCICIO A =====================================================================
x = 2
y = 5
if y > 8:
 y = y * 2
else:
 x = x * 2
print(x + y)

#EXERCICIO B =====================================================================
for i in range(0,9):
    if i != 3:
        for j in range(0,6):
            print('oi')


#EXERCICIO C =====================================================================
cont = 0
for x in range(1067,3628):
    if x % 2 == 0 and x % 7 == 0:
        cont += 1
        
print(cont)

#EXERCICIO D =====================================================================
cont = 0
for x in range(18644,33087):
    if '2' in str(x) and not('7' in str(x)):
        cont += 1
        
print(cont)

#EXERCICIO E =====================================================================
lista_numeros = []

cont = 0

def check_numero(numeros):
    numeroSTR = str(numeros)
        
    if numeroSTR[0] != numeroSTR[-1]: # NUMERO 3
        for i in range(5):
            if numeroSTR[i] == numeroSTR[i+1]: # NUMERO 1
                return 0
                   
        soma = sum(int(algarismo) for algarismo in numeroSTR)
        if soma % 2 == 0: # NUMERO 2
            return 1
    return 0
                
    
for n in lista_numeros:
    cont += check_numero(n)
            
            
print(cont)