num = input("digite um número inteiro para calcular sua raiz quadrada: ")
num = int(num)

raiz = num **(1/2) #** = elevado a
raiz = round(raiz, 3)
print("A raiz quadrada de", num, "é", raiz)