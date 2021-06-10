#Formata os dados do CPF
from validate_docbr import CPF
from validate_docbr import CNPJ

class Documento:

	@staticmethod
	def cria_documento(documento):
		if (len(documento) == 11):
			return DocCpf(documento)
		elif(len(documento) == 14):
			return DocCnpj(documento)
		else:
			raise ValueError ("A quantidade de dígitos está incorreta!!")

class DocCpf:

	def __init__(self, documento):
		if (self.valida(documento)):
			self._cpf = documento
		else:
			raise ValueError("O CPF inválido!")

	def __str__(self):
		return self.formata(self._cpf)

	def valida(self, documento):
		validadorCpf = CPF()
		return validadorCpf.validate(documento)

	def formata(self, documento):
		mascara = CPF()
		return mascara.mask(self._cpf)


class DocCnpj:

	def __init__(self, documento):
		if (self.valida(documento)):
			self._cnpj = documento
		else:
			raise ValueError("O CNPJ inválido!")

	def __str__(self):
		return self.formata(self._cnpj)

	def valida(self, documento):
		validadorCpf = CNPJ()
		return validadorCpf.validate(documento)

	def formata(self, documento):
		mascara = CNPJ()
		return mascara.mask(self._cnpj)