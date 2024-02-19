# num = 1
# while (num <= 40):
#     print(num)
#     num += 1
# print("Fim da contagem", num)

# nome: None
# while True:
#     print ("Digite o seu nome, ou pressione o x para parar:")
#     nome = input()
#     if nome == "x" or nome == "X":
#         break
#     print(f"Bem vindo, {nome}")
# print("Até logo!")

#algoritimo para o controle de saque diário
cliente = None
numero_da_conta = None
valor_a_ser_descontado = None
valor_estabelecido = 1000, "kz"
codigo_pessoal: None
data = None
valor_na_conta = None

ed = {"Elvis": 200, "Agostinho": 400}

codigo_pessoal = (input("Digite o seu código pessoal: "))
cliente = (str(input("Cliente: ")))
numero_da_conta = (str(input("Número da conta: ")))
valor_na_conta = (str(input("Saldo disponível: ")))
print(f"O seu saldo é de: {ed}")
valor_a_ser_descontado = (float(input("Valor a ser descontado: ")))
data = (str(input("Data: ")))
if (valor_a_ser_descontado <= 1000):
      print("Por favor agurde, equanto o sistema verifica...")
      input("Confirme a sua senha para concluir: ")
      print("O valor foi descontado. Obrigado!")
      print(f"Referência: \n Nome do Cliente: {cliente}  \n Número da conta: {numero_da_conta} \n Valor debitado: {valor_a_ser_descontado} \n D7685ata: {data}")

else:
    print("Valor não autorizado!" )
    print("Consulte as normas da sua Empresa!")


