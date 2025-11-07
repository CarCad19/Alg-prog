#Cdt Bancario
import math

cantidad=float(input("Ingrese la cantidad de dinero: "))
periodo=float(input("Ingrese el periodo en días: "))
Porcenint=float(input("Ingrese el porcentaje de interés: "))

valint=(cantidad*Porcenint/100*periodo)/360
valimpu=valint*0.07
netopagar= cantidad+valint-valimpu

print("Intereses ganados: ", valint)
print("Valor del impuesto: ", valimpu)
print("Total a pagar al cliente: ", netopagar)