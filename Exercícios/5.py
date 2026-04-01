n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

if n1 > n2:
    print(f"O primeiro número ({n1}) é maior.")
elif n2 > n1:
    print(f"O segundo número ({n2}) é maior.")
else:
    print("Os números são iguais.")