#Formata os dados do CPF

class Cpf:

	def __init__(self, cpf):
		cpf = str(cpf)
		if (self.valida(cpf)):
			self._cpf = cpf
		else:
			raise ValueError("CPF inválido")

	def __str__(self):
		return self.formata()

	#Valida o CPF
	def valida(self, cpf):
		#Se o CPF tiver 11 carteres é um cpf
		if (len(cpf) == 11):
			return True
		#Senão demonstra um erro
		else:
			return False

	def formata(self):
		fatiaUm = self._cpf[:3]
		fatiaDois = self._cpf[3:6]
		fatiaTres = self._cpf[6:9]
		fatiaQuatro = self._cpf[9:]
		return ("{}.{}.{}-{}".format(
			fatiaUm,
			fatiaDois,
			fatiaTres,
			fatiaQuatro
		))
	