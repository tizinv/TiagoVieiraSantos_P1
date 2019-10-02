# Autor: Tiago Vieira Santos
def Nob(entrada1, entrada2):
    resultado = (entrada1//10) + (entrada1%10) + (entrada2//10) + (entrada2%10)
    return resultado
entrada1 = int(input("Entre o primeiro valor:\n"))
entrada2 = int(input("Entre o segundo valor:\n"))
print("O resultado do enigma de Nob entre {} e {} = {}".format(entrada1, entrada2, Nob(entrada1, entrada2)))
print("Ex:O resultado do enigma de Nob entre {} e {} = {}".format(entrada1, entrada2, Nob(21, 36)))
