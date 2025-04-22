
texto = """escolha a sua água para comprar:
(1) água mineral natural
(2) água mineral com gás
"""

opcao = input(texto)

conta = 0
if opcao == "1":
    conta = 3
elif opcao == "2":
    conta = 3.5

if conta == 0:
    print("escolha a opção 1 ou 2, por favor")
else:
    print("sua conta deu R$", conta)

