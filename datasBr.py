from datetime import datetime, timedelta

class DatasBr:

	def __init__(self):
		self.momento_cadastro = datetime.today()

	@property
	def data_formatada(self):
		return self.momento_cadastro.strftime("O cadastro foi realizado em %d/%m/%Y às %H horas e %M minutos.")
	
	def mes_cadastro(self):
		meses_do_ano = [
			"Janeiro",
			"Fevereiro",
			"Março",
			"Abril",
			"Maio",
			"Junho",
			"Julho",
			"Agosto",
			"Setembro",
			"Outubro",
			"Novembro",
			"Dezembro"
		]
		#Retorna um inteiro que sinaliza o mês do ano
		mes_cadastro = self.momento_cadastro.month
		return meses_do_ano[mes_cadastro -1]

	def dia_semana(self):
		dias_da_semana = [
			"Domingo",
			"Segunda-Feira",
			"Terça-Feira",
			"Quarta-Feira",
			"Quinta-Feira",
			"Sexta-Feira"
		]
		#Retorna o dia da semana
		dia_semana = self.momento_cadastro.weekday()
		return dias_da_semana[dia_semana + 1]
