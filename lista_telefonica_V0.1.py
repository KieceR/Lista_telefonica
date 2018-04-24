agenda_file = open("agenda.txt", "r")

agenda = {}

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

for contato in agenda:
	numeros = ""
	enderecos = ""

	for i in agenda[contato][0]:
		if i != agenda[contato][0][-1]:
			numeros = numeros+i+", "
		else:
			numeros = numeros+i+"."

	for j in agenda[contato][1]:
		if j != agenda[contato][1][-1]:
			enderecos = enderecos+j+", "
		else:
			enderecos = enderecos+j+"."
	print("Nome: "+contato+"\n"+"Telefone: "+numeros+"\nEndereço: "+enderecos+"\n")	
