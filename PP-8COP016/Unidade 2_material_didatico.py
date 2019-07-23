
# TORNAR ESSA CLASSE ABSTRATA. ALÉM DO INIT E O STR, SEUS OUTROS
# MÉTODOS SERÃO ABSTRATOS. Dica: abc

import abc

class MaterialDidatico(abc.ABC):

	@abc.abstractclassmethod
	def __init__(self, titulo, autor):
		self._titulo = titulo
		self._autor = autor

	@abc.abstractclassmethod
	def __str__(self):
		return self._titulo

	@abc.abstractclassmethod
	def estudar(self):
		pass

	# CODIFICAR 3 MÉTODOS ABSTRATOS (SEM IMPLEMENTAÇÃO NENHUMA):
	# dar_uma_olhada(), abrir(), retomar()
	@abc.abstractclassmethod
	def dar_uma_olhada(self):
		pass

	@abc.abstractclassmethod
	def abrir(self):
		pass

	@abc.abstractclassmethod
	def retomar(self):
		pass

# FAZER A CLASSE LIVRO HERDAR DE MATERIALDIDATICO
class Livro(MaterialDidatico):

	def __init__(self, titulo, autor, capitulos, paginas):
		# CHAMAR O SUPER DA CLASSE MÃE
		MaterialDidatico.__init__(autor, titulo)
		# CRIAR 2 NOVOS ATRIBUTOS: CAPITULOS E PAGINAS

	def estudar(self):
		print("Lendo e refletindo a leitura")

	def dar_uma_olhada(self):
		print("Dando uma olhada no sumário, uma folheada...")

	def abrir(self):
		pass
		# IMPLEMENTE O MÉTODO

	def retomar(self):
		pass
		# IMPLEMENTE O MÉTODO

	def __len__(self):
		pass
		# RETORNE O NÚMERO DE PÁGINAS VEZES 5


# FAZER A CLASSE LIVRODIGITAL HERDAR DE LIVRO
class LivroDigital:

	def __init__(self, titulo, autor, capitulos, paginas, pasta_pc):
		super().__init__(titulo, autor, capitulos, paginas)
		self._pasta_pc = pasta_pc

	# REESCREVA OS MÉTODOS dar_uma_olhada(), abrir() e retomar()
	# ADPTANDO AS MENSAGENS PARA UM LIVRO DIGITAL


# FAZER A CLASSE SLIDE HERDAR DE MATERIALDIDATICO
class Slide:
	
	def __init__(self, titulo, autor, num_slides, tam_arquivo):
		pass
		# CHAMAR O SUPER DA CLASSE MÃE
		# CRIAR 2 NOVOS ATRIBUTOS: num_slides E tam_arquivo
	
	# REESCREVA OS MÉTODOS estudar() e dar_uma_olhada()

	def abrir(self):
		print("Clicando no arquivo PDF.")

	def retomar(self):
		print("Dando um scroll até o slide correto.")

	# REESCREVA O MÉTODO __len__ PARA QUE ELE RETORNE O NÚMERO
	# SLIDES VEZES 1.5 (E CONVERTA PARA INTEIRO ANTES DE RETORNAR)
	

# FAZER A CLASSE VIDEOAULA HERDAR DE MATERIALDIDATICO
class VideoAula:
	
	def __init__(self, titulo, autor, duracao):
		super().__init__(titulo, autor)
		self._duracao = duracao
	
	def estudar(self):
		print(self.__str__() + ": " + "Assistindo o vídeo e prestando atenção.")

	def dar_uma_olhada(self):
		print("Assistindo o começo da aula.")

	def abrir(self):
		print("Clicando no play.")

	def retomar(self):
		print("Selecionando o minuto correto e clicando em play.")
	
	# REESCREVA O MÉTODO __len__ PARA QUE ELE RETORNE
	# A DURAÇÃO DA VIDEOAULA


# FAZER A CLASSE CODIGO HERDAR DE MATERIALDIDATICO
class Codigo:

	def __init__(self, nome, autor, linhas, qtdade_funcoes, descricao):
		pass
		# CHAMAR O SUPER DA CLASSE MÃE
		# CRIAR 2 NOVOS ATRIBUTOS: linhas, qtdade_funcoes e descricao

	def estudar(self):
		print(self.__str__() + ": " + "Analisando e entendendo a sua lógica...")

	# REESCREVA OS MÉTODOS dar_uma_olhada(), abrir() e retomar()

	# REESCREVA O MÉTODO __len__ PARA QUE ELE RETORNE A
	# QUANTIDADE DE LINHAS / 2 (E CONVERTA PARA INTEIRO)


# EXPLICAR 1) QUAL O PAPEL DA CLASSE MATERALESTUDO?
# 2) O QUE ELA FAZ?
# 3) ONDE OCORRE O POLIMORFISMO?
class MaterialEstudo:

	def __init__(self, disciplina, unidade):
		self._disciplina = disciplina
		self._unidade = unidade
		self._lista_material = []

	def add_material(self, material):
		self._lista_material.append(material)

	def dar_olhada_nas_coisas(self):
		for m in self._lista_material:
			m.dar_uma_olhada()

	def maratonar_estudo(self):
		for m in self._lista_material:
			m.abrir()
			m.estudar()

	def tempo_total(self):
		total = 0
		for m in self._lista_material:
			total += len(m)
		return total


unidade1 = MaterialEstudo("Paradigmas de Programação", "Unidade 1")
lucas = "Lucas B. Galhardi"
nead = "NEAD"
aula1 = "Aula 1: Introdução aos Paradigmas de Programação"
s1 = Slide(aula1, lucas, 20, 542)
v1 = VideoAula(aula1, lucas + " e " + nead, 10)
unidade1.add_material(s1)
unidade1.add_material(v1)

# CRIAR +1 SLIDE, +1 VIDEOAULA, +1 LIVRO, +1 LIVRODIGITAL E +2 CODIGOS
# ADICIONE TODOS OS MATERIAIS À VARIÁVEL UNIDADE1

# USE O MÉTODO dar_olhada_nas_coisas()

print("Vish, vou demorar {} horas nessa unidade.".format(unidade1.tempo_total()/60))

# USE O MÉTODO maratonar_estudo()

# EXECUTE O CÓDIGO INTEIRO E VEJA A SAÍDA

# EXPLICAR O OBJETIVO GERAL DO CÓDIGO E EM QUE LUGAR PODEMOS VER OS SEGUINTES ELEMENTOS:
# MODELAGEM CONCEITUAL:
# MÉTODOS "MÁGICOS":
# CLASSE ABSTRATA:
# HERANÇA:
# REESCRITA DE MÉTODO:
# POLIMORFISMO:
