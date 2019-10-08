N=int(input("ingrese un numero====>"))
suma=0
for i in range(1,N):
    
    if N%i==0:
        suma +=i
    elif N%i!=0:
        n=N
        
print("el valor {} es un número perfecto".format(suma))
print("el valor {} NO es un número perfecto".format(n))

        
        