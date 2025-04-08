import math

# Solicita os coeficientes da equação do segundo grau
a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))
c = float(input("Digite o valor de 'c': "))

# Calcula o valor de delta
delta = b**2 - 4*a*c

# Verifica se delta é positivo
if delta > 0:
    # Calcula as duas raízes reais
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    
    # Exibe as raízes reais
    print(f"As raízes reais da equação são: {raiz1} e {raiz2}")
elif delta == 0:
    # Calcula a raiz única quando delta é zero
    raiz = -b / (2 * a)
    print(f"A equação possui uma raiz real: {raiz}")
else:
    # Informa que não existem raízes reais
    print("Não existem raízes reais, pois o delta é negativo.")
