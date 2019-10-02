# Autor: Tiago Vieira Santos

import math
def segundograu(a,b,c):
  delta = (b**2) - (4 * a * c)
  if delta < 0:
    return (1, "raiz complexa", "raiz complexa")
  raiz1 = (-b + math.sqrt(delta)) / 2*a 
  raiz2 = (-b - math.sqrt(delta)) / 2*a
  return (0, raiz1, raiz2)
a = int(input("Entre com o parâmetro a:\n"))
b = int(input("Entre com o parâmetro b:\n"))
c = int(input("Entre com o parâmetro c:\n"))
print("Modelo(1 = raízes complexas/ 0 = raízes reais, raiz1, raiz2)")
print(segundograu(a,b,c))
