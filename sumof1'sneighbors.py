def calcular_soma_vizinhos(vetor):
    soma = 0
    for i in range(len(vetor)):
        if vetor[i] == 1:
            if i > 0:
                soma += vetor[i - 1]
            if i < len(vetor) - 1:
                soma += vetor[i + 1]
    return soma
def main():
    n = int(input())
    vetor = []
    for i in range(n):
        elemento = int(input())
        vetor.append(elemento)
    soma_vizinhos = calcular_soma_vizinhos(vetor)
    print(f"{soma_vizinhos}")
main()