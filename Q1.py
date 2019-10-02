# Autor: Tiago Vieira Santos

import.math(sqrt)
def 2grau(a,b,c):
  delta = (b**2) - (4 * a * c)
  if delta < 0:
    return 1
   raiz1 = -b + sqrt(delta)
   raiz2 = -b - sqrt(delta)
   return (0, raiz1, raiz2)
a = int(input("Entre com o parâmetro a"))
b = int(input("Entre com o parâmetro b"))
c = int(input("Entre com o parâmetro c"))
print("Modelo(número de raízes complexas, raiz1, raiz2)")
print(2grau(a,b,c))

2grau()
