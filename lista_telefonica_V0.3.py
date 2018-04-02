def try_numero():
	while True:
		try:
			numero = input("Digite o numero do contato: ")
			int(numero)
		except:
			print("Formato de número não aceito. Utilize o padrão 'xxxxxxx'")
		else:
			break

	return numero

def imprimir_agenda(agenda):
	for contato in agenda:
		numeros = ""
		enderecos = ""

		for i in agenda[contato][0]:
			if i != agenda[contato][0][-1]:
				numeros = numeros+i+"; "
			else:
				numeros = numeros+i+"."

		for j in agenda[contato][1]:
			if j != agenda[contato][1][-1]:
				enderecos = enderecos+j+"; "
			else:
				enderecos = enderecos+j+"."
		print("Nome: "+contato+"\n"+"Telefone: "+numeros+"\nEndereço: "+enderecos+"\n")

def imprimir_contato(agenda):
	contato = input("Digite o nome do contato: ")
	numeros = ""
	enderecos = ""

	if contato in agenda:
		for i in agenda[contato][0]:
			if i != agenda[contato][0][-1]:
				numeros = numeros+i+"; "
			else:
				numeros = numeros+i+"."

		for j in agenda[contato][1]:
			if j != agenda[contato][1][-1]:
				enderecos = enderecos+j+"; "
			else:
				enderecos = enderecos+j+"."
		print("Nome: "+contato+"\n"+"Telefone: "+numeros+"\nEndereço: "+enderecos+"\n")
	else:
		print("Contato não existe na agenda.")

def inserir_contato(agenda):
	nome = input("Digite o nome do contato: ")

	numero = try_numero()

	endereco = input("Digite o endereco do contato: ")

	if nome not in agenda:
		agenda[nome] = ([numero], [endereco])

	else:
		while True:
			choice = input("Contato já existente, deseja uní-los (digite 1) ou abortar a operação (digite 2)? ")
			if choice == '1':
				if numero not in agenda[nome][0]:
					agenda[nome][0].append(numero)
				if endereco not in agenda[nome][1]:
					agenda[nome][1].append(endereco)
				break
			else:
				break

def deletar_contato(agenda):
	nome = input("Digite o nome do contato que deseja deletar: ")

	if nome in agenda:
		del agenda[nome]
	else:
		print("Contato não localizado.")

def add_numero(agenda):
	nome = input("Digite o nome do contato que deseja adicionar um número: ")

	numero = try_numero()
	
	if nome in agenda:

		if numero not in agenda[nome][0]:
			agenda[nome][0].append(numero)
		else:
			print("Número já existe na agenda.")
	else:
		print("Contato não localizado.")



while True:
	try:
		quant = int(input("Digite a quantidade de agendas: "))
	except:
		print("Número inválido. Tente novamente.")
	else:
		break

for i in range(quant):
	
	while True:
		try:
			agenda_dir = input("Digite o nome do arquivo: ")
			agenda_file = open(agenda_dir, "r")
		except:
			print("Agenda inexistente. Tente novamente.")
		else:
			break
	
	agenda_nome = input("Digite o nome do dono da agenda: ")
	
	agenda = {}

	print("\nAgenda de "+agenda_nome+"\n")

	for line in agenda_file.readlines():
		try:
			nome, numero, endereco = line.split(":")
			endereco, nada = endereco.split("\n")
		except:
			pass

		if nome not in agenda:
			agenda[nome] = ([numero], [endereco])

		else:
			if numero not in agenda[nome][0]:
				agenda[nome][0].append(numero)
			if endereco not in agenda[nome][1]:
				agenda[nome][1].append(endereco)

	agenda_file.close()

	print("Existem %s contatos na agenda:\n"%(len(agenda)))

	imprimir_agenda(agenda)

#	MENU DE INTERAÇÃO

while True:
	opt = input("O que deseja fazer a seguir? (Digite 'ajuda' para opções)\n")
	if (opt == 'ajuda' or  opt == '\'ajuda\''):
		print("\nNão use aspas ou apostrofes no menu.")
		print("\nPara imprimir a agenda novamente digite: \'agenda\'")
		print("\nPara imprimir um contato específico digite \'contato\'")
		print("\nPara inserir um novo contato digite \'inserir\'")
		print("\nPara deletar um contato digite \'deletar\'")
		print("\nPara adicionar um numero a um contato digite \'numero\'")
		print("\nPara sair digite \'quit\'\n")
	elif (opt == 'agenda'):
		imprimir_agenda(agenda)
	elif (opt == 'contato'):
		imprimir_contato(agenda)
	elif (opt == 'inserir'):
		inserir_contato(agenda)
	elif (opt == 'deletar'):
		deletar_contato(agenda)
	elif (opt == 'numero'):
		add_numero(agenda)
	elif (opt == 'quit'):
		print("O programa foi encerrado.")
		break
	else:
		print("Comando não reconhecido.")

# ~ Rodrigo Chiesse ~