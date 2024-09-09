#pip install pytz

import datetime
import pytz

# Criando um datetime com timezone
d = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
print(d)