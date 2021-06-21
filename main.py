from telefones import Telefones
import re

#Produra por um padrão número, letra, número (Exemplo 1a2)
#padrao = "[0-9][a-z][0-9]"
#texto = "123 1a2 1cc aa1"
#Procura por um padrão número, letra, letra, número (Exemplo 1ab2)
#padrao = "[0-9][a-z]{2}[0-9]"
#texto = "123 1ab2 1cc aa1"
#resposta = re.search(padrao, texto)
#print(resposta.group())

#Padrão de e-mail
#\W 'Qualquer número de 0 até 9, letra de a até z ou 0 _(Underline)'
'''padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
email = 'Vixeeeeeeeeeeeeeeeeeeeeeeeeeeeee chico012@gmail.com.br'
resposta = re.search(padrao, email)
#print(resposta.group())

#Padrões para telefone
padraoMolde = "(xx)aaaa-wwww"
#Pode conter 4 ou 5 dígitos {4,5}
telefone = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "Eu gosto do numero 2126451234 e outro 12314563135"
#Encontra todas as correspondecias de um padrão em um texto
respostaTel = re.findall(telefone, texto)
print(respostaTel)'''

telefone = "552126481234"

telefone_obj = Telefones(telefone)
print(telefone_obj)
#Uso do () na rbiblioteca re (Captura e agrupa)
#(pais)(area ou regiao)(5 primeiros dígitos do número)(4 últimos dígitos)
#O ? indica que a parte indicada não é obrigatório
#padrao = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.findall(padrao, telefone)
#print(resposta)