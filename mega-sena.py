# Gerador de números para diversos sistemas de 
# loterias brasileiras

# 30/08/2022
# by: SynnK

import random 

numeros_finais = []

def gerar_numero():
    return str(abs(random.randrange(60))).zfill(2)

for i in range(6):
    num_gerado = gerar_numero()

    while num_gerado in numeros_finais:
        num_gerado = gerar_numero()

    if not num_gerado in numeros_finais:
        numeros_finais.append(num_gerado)
    
print('-'.join(numeros_finais))
