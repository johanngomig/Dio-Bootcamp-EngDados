from datetime import datetime

data_hora_atual = datetime.now()
data_hora_string = "2024-09-09 10:15"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))


data_convertida = datetime.strptime(data_hora_string, mascara_en)
print(data_convertida)
print(type(data_convertida))