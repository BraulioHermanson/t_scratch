import time

#Crie um script Python que calcula quantos dias, horas, minutos e segundos faltam até o próximo Ano Novo.

segundos_por_minuto = 60
segundos_por_hora = 60 * 60
segundos_por_dia = 24 * 60 * 60

print(f"Segundos em um minuto: {segundos_por_minuto} s")
print(f"Segundos em uma hora: {segundos_por_hora} s")
print(f"Segundos em um dia: {segundos_por_dia} s")
print("-"*20)
print(divmod(7, 3))
print("-"*20)

agora = time.localtime()
proximo_ano = (agora.tm_year + 1, 1, 1, 0, 0, 0, 0, 0, 0)

segundos_restantes = int(time.mktime(proximo_ano) - time.mktime(agora))

dias, resto_segundos = divmod(segundos_restantes, segundos_por_dia)
horas, resto_segundos = divmod(resto_segundos, segundos_por_hora)
minutos, segundos = divmod(resto_segundos, segundos_por_minuto)

print(f"Faltam {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos para o próximo Ano Novo.") 
print("-"*20)