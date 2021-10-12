import csv
import semaforootimizado as so
import semafarocomum as sc

# 1. cria o arquivo
f = open('volume.csv', 'w', newline='', encoding='utf-8')

# 2. cria o objeto de gravação
w = csv.writer(f)

# 3. grava as linhas
for i in range(5):
  w.writerow([i, i*2, i*3])

# Recomendado: feche o arquivo
w.close() 