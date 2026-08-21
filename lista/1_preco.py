produto = "Camiseta"
quantidade = 5
preco = 50

total = quantidade * preco

print(f"O valor total da compra é: {quantidade} x R${preco} = R${total}")

if total >= 200:
    desconto = total * 0.10
    total_com_desconto = total - desconto

    print(f"O produto {produto} teve 10% de desconto.")
    print(f"Valor com desconto: R${total_com_desconto:.2f}")
else:
    print(f"O produto {produto} não recebeu desconto.")
    print(f"Valor final: R${total:.2f}")