"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

N=int(input("ingrese valor===>"))
for i in range(1,N+1,2):
    if N%i==0:
        if i==3 or i==5 or i==7 or i==11 or i==13 or i==17 or i==19 or i==23 or i==29:
            print(i)