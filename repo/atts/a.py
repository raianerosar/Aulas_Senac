n = input("Nome: ")
p = float(input("Peso (kg): "))
a = float(input("Altura: "))

imc = p/ (a **2)
print(f"IMC de {n}: {imc: .2f}")
p_baixo = imc < 18.5
normal = (imc >= 18.5) and (imc <25)
sobrepeso = (imc >= 25) and (imc <30)
obesidade = imc >= 30

print("Baixo preso: " , p_baixo)
print("Normal: ", normal)
print("Sobrepeso: " , sobrepeso)  
print("Obesidade: ", obesidade)
