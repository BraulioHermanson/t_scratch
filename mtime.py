import time

tempo_atual_segundos = time.time()
print(f"Tempo atual: {tempo_atual_segundos} segundos desde a Epoch")

tempo_atual_nanosegundos = time.time_ns()
print(f"Tempo atual: {tempo_atual_nanosegundos} nanosegundos desde a Epoch")

inicio = time.time()

for i in range(100_000_000): # 10000000
    pass

fim = time.time()

print(f"Tempo decorrido: {fim - inicio} segundos")

#time.sleep
print("Iniciando a pausa")
time.sleep(5)  # Pausa o programa por 5 segundos
print("Pausa terminada")

#time.ctime
#funcao converte um tempo expresso em segundos desde a epoch em uma string representando o tempo local.
tempo_em_segundos = time.time()
tempo_local = time.ctime(tempo_em_segundos)
print(f"Tempo local: {tempo_local}")

tempo_em_segundos = time.time()
tempo_local = time.localtime(tempo_em_segundos)
print(f"Tempo local: {tempo_local}")

print(tempo_local.tm_year)
print(tempo_local.tm_hour)
print(tempo_local.tm_mday)
#dia da semana(0-6, 0=segund e 6 domingo)
print(tempo_local.tm_wday)
# dia do ano
print(tempo_local.tm_yday)

print(time.time())
print(time.ctime(time.time()))
print(time.localtime())