N=str(input("agregue una letra===>"))
c=0
v=0
e=0
for n in N:
    if n=='a' or n=='A' or n=='e' or n=='E' or n=='i' or n=='I' or n=='o' or n=='O' or n=='u' or n=='U':
        n=1
        v +=n
    
    elif n!='a' and n!='A' and n!='e' and n!='E' and n!='i' and n!='I' and n!='o' and n!='O' and n!='u' and n!='U' and n!=" ":
        n=1
        c +=n
        
    elif n==" ":
        n=1
        e +=n
        
    
       
print("vocales=",v,"consonante=",c,"espacios=",e)