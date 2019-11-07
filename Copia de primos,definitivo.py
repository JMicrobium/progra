"""for i in range(1,n+1):
    if n%i==0:
        a=("divisor {}".format(n/i))
        v +=1
    elif n%i!=0:
        a =("parte entera {}".format(n//i))
        b +=1
    #print(a) #si se quieren ver todos los divisores del numero, sacar el GATO del print
if b!=(n-2):
    print("El numero no es primo")
elif b==(n-2):
    print('El numero es primo')"""

def pri(n):
    b=0
    for i in range(1,n+1):
        if n%i!=0:
            a =(n//i)
            b +=1
    if b==(n-2):
        return (i)

N=int(input("===>"))
b=0.0
for i in range(1,N+1,2):
    for j in range(1,i,2):
        if i%j==0:
            pri(i)
            if pri(i)!=None:
                print(pri(i))
            
            
            
        
            
                
                
            #el valor se repite la misma cantidad de veces como divisores posea el numero, por ende, si no se repite, es primo.
            