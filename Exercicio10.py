qdcf = int(input("quantidade de cigarros fumados ao dia:"))
qaf = int(input("quantos anos ja fumou:"))

A = qaf*365
R = qdcf*A/144

print("quantidade de dias de vida que o fumante perdeu:",R)
