deltasB=[ 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
tiemposB=[ 0.0088, 0.0086, 0.0086, 0.0087, 0.0087, 0.0082, 0.0083, 0.0079, 0.0078, 0.0079, 0.0078, 0.0077, 0.0078, 0.0076, 0.0073, 0.0074, 0.0072, 0.0072, 0.0070, 0.0068, 0.0067, 0.0066, 0.0066, 0.0066, 0.0066, 0.0065, 0.0064, 0.0063, 0.0062, 0.0065, 0.0063, 0.0057, 0.0053, 0.0059, 0.0057, 0.0055, 0.0055, 0.0053, 0.0054, 0.0053, 0.0054, 0.0055, 0.0052, 0.0054, 0.0054, 0.0055, 0.0055, 0.0058, 0.0057, 0.0056, 0.0058, 0.0057, 0.0054, 0.0052, 0.0052, 0.0052, 0.0050, 0.0057, 0.0055, 0.0052, 0.0054]
B=[(i-20) for i in deltasB]
velocidadesB=[k/j for k,j in zip(B,tiemposB)]
print("'velocidadesB':",velocidadesB)