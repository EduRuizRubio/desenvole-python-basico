from datetime import datetime

agora = datetime.today()

# Data atual
dia = agora.day
mes = agora.month
ano = agora.year

print("Data: ", dia, "/", mes, "/", ano)

# Hora atual
hora = agora.hour
min = agora.minute

print("Hora: ", hora, ":", min)