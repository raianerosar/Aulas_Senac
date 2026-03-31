# Entrada de dados
peso = float(input("Digite seu peso em kg (ex.: 68.5): "))
altura = float(input("Digite sua altura em metros (ex.: 1.65): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação
if imc < 18.5:
    categoria = "Magreza"
elif imc < 25:  # já sabemos que é >= 18.5 aqui
    categoria = "Normal"
elif imc < 30:  # já sabemos que é >= 25 aqui
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

# Saída formatada
print(f"IMC = {imc:.2f} - {categoria}")


