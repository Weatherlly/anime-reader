import os

# Intervalo total desejado
capitulo_inicial = 0
capitulo_final = 374

# Descobre quais faltam com base nas pastas locais
faltando = []
for num in range(capitulo_inicial, capitulo_final + 1):
    pasta = f"kengan_omega_{num}"
    if not os.path.exists(pasta):
        faltando.append(num)

print(f"Capítulos faltantes ({len(faltando)}): {faltando}")