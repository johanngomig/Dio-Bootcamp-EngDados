import datetime

d = datetime.datetime.now()

# Formatando data e hora
print(d.strftime('%d/%m/%Y %H:%M:%S')) #09/09/2024 13:15:30

# Convertendo string para datetime
date_string = '09/09/2024 13:15:30'
d = datetime.datetime.strptime(date_string, '%d/%m/%Y %H:%M:%S')
print(d)