H=int(input("====>"))
M=int(input("====>"))
S=int(input("====>"))
tiempo=0
for i in H:
    tiempo=i*60*60
    for j in M:
        tiempo=tiempo+(j*60)
        for k in S:
            tiempo=k+tiempo
            print(tiempo)
