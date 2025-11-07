#SeguridadSocial
import math

salbase=float(input("Ingrese el salario base del empleado: "))

aportsalud=salbase*0.04
aportpen=salbase*0.04
descuento=aportsalud+aportpen
salneto=salbase-descuento

print("El aporte a salud es de: ", aportsalud)
print("El aporte a pensión es de: ", aportpen)
print("El descuento es de: ", descuento)
print("El salario neto a pagar es: ", salneto)