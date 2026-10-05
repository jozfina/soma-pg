from scipy.optimize import fsolve
from math import log

#Soma de n termos
def calcular_soma(u1, r, n):
    if r == 1:
        return u1 * n
    return u1 * (1 - r**n) / (1 - r)

# Primeiro termo
def calcular_u1(S, r, n):
    if r == 1:
        return S / n
    return S * (1 - r) / (1 - r**n)

# Razão
def calcular_r(S, u1, n):
    funcao = lambda r: u1 * (1 - r**n) / (1 - r) - S
    return fsolve(funcao, 1.5)[0]

# Número de termos
def calcular_n(S, u1, r):
    if r == 1:
        return S / u1

    n = log(1 - S * (1 - r) / u1) / log(r)
    return n


print("     CALCULADORA DE PROGRESSÃO GEOMÉTRICA")

print("O que pretende calcular?")

print("1 - Soma de n termos (Sₙ)")
print("2 - Primeiro termo (u₁)")
print("3 - Razão (r)")
print("4 - Número de termos (n)")

opcao = int(input("Introduza a opção pretendida, entre 1 e 4: "))

if opcao == 1:

    print("CÁLCULO DA SOMA")

    u1 = float(input("Introduza u₁: "))
    r = float(input("Introduza r: "))
    n = int(input("Introduza n: "))

    S = calcular_soma(u1, r, n)

    print("A soma dos", n, "termos é:", S)

elif opcao == 2:

    print("CÁLCULO DE u₁")

    S = float(input("Introduza Sₙ: "))
    r = float(input("Introduza r: "))
    n = int(input("Introduza n: "))

    u1 = calcular_u1(S, r, n)

    print("O primeiro termo u₁ é:", u1)

elif opcao == 3:

   
    print("CÁLCULO DA RAZÃO")
  

    u1 = float(input("Introduza u₁: "))
    S = float(input("Introduza Sₙ: "))
    n = int(input("Introduza n: "))

    r = calcular_r(S, u1, n)

    print("A razão r é:", r)

elif opcao == 4:

   
    print("CÁLCULO DE n")
  

    u1 = float(input("Introduza u₁: "))
    r = float(input("Introduza r: "))
    S = float(input("Introduza Sₙ: "))

    n = calcular_n(S, u1, r)

    print("O número de termos n é:", n)

# OPÇÃO INVÁLIDA
else:
         print()
         print("Opção inválida. Introduza um número entre 1 e 4.")