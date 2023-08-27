from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

agora = datetime.now()
print(agora)
print("-"*10)
print(agora.strftime("%A, %d de %B"))
print(agora.strftime("%a"))
data_formatada = agora.strftime("%A, %d de %B de %Y, %H:%M:%S")
print(f"Data Formatada: {data_formatada}")
print("-"*10)

import locale
from datetime import datetime
locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')
agora = datetime.now()
data_formatada = agora.strftime("%A, %d de %B de %Y, %H:%M:%S")
print(f"Data Formatada: {data_formatada}")
print("-"*10)

string_data = "30 Junho, 2023, 15:30:20"
formato1 = "%d %B, %Y, %H:%M:%S"
data = datetime.strptime(string_data, formato1)
print(f"Data: {data}")
print("-"*10)

# formato DD/MM/YYYY
string_data = "09/06/2023, 15:30:20"
formato2 = "%d/%m/%Y, %H:%M:%S"
data = datetime.strptime(string_data, formato2)
print(f"Data: {data}")
print("-"*10)

# formato MM/DD/YYYY
string_data = "09/06/2023, 15:30:20"
formato3 = "%m/%d/%Y, %H:%M:%S"
data = datetime.strptime(string_data, formato3)
print(f"Data: {data}")
print("-"*10)


#fuso horario
data_hora = datetime(2023, 6, 26, 15, 30, 20)
print(f"Data/hora: {data_hora}")

fuso_horario = timezone.utc
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario)
print(f"Data/hora: {data_hora}")
print("-"*10)


fuso_horario_sao_paulo = timezone(timedelta(hours=-3))
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario_sao_paulo)
print(f"Data/hora: {data_hora}")
print("-"*10)

# # exemplo com fuso horário de São Paulo sem necessidade de timedelta
from zoneinfo import ZoneInfo
fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario_sao_paulo)
print(f"Data/hora: {data_hora}")
print("-"*10)

data_hora_atual = datetime.now()
print(f"Data/hora atual (fuso horário local): {data_hora_atual}") 
fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario_sao_paulo)
print(f"Data/hora atual em São Paulo: {data_hora_sao_paulo}")
print("-"*10)

fuso_horario_ny = ZoneInfo('America/New_York')
data_hora_ny = data_hora_atual.astimezone(fuso_horario_ny)
print(f"Data/hora atual em Nova York: {data_hora_ny}")
print("-"*10)