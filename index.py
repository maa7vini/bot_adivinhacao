import random 
import matplotlib.pyplot as plt 

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0 
    acertou = False 

    limite_inferior = 1
    limite_superior = 100

    while not acertou:
        chute = (limite_inferior + limite_superior) // 2
        tentativas += 1

        if chute == numero_secreto:
            acertou = True
        elif chute < numero_secreto:
            limite_inferior = chute + 1
        else:
            limite_superior = chute - 1
    
    return tentativas 

resultados = []

for i in range(100):
    tentativas = jogo_adivinhacao()
    resultados.append(tentativas)

media = sum(resultados) / len(resultados)
melhor = min(resultados)
pior = max(resultados)

print(f"Média de tentativas: {media:.2f}")
print(f"Melhor caso (menos tentativas): {melhor}")
print(f"Pior caso (mais tentativas): {pior}")

plt.plot(resultados, label='Tentativas por rodada')
plt.axhline(y=media, color='r', linestyle='--', label=f'Média: ({media:.2f})')
plt.title('Evolução das Tentativas do Bot')
plt.xlabel('Rodadas')
plt.ylabel('Número de tentativas')
plt.legend()
plt.show()