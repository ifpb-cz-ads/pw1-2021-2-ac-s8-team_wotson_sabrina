n1 = int(input("Digite um numero:"))
n2 = int(input("Digite outro numero:"))

def maior(n1, n2):
    return(n1>n2)

def maximo(n1, n2):
    if maior(n1,n2):
        return(n1, "e maior")
    else:
        return(n2, "e maior")

print(maximo(n1,n2))
