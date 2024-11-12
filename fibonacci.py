#Criando um código para fibonacci

A = 0
B = 1
C = 0

lp = 200
i  = 0

print(A)
print(B)
while i < lp:
    C = A + B
    print(C)
    A = B + C
    print(A)
    B = C + A
    print(B)

    i += 1