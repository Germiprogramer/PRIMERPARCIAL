from cuenta_bancaria import *
from cuenta_bancaria_plazofijo import *
from cuenta_bancaria_VIP import *
from crear_cuenta import *

if __name__ == "__main__":
    crear_cuenta(cuenta)
    cuenta.ingresar(575)
    cuenta.retirar(78)
    cuenta.transferir(2000)

    print(cuenta.get_saldo())


