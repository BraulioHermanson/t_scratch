import time 
import locale
locale.setlocale(locale.LC_TIME,"pt_BR.UTF-8")
# for numero in range(10, -1,-1):
#     print(numero)
#     #time.sleep(1)

# print("Começou!")
# print("-"*20)

for numero in range(10, -1,-1):
    print(numero, end=" \r") #add o espaco no end e depois o \r
    time.sleep(1)
print("Começou!")

# Exibindo a data e a hora atual no site em formato "dia da semana, dia do mes do ano, horas:minuto"

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B %Y, %H:%M",tempo_em_struct)
print(tempo_formatado)