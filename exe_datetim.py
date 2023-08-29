# Exercicio 1-
from datetime import datetime
from zoneinfo import ZoneInfo

ultima_compra = datetime(2023, 5, 10)

data_hora_atual = datetime.now()

print(ultima_compra)
print(data_hora_atual)
print('-'*20)

diferenca =data_hora_atual - ultima_compra
print(diferenca)
print(type(diferenca))
print(diferenca.days)

if diferenca.days > 30:
    print("Voce ganhou um desconto!")

#Exercicio 2
data_hora_atual = datetime.now()
print(data_hora_atual)

fuso_horario_sp = ZoneInfo("America/Sao_Paulo")
fuso_horario_ny = ZoneInfo("America/New_York")
fuso_horario_tk = ZoneInfo("Asia/Tokyo")

data_hora_sp = data_hora_atual.astimezone(fuso_horario_sp)
data_hora_ny = data_hora_atual.astimezone(fuso_horario_ny)
data_hora_tk = data_hora_atual.astimezone(fuso_horario_tk)

print(f"""Data/hora em Sao Paulo {data_hora_sp}, 
Data/hora em NY {data_hora_ny} e Data/hora em Tokyo {data_hora_tk}""")

def horario_escritorio(data_hora):
    if 9 <= data_hora.hour < 17:
        return "Aberto"
    else:
        return "Fechado"
    
print(f"Escritorio de Sao Paulo esta {horario_escritorio(data_hora_sp)}")
print(f"Escritorio de Nova York esta {horario_escritorio(data_hora_ny)}")
print(f"Escritorio de Tokyo esta {horario_escritorio(data_hora_tk)}")