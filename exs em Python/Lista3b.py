#EX 1 ==========================================
n = int(input())
t = 0
for i in range(int(n)):
    if i * (i+1) * (i+2) == n:
        print("É triangular")
        t = 1
        print(i, i+1, i+2)
        break
        
if t == False:
    print("Número não triangular")

#EX 2 ==========================================
