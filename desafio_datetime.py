# Um usuario fornece sua dadta de nascimento no formato "dd/mm/aaaa". Criar um scipt que calcula a idade do usuario
from datetime import datetime

data_nascimento_usuario = input("Qual a data do seu aniversario (dd/mm/aaaa): ")

print(data_nascimento_usuario)
print(type(data_nascimento_usuario))
print('-'*20)

data_nascimento_usuario = datetime.strptime(data_nascimento_usuario, "%d/%m/%Y")
print(data_nascimento_usuario)
print(type(data_nascimento_usuario))

data_atual = datetime.now()
print(data_atual)

idade = data_atual.year - data_nascimento_usuario.year
mes_atual = data_atual.month
dia_atual = data_atual.day

mes_nascimento = data_nascimento_usuario.month
dia_nascimento = data_nascimento_usuario.day

if mes_nascimento > mes_atual:
    idade -= 1
elif mes_nascimento == mes_atual and dia_nascimento > dia_atual:
    idade -= 1

print(idade)