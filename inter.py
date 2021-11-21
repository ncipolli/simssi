import re

# lê o arquivo de texto
arquivo = open("valores.txt", "r")
arq = arquivo.read()
# retira caracteres especiais ( '[', ']', ',' )
new_string = re.sub(r"[^a-zA-Z0-9]", " ", arq)
# separa as palavras
valores = new_string.split()
print('inter')
# atribui os valores
vol1, cond1, st1, vol2, cond2, st2, vol3, cond3, st3, vol4, cond4, st4, toc, vr = valores
arquivo.close()