# Autor: Tiago Vieira Santos
def Nob(entrada1, entrada2):
    if entrada2 > entrada1:
        return Nob(entrada2, entrada1)
    resultado = entrada1 - entrada2
    return resultado
entrada1 = int(input("Entre o primeiro valor:\n"))
entrada2 = int(input("Entre o segundo valor:\n"))
print("O resultado do enigma de Nob entre {} e {} = {}",.format(entrada1, entrada2, Nob(entrada1, entrada2)))


Nob()
