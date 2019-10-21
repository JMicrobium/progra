from math import pow
deltasABC=[50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
velocidadesA=[2586.206896551724, 2743.3628318584074, 2782.608695652174, 2920.353982300885, 3008.849557522124, 3125.0, 3243.243243243243, 3394.4954128440368, 3689.3203883495144, 3979.591836734694, 4255.31914893617, 4606.741573033708, 4941.176470588235, 4942.528735632184, 5116.279069767442, 5294.117647058823, 5542.168674698795, 5529.411764705882, 5647.058823529412, 5444.444444444445, 5882.35294117647, 5930.232558139535, 5909.090909090909, 5955.056179775281, 6750.0, 6875.0, 6829.268292682927, 7037.037037037037, 7160.493827160494, 7108.433734939759, 7894.736842105263, 8243.243243243243, 8493.150684931506, 8750.0, 9014.084507042253, 9154.929577464789, 9295.774647887323, 9305.555555555557, 9714.285714285714, 9718.30985915493, 10000.0, 10289.855072463768, 10588.235294117647, 10895.5223880597, 11044.776119402984, 11194.029850746268, 11515.151515151516, 11666.666666666666, 11818.181818181818, 11969.69696969697, 12307.692307692309, 12272.727272727272, 12615.384615384615, 12968.75, 13125.0, 13709.677419354839, 13870.967741935485, 14262.295081967211, 14666.666666666666, 14833.333333333332, 15000.0]
velocidadesB=[3409.090909090909, 3604.6511627906975, 3720.9302325581393, 3793.1034482758623, 3908.0459770114944, 4268.292682926829, 4337.349397590361, 4683.544303797468, 4871.794871794872, 4936.708860759493, 5128.205128205129, 5324.675324675324, 5384.615384615385, 5657.894736842105, 6027.397260273972, 6081.081081081081, 6388.888888888889, 6527.777777777778, 6857.142857142857, 7205.882352941177, 7462.686567164179, 7727.272727272727, 7878.787878787879, 8030.30303030303, 8181.818181818182, 8461.538461538463, 8750.0, 9047.619047619048, 9354.83870967742, 9076.923076923078, 9523.809523809523, 10701.754385964912, 11698.11320754717, 10677.966101694916, 11228.070175438595, 11818.181818181818, 12000.0, 12641.509433962265, 12592.592592592591, 13018.867924528302, 12962.962962962962, 12909.09090909091, 13846.153846153848, 13518.518518518518, 13703.703703703703, 13636.363636363638, 13818.18181818182, 13275.862068965518, 13684.210526315788, 14107.142857142857, 13793.103448275862, 14210.526315789473, 15185.185185185184, 15961.538461538463, 16153.846153846154, 16346.153846153848, 17200.0, 15263.157894736842, 16000.000000000002, 17115.384615384617, 16666.666666666664]
velocidadesC=[2419.3548387096776, 2583.3333333333335, 2711.8644067796613, 2972.972972972973, 3119.266055045872, 3271.028037383178, 3529.411764705882, 3700.0, 4175.824175824176, 4482.758620689656, 4597.701149425287, 4712.64367816092, 5000.0, 5243.902439024389, 5432.098765432099, 5555.555555555556, 5609.756097560975, 6184.210526315789, 6315.789473684211, 6125.0, 6329.113924050633, 6800.0, 7123.287671232877, 7260.273972602739, 7605.633802816901, 7746.478873239436, 7777.777777777778, 8142.857142857143, 8405.797101449276, 8939.39393939394, 9090.90909090909, 9242.424242424242, 9841.269841269841, 10000.0, 10000.0, 10317.460317460318, 10645.161290322581, 10806.451612903225, 11147.540983606557, 11500.0, 11475.409836065573, 11833.333333333334, 12203.389830508475, 12372.881355932204, 12758.620689655174, 12931.034482758621, 13103.44827586207, 13508.771929824561, 13928.57142857143, 13859.649122807017, 14285.714285714286, 14727.272727272728, 14909.09090909091, 14821.428571428572, 15849.056603773584, 16037.735849056604, 15925.925925925925, 16111.11111111111, 16603.77358490566, 17115.384615384617, 17647.05882352941]
s=0
l=0
A=[(i-20) for i in deltasABC]
s=sum(A)
B=[(i**2) for i in A]
l=sum(B)
f=sum(velocidadesA)
g=sum(velocidadesB)
h=sum(velocidadesC)
Q=[(i*j) for i,j in zip(A,velocidadesA)]
q=sum(Q)
W=[(i*j) for i,j in zip(A,velocidadesB)]
w=sum(W)
E=[(i*j) for i,j in zip(A,velocidadesC)]
e=sum(E)

"alpha"

a0=(((s*q)-(l*f)))/((s**2)-(61*(l)))

a1=((s*f)-(61*q))/((s**2)-(61*l))

"beta"

b0=((s*w)-(l*g))/(((s**2)-(61*l)))

b1=((s*g)-(61*w))/((s**2)-(61*l))

"Gammma"

c0=((s*e)-(l*h))/((s**2)-(61*l))

c1=((s*h)-(61*e))/((s**2)-(61*l))
#de aqui hacia arriba es copia de "ecuaciones de regresion"

"deltas"

al= [(a0+(a1*x)-y) for x,y in zip(A,velocidadesA)]#error entre el ajuste y los datos
bl= [(b0+(b1*x)-y) for x,y in zip(A,velocidadesB)]#error entre el ajuste y los datos
cl= [(c0+(c1*x)-y) for x,y in zip(A,velocidadesC)]#error entre el ajuste y los datos


Al=[(i**2) for i in al]#valores de las listas al cuadrado
Bl=[(i**2) for i in bl]#valores de las listas al cuadrado
Cl=[(i**2) for i in cl]#valores de las listas al cuadrado

As=0
Bs=0
Cs=0

As=sum(Al)#sumatoria de los valores al cuadrado
Bs=sum(Bl)#sumatoria de los valores al cuadrado
Cs=sum(Cl)#sumatoria de los valores al cuadrado

af=(As/60)**(1/2)
bf=(Bs/60)**(1/2)
cf=(Cs/60)**(1/2)

print(af,bf,cf)
