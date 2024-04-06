entrada = input().split()
codigo_1 = int(entrada[0])
quantidade_1 = int(entrada[1])
valor_1 = float(entrada[2])

entrada = input().split()
codigo_2 = int(entrada[0])
quantidade_2 = int(entrada[1])
valor_2 = float(entrada[2])

total = quantidade_1*valor_1 + quantidade_2*valor_2

print("VALOR A PAGAR: R$ {:.2f}".format(total))