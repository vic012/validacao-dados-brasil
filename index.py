#Formata os dados do CPF
from validate_docbr import CPF

class Cpf:

	def __init__(self, cpf):
		cpf = str(cpf)
		if (self.valida(cpf)):
			self._cpf = cpf
		else:
			raise ValueError("CPF inválido")

	#Valida o CPF
	def valida(self, cpf):
		#Se o CPF tiver 11 carteres é um cpf
		if (len(cpf) == 11):
			validador = CPF()
			return validador.validate(cpf)
		#Senão demonstra um erro
		else:
			raise ValueError("O CPF deve possuir 11 dígitos! Mas você inseriou {} dígitos".format(len(cpf)))

	def formata(self):
		mascara = CPF()
		return mascara.mask(self._cpf)
	
	def __str__(self):
		return self.formata()