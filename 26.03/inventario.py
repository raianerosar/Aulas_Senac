inventario = []

while True:
    item = input("Digite seu item, se quiser sair (digite Sair): ").strip()
    
    if item.lower() == "sair":
        break
    
    inventario.append(item)

inventario.sort()

print("Inventário já organizado:", inventario)
