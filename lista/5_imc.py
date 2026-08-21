input_peso = float(input("Digite o peso: "))
input_altura = float(input("Digite a altura: "))

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

imc = calcular_imc(input_peso, input_altura)
print(f"\nO IMC calculado é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")