# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.
n = float(input("Insira seu número"))
f = 1
while n > 1:
    f *= n
    n -= 1
print (f"O fatorial é {f}")