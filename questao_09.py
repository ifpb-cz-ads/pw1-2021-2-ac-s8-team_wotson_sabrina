import random
y = 0
n=random.randint(1,10)
while y < 3:
    y+=1
    x=int(input("Escolha um número entre 1 e 10:"))
    if (x==n):
        print("Você acertou!")
        break
    else:
        print("Você errou.")
