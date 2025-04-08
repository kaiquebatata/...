# Solicita a distância e o tempo
espaco = float(input("Digite a distância percorrida (em km): "))
tempo = float(input("Digite o tempo gasto (em h): "))

# Verifica se a distância e o tempo são valores positivos
if espaco > 0 and tempo > 0:
    # Calcula a velocidade (v = espaço / tempo)
    velocidade = espaco / tempo
    print(f"A velocidade do veículo é: {velocidade} km/h")
else:
    # Exibe mensagem de erro
    print("Erro: A distância e o tempo devem ser valores positivos.")
