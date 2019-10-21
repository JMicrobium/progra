N=int(input("-"))
N +=1
suma=0
fact=0
for i in range(1,N+1):
    suma=fact+suma
    fact=1
    for j in range(1,i+1):
        fact=j*fact
print(suma)