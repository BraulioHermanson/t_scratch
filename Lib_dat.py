from datetime import datetime, timedelta
from datetime import date 

agora = datetime.now()
print(f"Agora: {agora}")

print(f"Data: {agora.date()}")
print(f"Horario: {agora.time()}")
print("-"*10)
print(f"Ano: {agora.year}")
print(f"Mês: {agora.month}")
print(f"Dia: {agora.day}")
print(f"Hora: {agora.hour}")
print(f"Minuto: {agora.minute}")
print(f"Segundo: {agora.second}")
print("-"*10)

# date.today
hoje = date.today()
print(f"Data atual: {hoje}")
print("-"*10)
print(f"Ano: {hoje.year}")
print(f"Mês: {hoje.month}")
print(f"Dia: {hoje.day}")
print("-"*10)

#A classe timedelta é usada para realizar operações com datas (adição e subtração).
data_atual = datetime.now()
print(f"Data atual: {data_atual}")
print("-"*10)
data_futura = data_atual + timedelta(days=10)
print(f"Data 10 dias no futuro: {data_futura}")
print("-"*10)
data_passada = data_atual - timedelta(days=10)
print(f"Data 10 dias no passado: {data_passada}")
print("-"*10)

dez_horas_adiante = data_atual + timedelta(hours=10)
print(f"10 horas adiante: {dez_horas_adiante}")

print("-"*10)
data = datetime(2023, 7, 20, 8, 30, 20)
print(f"Data criada: {data}")
data = datetime(2023, 7, 20)
print(f"Data criada: {data}")
data = datetime(2023, 7, 20, 8, 30, 20, 100000)
print(f"Data criada: {data}")
print("-"*10)

# fromisoformat() é um método de classe que converte uma string em um objeto datetime.
data_hora_iso = datetime.fromisoformat("2023-06-26 15:30:20")
print(f"Data/hora: {data_hora_iso}")
print("-"*10)

#Calculando diferença de duas datas
data1 = datetime(2023, 6, 25)
data2 = datetime(2023, 7, 25)

diferenca = data2 - data1
print(f"A diferença entre as duas datas é de {diferenca.days} dias.")
print(type(diferenca))
print(diferenca.days)
print("-"*10)

## diferença entre datas

data1 = datetime(2023, 7, 25)
data2 = datetime(2023, 8, 16)

if data1 > data2:
    print("A data1 é posterior à data2")
elif data1 < data2:
    print("A data1 é anterior à data2")
else:
    print("As datas são iguais")

print("-"*10)
data1 = datetime(2023, 7, 25, 8, 30, 30)
data2 = datetime(2023, 7, 25, 8, 30, 20)

if data1 > data2:
    print("A data1 é posterior à data2")
elif data1 < data2:
    print("A data1 é anterior à data2")
else:
    print("As datas são iguais")

print("-"*10)
datas = [
    datetime(2023, 6, 28),
    datetime(2023, 5, 28),
    datetime(2023, 7, 28),
    datetime(2023, 6, 18),
]

datas_ordenadas = sorted(datas)

print(datas_ordenadas)
for data in datas_ordenadas:
    print(data.date())
print("-"*10)
