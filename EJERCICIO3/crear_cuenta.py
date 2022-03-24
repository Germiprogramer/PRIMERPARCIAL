from cuenta_bancaria import *
from cuenta_bancaria_plazofijo import *
from cuenta_bancaria_VIP import *

cuenta = ""

def crear_cuenta(cuenta):
    tipodecuenta = input("Selecciona el tipo de cuenta que quieres usar: normal, VIP, plazofijo:  ")

    if tipodecuenta == "normal":
        cuenta = Cuenta_bancaria(22, "Germán Llorente", 1, 674, 10000)

    if tipodecuenta == "VIP":
        cuenta = Cuenta_bancaria_VIP(22, "Germán Llorente", 1, 674, 10000, -10000)

    if tipodecuenta == "plazofijo":
        cuenta = Cuenta_bancaria_plazofijo(22, "Germán Llorente", 1, 674, 10000, 2)

    else:
        pass
    
    return cuenta