m = float(input("digite o preço da mercadoria: "))
p = float(input("porcentagem de desconto:"))

print("valor do desconto", m*p/100)
print("preço a pagar", m*-p/100+m)
