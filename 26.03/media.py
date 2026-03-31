notas = []

while True:
    nota = float(input("Digite a nota (digite 0 se quiser sair): "))
    
    if nota == 0:
        break
    
    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("Notas:", notas)
    print(f"Média: {media:.2}")
    
    if media >= 7:
        print("Situação: APROVADO")
    else:
        print("Situação: RECUPERAÇÃO")
else:
    print("Nenhuma nota foi digitada.")