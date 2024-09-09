from datetime import timedelta, datetime, date, time

tipo_carro = 'M' # P - Pequeno, M - Medio, G - Grande
tempo_pequeno = 130
tempo_medio = 4500
tempo_grande = 9000
data_atual = datetime.now()

if tipo_carro == 'P':
    # print(data_atual + timedelta(days=tempo_pequeno))
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == 'M':
    # print(data_atual + timedelta(days=tempo_medio))
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    #print(data_atual + timedelta(days=tempo_grande))
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
    
print(date.today() - timedelta(days=1))

resultado = datetime(2024, 9, 9, 12, 34, 00) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())