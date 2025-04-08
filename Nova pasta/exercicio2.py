# Solicita o preço à vista e a quantidade de parcelas
preco_vista = float(input("Digite o preço à vista do produto: R$ "))
parcelas = int(input("Digite a quantidade de parcelas: "))

# Verifica a quantidade de parcelas e aplica o acréscimo correspondente
if parcelas == 1:
    # Pagamento à vista sem acréscimo
    total_a_pagar = preco_vista
    prestacao = total_a_pagar
elif parcelas <= 3:
    # Pagamento parcelado em 2 ou 3 vezes com acréscimo de 10%
    total_a_pagar = preco_vista * 1.10
    prestacao = total_a_pagar / parcelas
else:
    # Pagamento parcelado em 4 ou mais vezes com acréscimo de 20%
    total_a_pagar = preco_vista * 1.20
    prestacao = total_a_pagar / parcelas

# Exibe o total a pagar e o valor da prestação mensal
print(f"\nTotal a pagar: R$ {total_a_pagar:.2f}")
print(f"Valor da prestação mensal: R$ {prestacao:.2f}")
