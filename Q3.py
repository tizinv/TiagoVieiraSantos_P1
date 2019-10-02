# Autor: Tiago Vieira Santos	
# Valor de Pi
diferenca = 1
Valorpi = 0	
divisor1 = 1
divisor2 = 1
while (diferenca > (5*10**(-8))):
    pianterior = Valorpi
    Valorpi += 4/(divisor1 * divisor2)
    divisor1 += 2
    divisor2 *= -1
    diferenca = (pianterior - Valorpi) * divisor2
print("O valor de pi = {}".format(Valorpi))
