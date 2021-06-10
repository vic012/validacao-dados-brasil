#Formata os dados do CPF
from validate_docbr import CPF
from validate_docbr import CNPJ

class Cpfcnpj:

	def __init__(self, documento, tipoDocumento):
		self.tipoDocumento = tipoDocumento.upper()
		documento = str(documento)
		if (tipoDocumento == "CPF"):
			if (self.validaCpf(documento)):
				self._documento = documento
			else:
				raise ValueError("CPF inválido")
		else:
			if (self.validaCnpj(documento)):
				self._documento = documento
			else:
				raise ValueError("CNPJ inválido")

	#Valida o CPF
	def validaCpf(self, cpf):
		#Se o CPF tiver 11 carteres é um cpf
		if (len(cpf) == 11):
			validadorCpf = CPF()
			return validadorCpf.validate(cpf)
		#Senão demonstra um erro
		else:
			raise ValueError("O CPF deve possuir 11 dígitos! Mas você inseriou {} dígitos".format(len(cpf)))

	#Valida o CNPJ
	def validaCnpj(self, cnpj):
		#Se o CNPJ tiver 14 carteres é um cnpj
		if (len(cnpj) == 14):
			validadorCnpj = CNPJ()
			return validadorCnpj.validate(cnpj)
		#Senão demonstra um erro
		else:
			raise ValueError("O CNPJ deve possuir 14 dígitos! Mas você inseriou {} dígitos".format(len(cnpj)))

	def formata(self):
		if (self.tipoDocumento == "CPF"):
			mascara = CPF()
			return mascara.mask(self._documento)
		else:
			mascara = CNPJ()
			return mascara.mask(self._documento)
	
	def __str__(self):
		return self.formata()