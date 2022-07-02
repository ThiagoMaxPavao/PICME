from re import A
from gmpy2 import is_square, sqrt, get_context
get_context().precision=10000

def geraSequencias(a, p, tamanho):
    s1 = []
    s2 = []
    for n in range(1, tamanho+1):
        k = p**n
        i = 0
        while True:
            if is_square(a + k*i):
                raiz = int(sqrt(a + k*i))
                
                if len(s1) == 0:
                    s1.append(raiz)
                    s2.append(k-raiz)
                elif (raiz-s1[-1]) % p**(n-1) == 0:
                    s1.append(raiz)
                    s2.append(k-raiz)
                elif (raiz-s2[-1]) % p**(n-1) == 0:
                    s1.append(k-raiz)
                    s2.append(raiz)
                else: print("Como chegamos aqui?")
                break
            i+=1
    return s1, s2

def transformaAlfaEmX(a, b, s, p, nDigitos):
    x = []

    for n in range(1,nDigitos+1):
        for i in range(0 if n-2<0 else x[n-2], p**n):
            if (2*a*i + b-s[n-1])%(p**n) == 0:
                x.append(i)
                break
    return x

def transformSeqEmPadico(s, p, nDigitos):
    x = []
    x.append(s[0])
    for n in range(1, nDigitos):
        x.append(int((s[n] - s[n-1]) / p**n))
    x.reverse()
    return x

def imprimeSequencia(nome, s):
    print(nome.strip() + " = (", end="")
    for n in s:
        print(n, end=", ")
    print("...)")

def imprimePadico(nome, x):
    print(nome.strip() + " = [... , ", end="")
    for i in range(len(x)-1):
        print(x[i], end=", ")
    print(f"{x[-1]}]")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
p = int(input("p = "))
nDigitos = int(input("nDigitos = "))

s1, s2 = geraSequencias(b**2 - 4*a*c, p, nDigitos) # sequencias de alfa

x1 = transformaAlfaEmX(a, b, s1, p, nDigitos)
x2 = transformaAlfaEmX(a, b, s2, p, nDigitos)

x1N = transformSeqEmPadico(x1, p, nDigitos)
x2N = transformSeqEmPadico(x2, p, nDigitos)

print()
imprimeSequencia("s1", s1)
imprimeSequencia("x1", x1)
imprimePadico("x1", x1N)

print()
imprimeSequencia("s2", s2)
imprimeSequencia("x2", x2)
imprimePadico("x2", x2N)