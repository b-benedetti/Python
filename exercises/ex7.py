
texto = """escolha a sua água para comprar:
(1) água mineral natural
(2) água mineral com gás
"""

opcao = input(texto)

if opcao == "1":
    valor_item = 3

elif opcao == "2":
    valor_item = 3.5

if valor_item == 0:
    print("escolha a opção 1 ou 2, por favor")

else:
    qtdade = input("quantas garrafas?")
    qtdade = int(qtdade)
    valor_total = valor_item * qtdade
    print("sua conta deu R$", valor_total)
