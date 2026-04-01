total_compras = 0.0
quantidade_compras = 0

print("Sistema de Compras (Digite 0 para finalizar)")

while True:
    valor = float(input("Digite o valor da compra: "))
    
    
    if valor == 0:
        break
    
    total_compras += valor
    quantidade_compras += 1


if quantidade_compras > 0:
    media = total_compras / quantidade_compras
    
    print("\n--- Resumo do Dia ---")
    print(f"Total das compras: R$ {total_compras:.2f}")
    print(f"Quantidade de compras: {quantidade_compras}")
    print(f"Valor médio das compras: R$ {media:.2f}")
else:
    print("\nNenhuma compra foi registrada.")

    