#Formata os dados do CPF
from validate_docbr import CPF
from validate_docbr import CNPJ

class CpfCnpj:

	def __init__(self, documento, tipo_de_documento):
		self._tipo_de_documento = tipo_de_documento
		documento = str(documento)
		if (self._tipo_de_documento == "cpf"):
			if (self.valida(documento)):
				self._cpf = documento
			else:
				raise ValueError("CPF inválido")
		elif (self._tipo_de_documento == "cnpj"):
			if (self.validate_cnpj):
				self._cnpj = documento
			else:
				raise ValueError("CNPJ inválido!!")

	#Valida o CPF
	def valida_cpf(self, cpf):
		#Se o CPF tiver 11 carteres é um cpf
		if (len(cpf) == 11):
			validador = CPF()
			return validador.validate(cpf)
		#Senão demonstra um erro
		else:
			raise ValueError("O CPF deve possuir 11 dígitos! Mas você inseriou {} dígitos".format(len(cpdocumentof)))

	def validade_cnpj(self, cnpj):
		if (len(cnpj) == 14):
			validate_cnpj = CNPJ()
			return validate_cnpj.validate(cnpj)
		else:
			raise ValueError("O CNPJ deve possuir 14 dígitos! Mas você inseriou {} dígitos".format(len(cnpj)))
	
	def formata(self):
		mascara = CPF()
		return mascara.mask(self._cpf)
	
	def __str__(self):
		return self.formata()

