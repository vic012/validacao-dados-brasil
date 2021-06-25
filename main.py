from acessoCep import BuscaCep

cep = 58801680
objeto_cep = BuscaCep(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(cidade, uf, bairro)