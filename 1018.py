numero = int(input())

qntd100 = numero // 100
sobra76 = numero % 100
qntd50 = sobra76//50
sobra26 = sobra76 % 50
qntd20 = sobra26 // 20
sobra6 = sobra26 % 20 
qntd10 = sobra6 // 10
sobra262 = sobra6 % 10
qntd5 = sobra262 //5
sobra = sobra262 % 5
qntd2 = sobra // 2
sobra2 = sobra % 2
qntd1 = sobra2 // 1
final = sobra2 % 1

print(numero)
print(qntd100,"nota(s) de R$ 100,00")
print(qntd50,"nota(s) de R$ 50,00")
print(qntd20,"nota(s) de R$ 20,00")
print(qntd10,"nota(s) de R$ 10,00")
print(qntd5,"nota(s) de R$ 5,00")
print(qntd2,"nota(s) de R$ 2,00")
print(qntd1,"nota(s) de R$ 1,00")