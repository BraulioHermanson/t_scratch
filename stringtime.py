import time 
import locale

tempo_em_struct = time.localtime()
print("-"*20)
print(tempo_em_struct)
print("-"*20)
print(time.strftime("%d %B %Y",tempo_em_struct))
print("-"*20)
print(time.strftime("%H %M %S",tempo_em_struct))
print("-"*20)

tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S",tempo_em_struct)
print(f"Tempo formatado: {tempo_formatado}")
print("-"*20)

print("Definir localizacao em pt-br")
locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')
tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S",tempo_em_struct)
print(f"Tempo formatado: {tempo_formatado}")
print("-"*20)

#time.strptime() analisa a string representando um horario de acordo com um formato. O retorno é um objeto struct_time
string_tempo = "30 Junho, 2023"
formato = "%d %B, %Y"
tempo_em_struct = time.strptime(string_tempo, formato)

print(f"Tempo em struct: {tempo_em_struct}")
print("-"*20)

# data na forma dia/mes/ano
string_tempo = "15/08/2023"
formato = "%d/%m/%Y"
tempo_em_struct = time.strptime(string_tempo, formato)
print(f"Tempo em struct: {tempo_em_struct}")
print("-"*20)

# data na forma mes/dia/ano
string_tempo = "06/11/2023"
formato = "%d/%m/%Y"
tempo_em_struct = time.strptime(string_tempo, formato)
print(f"Tempo em struct: {tempo_em_struct}")
print("-"*20)

#time gmtime() converte tempo expresso em segundos desde da EPOCH em um objecto struct time em UTC
time.gmtime(0)
gmt_struct = time.gmtime()
print(f"tempo em UTC: {gmt_struct}")
print(f"Tempo local: {time.localtime()}")
print("-"*20)
print(f"Tempo em UTC completo: {time.strftime('%A, %d de %B de %Y, %H:%M:%S',gmt_struct)}")
print("-"*20)
print(gmt_struct.tm_zone)
print("-"*20)
gmt_struct_exemplo = time.gmtime(1_234_567_890)

print(f"Tempo em UTC: {gmt_struct_exemplo}")
print(f"Tempo em UTC: {time.strftime('%A, %d de %B de %Y, %H:%M:%S', gmt_struct_exemplo)}") 
print("-"*20)
#mktime
tempo_em_struct = time.localtime()
tempo_em_segundos = time.mktime(tempo_em_struct)
print(f"Tempo em segundos: {tempo_em_segundos}")
print(f"Tempo em segundos: {time.time()}")
print("-"*20)
tempo_atual = time.localtime()
tempo_ano_novo = time.mktime((2023, 1, 1, 0, 0, 0, 0, 0, 0))
diferenca = time.mktime(tempo_atual) - tempo_ano_novo
print(f"Diferença em segundos: {diferenca}") 
print("-"*20)