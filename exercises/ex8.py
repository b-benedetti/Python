#faça um programa que receba 4 alturas usando um laço de repetição
# e realize a soma dessas alturas

soma = 0
qtde_entradas = 4

while qtde_entradas > 0:
    altura = input("Digite a altura: ")
    altura = float(altura)
    soma += altura 
    qtde_entradas -=1  

print("a soma das alturas resulta em: ", soma)