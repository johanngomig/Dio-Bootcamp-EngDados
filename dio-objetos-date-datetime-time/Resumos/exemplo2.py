import datetime

# Criando data e hora
d = datetime.datetime(2024, 9, 9, 10, 20, 10)
print(d)

# Adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d)