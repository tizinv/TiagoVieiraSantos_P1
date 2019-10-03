# Autor: Tiago Vieira Santos

import math
def segundograu(a,b,c):
  delta = (b**2) - (4 * a * c)
  if delta < 0:
    print ("Raízes Complexas = " + str(-b / (2 * a)) + "+-" + str(math.sqrt(-delta) / (2 * a)) + "i")
    return 1
  raiz1 = (-b + math.sqrt(delta)) / 2*a 
  raiz2 = (-b - math.sqrt(delta)) / 2*a
  return (0, raiz1, raiz2)
def main():
  a = int(input("Entre com o parâmetro a:\n"))
  b = int(input("Entre com o parâmetro b:\n"))
  c = int(input("Entre com o parâmetro c:\n"))
  print("Se o Resultado for 1 = raízes complexas\nSe o Resultado for 0 = raízes reais \n\n\t\t\t\tRaiz1, Raiz2")
  print("Resultado = ", segundograu(a,b,c))

  
main()
