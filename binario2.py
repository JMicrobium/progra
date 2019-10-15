
    
N=int(input("ingrese un valor entero===>"))
div=N
cuo=0
res=0
valor=""
while div!=0:
    cuo=div//2
    res=div%2
    valor +=str(res)
    div=cuo
print(valor)
    
