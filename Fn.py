i=int(input("ingrese posición====>"))
i=i+1
Fn=(1/((5)**(1/2)))*((((1+(5)**(1/2))/2)**i)-(((1-((5)**(1/2)))/2)**i))
suma=0
if Fn%2!=0:
    suma +=Fn
    print(suma)