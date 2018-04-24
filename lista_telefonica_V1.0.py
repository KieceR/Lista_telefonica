# Programa desenvolvido pela Turma B de Prog II (MCG126) em 17/04/2018.

class Telefone:
	def __init__(self, valor="---"):
		self.legth = len(valor)
		if self.legth == 12:
			self.DDD 	= valor[:3]
			self.local  = valor[-9:]
		else:
			self.DDD	= ""
			self.local	= valor
	def __str__(self):
		if self.legth == 12:
			return ("Telefone: (" + self.DDD + ") " + self.local[:-4] + "-" + self.local[-4:])
		else:
			return ("Telefone: " + self.local[:-4] + "-" + self.local[-4:])


class Endereco:
	def __init__(self, valor="---"):
		self.valor  = valor

	def __str__(self):
		return "Endereco: "+str(self.valor)


class Contato:
	# >>> Construtor - inicializa os atributos de um objeto <<<
	def __init__(self, n, tel=None, end=None):
		self.nome = n.lower()
		self.enderecos = [ end ]
		self.telefones = [ tel ]
	
	# >>> Método especial para print <<<
	def __str__(self): 
		enderecos = ""
		numeros = ""
		for numero in self.telefones:
			numeros = numeros+str(numero)+"; "
		for endereco in self.enderecos:
			enderecos = enderecos+str(endereco)+"; "
		return "Nome: " + self.nome.title() + "\nNúmero: " + numeros + "\nEndereço: " + enderecos


class Agenda:
	def __init__(self, nome, contato=None):
		self.nome = nome
		if type(contato) == str:
			self.contatos = [ contato ]
		elif type(contato) == list:
			self.contatos = contato
		else:
			self.contatos = []

	def __str__(self):
		agenda_string = ""
		for c in self.contatos:
			agenda_string = agenda_string + str(c) + "\n"
		return agenda_string

	def incluir_contato(agenda, contato):
		agenda.contatos.append(contato)

	def remover_contato(agenda, contato):
		existe = False
		for i in agenda.contatos:
			if i.nome == contato:
				c = agenda.contatos.index(i)
				agenda.contatos[c].remove()
				existe = True
			else:
				pass
		if not existe:
			print("Não existe contato com este nome na agenda. ")

	def add_endereco(agenda, contato, endereco):
		existe = False
		for i in agenda.contatos:
			if i.nome == contato:
				c = agenda.contatos.index(i)
				agenda.contatos[c].enderecos.append(endereco)
				existe = True
			else:
				pass
		if not existe:
			print("Não existe contato com este nome na agenda. ")

	def add_telefone(agenda, contato, numero):
		existe = False
		for i in agenda.contatos:
			if i.nome == contato:
				c = agenda.contatos.index(i)
				agenda.contatos[c].enderecos.append(numero)
				existe = True
			else:
				pass
		if not existe:
			print("Não existe contato com este nome na agenda. ")


def imprimir(agenda, nome):
	print("Agenda de "+nome)
	print(agenda)
		

def imprimir_contato(agenda, contato):
	existe = False
	for i in agenda.contatos:
		if i.nome == contato:
			c = agenda.contatos.index(i)
			print(agenda.contatos[c])
			existe = True
		else:
			pass
	if not existe:
		print("Não existe contato com este nome na agenda. ")



quant=int(input("Digite a quantidade de agendas: "))
for q in range(quant):
	dono=input("Digite o nome do dono da agenda: ").title()
	nomearquivo=input("Digite o nome do arquivo: ")
	arquivo_agenda = open(nomearquivo, "r")
	agenda = Agenda(dono)

	for linha in arquivo_agenda.readlines():
		nome, numero, endereco = linha.split(":")
		nome = nome.strip()
		endereco = Endereco(endereco.strip())
		numero = Telefone(numero.strip())
		c = Contato(nome, numero, endereco)
		agenda.contatos.append(c)

	imprimir(agenda, agenda.nome)    
	arquivo_agenda.close()