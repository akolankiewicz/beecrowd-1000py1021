entrada = input().split()
a= int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

R = (a + b + abs(a-b)) / 2 
segundo = (R + c + abs(R-c)) / 2


print("{:.0f} eh o maior".format(segundo))