from bank import Bank


def menu():
	print('1 - Cliente')
	print('2 - Conta')
	print('3 - Quantidade de contas')
	print('0 - SAIR')
	return b.integer_values('Digite a opção desejada: ')


def menu_client():
	print('1 - Cadastra')
	print('2 - Exibir')
	print('0 - SAIR')
	return b.integer_values('Digite a opção desejada: ')


def menu_account():
	print('1 - Cadastra')
	print('2 - Exibir')
	print('3 - Sacar')
	print('4 - Deposita')
	print('5 - Transferir')
	print('6 - Histórico')
	print('0 - SAIR')
	return b.integer_values('Digite a opção desejada: ')


b = Bank()

while True:
	
	op = menu()
	b.clear()

	if op == 0:
		b.clear()
		break

	elif op == 1:
		b.clear()

		while True:
			cliente = menu_client()
			b.clear()

			if cliente == 0:
				b.clear()
				break

			elif cliente == 1:
				b.add_client()
				b.pause()

			elif cliente == 2:
				b.display_clients()
				b.pause()
	
	elif op == 2:
		b.clear()

		while True:
			conta = menu_account()
			b.clear()

			if conta == 0:
				b.clear()
				break

			elif conta == 1:
				b.add_account()
				b.pause()
				
			elif conta == 2:
				b.display_accounts()
				b.pause()

			elif conta == 3:
				b.withdraw()
				b.pause()

			elif conta == 4:
				b.deposit()
				b.pause()

			elif conta == 5:
				b.transfer()
				b.pause()

			elif conta == 6:
				b.display_extract()
				b.pause()

	elif op == 3:
		b.display_amount_account()
		b.pause()
