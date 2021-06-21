class BuscaCep:

	def __init__(self, cep):
		cep = str(cep)
		if (self.valida(cep)):
			self.cep = cep
		else:
			raise ValueError("CEP inválido!")

	def __str__(self):
		return self.format_cep()

	def valida(self, cep):
		if (len(cep) == 8):
			return True
		else:
			return False

	def format_cep(self):
		return "{}-{}".format(self.cep[:5], self.cep[5:])