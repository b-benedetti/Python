#faça um programa que receba a quantidade indefinida de valores
#correspondentes a "saldo em conta", mas quando apertar "enter"
#sem digitar valor algum, o programa para de receber valores e exibe
#a soma de todos os valores digitados anteriormente

saldo_total = 0

while True:
    saldo = input("Digite o saldo: ")
    if saldo == "":
        break

    saldo_total += float(saldo)

print("A soma dos valores é igual a: ",saldo_total)