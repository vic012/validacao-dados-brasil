from cpf_cnpj import Cpfcnpj
from validate_docbr import CNPJ

#documento = Cpf(13456345554564)
exemplo = "35379838000112"
cnpj = Cpfcnpj(exemplo, 'cnpj')
print(cnpj)