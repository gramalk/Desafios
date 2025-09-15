b = float(input("usuario, insira o primeiro valor: "))
a =  float(input("usuario, insira o segundo valor: "))
c =  float(input("usuario, insira o terceiro valor: "))
delta = b**2 - 4*a*c

print("valor de delta é: ", delta)

if delta > 0:
    print("a equação tem duas raizes")
elif delta == 0:
    print("a equação tem uma raiz real")
else:
    print("usuario,a equação não possui raizes")




