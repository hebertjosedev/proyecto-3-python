from usuario import Usuario


class SistemaBancario:
    # BASE DE DATOS
    usuarios = [
        Usuario('john','doe','26275576','johndoe', '123456', []),
        Usuario('ryan','smith','25645888','ryansmith','123456789', [])
    ]
    
    def main(self):
        # USUARIO LEVANTA LA SESION
        self.menu_iniciar_sesion(self.usuarios)
        
    def menu_iniciar_sesion(self, session):
        session = session
        print("menu para iniciar sesion")
        nombre_usuario = input("Ingresa tu usuario: ")
        
        while not nombre_usuario.isalpha():
            nombre_usuario = input("Ingresa un usuario valido: ")

        filtrar_usuario = list(filter(lambda usuario: usuario.nombre_usuario == nombre_usuario, self.usuarios))
        
        while filtrar_usuario == []:
            nombre_usuario = input("Ingresa un usuario valido while 1 usuario: ")
            filtrar_usuario = list(filter(lambda usuario: usuario.nombre_usuario == nombre_usuario, self.usuarios))
        
        clave_usuario = input("Ingresa tu clave: ")
        
        while clave_usuario == '':
            print("Clave incorrecta!")
            clave_usuario = input("Ingresa tu clave nuevamente: ")
        
        filtrar_clave = list(filter(lambda clave: clave.clave_usuario == clave_usuario, self.usuarios))
        
        while filtrar_clave == []:
            clave_usuario = input("Ingresa bien tu clave valido while 1 clave: ")
            filtrar_clave = list(filter(lambda usuario: usuario.clave_usuario == clave_usuario, self.usuarios))
        
        nombre_de_usuario = nombre_usuario
        clave_de_usuario = clave_usuario
         
        if filtrar_usuario[0].nombre_usuario == nombre_de_usuario and filtrar_clave[0].clave_usuario == clave_de_usuario:
             print("TE HAS LOGUEADO CON EXITO!")
             print(f"Bienvenido {filtrar_usuario[0].nombre}")
             session = filtrar_usuario[0].cedula
             print(f"Dato en session luego de iniciar sesion {session}")
             self.menu_usuario(session)
         
        elif filtrar_usuario[0].nombre_usuario != nombre_de_usuario and filtrar_usuario[0].clave_usuario != clave_de_usuario:
             print("Ingreso fallido, datos invalidos")
    
     
    def crear_cuenta(self, cedula):
        print(f"Usuarios de arriba todos: {self.usuarios}")
        print(f"Usuario filtrado solo: {cedula}")
        numero_de_cuenta = input("Ingresa el numero de tu cuenta: ")

        while not numero_de_cuenta.isdigit() or len(numero_de_cuenta) != 12:
         print("Numero de cuenta invalido, tiene que tener 12 numeros tu cuenta")
         numero_de_cuenta = input("Ingresa un numero de cuenta valido no puede estar vacio: ")
        
        numero_cuenta = numero_de_cuenta
        
        saldo = input("Ingresa tu saldo inicial: ")
        
        while not saldo.isdigit():
         print("Saldo invalido solo numeros")
         saldo = input("Ingresa tu saldo inicial no puede estar vacio: ")
    
        saldo = int(saldo)
        saldo_inicial = format(saldo, ".2f")
        saldo_inicial = float(saldo_inicial)        
        
        for usuario in enumerate(self.usuarios):
            if usuario[1].cedula == cedula:
                self.usuarios[usuario[0]].cuentas_usuarios = [numero_cuenta, saldo_inicial]
                print("Cuenta creada con exito!")
                print(self.usuarios[1].cuentas_usuarios)
                return self.menu_usuario(usuario[1].cedula)
    
    def depositar(self, cedula):
        for usuario in enumerate(self.usuarios):
            if usuario[1].cedula == cedula:
                cuentas = usuario[1].cuentas_usuarios
                
                if cuentas == []:
                 print("No tienes cuenta, create una para poder usarla")
                 self.menu_usuario(usuario)
        
        print("depositar saldo a la cuenta")
        deposito = input("Ingresa la cantidad a depositar: ")
        
        while not deposito.isdigit():
            deposito = input("Dato invalido, ingresa la cantidad a depositar: ")
            
        deposito = int(deposito)

        self.usuarios[usuario[0]].cuentas_usuarios[1] += deposito
        print(f"Saldo actual despues del deposito: {self.usuarios[usuario[0]].cuentas_usuarios[1]}")
        return self.menu_usuario(cedula)
        
    def retirar(self, cedula):
        for usuario in enumerate(self.usuarios):
            if usuario[1].cedula == cedula:
                cuentas = usuario[1].cuentas_usuarios
                
                if cuentas == []:
                 print("No tienes cuenta, create una para poder usarla")
                 self.menu_usuario(usuario)
        
        print("Retirar dinero en tu cuenta")
        deposito = input("Ingresa la cantidad a retirar: ")
        
        while not deposito.isdigit():
            deposito = input("Dato invalido, ingresa la cantidad a depositar: ")
            
        deposito = int(deposito)

        self.usuarios[usuario[0]].cuentas_usuarios[1] -= deposito
        print(f"Saldo actual despues del retiro: {self.usuarios[usuario[0]].cuentas_usuarios[1]}")
        return self.menu_usuario(cedula)
        
    def transferir(self, cedula):
        for emisor in enumerate(self.usuarios):
            if emisor[1].cedula == cedula:
                cuenta_emisor_indice = emisor[0]
                cuenta_emisor = emisor[1].cuentas_usuarios
                
                if cuenta_emisor == []:
                 print("No tienes cuenta, create una para poder usarla")
                 self.menu_usuario(emisor)
            
        cedula_destinatario = input("Ingresa la cedula de tu destinatario: ")
        
        while cedula_destinatario == '':
            cedula_destinatario = input("Ingresa una cedula valida: ")
        
        for destinatario in enumerate(self.usuarios):
            if destinatario[1].cedula == cedula_destinatario:
                cuenta_destinatario_indice = destinatario[0]
                cuenta_destinatario = destinatario[1].cuentas_usuarios
                
                if cuenta_destinatario == []:
                 print("No tiene una cuenta tu destinatario, debe crear una para que le puedas transferir")
                 self.menu_usuario(destinatario)
                 
                elif cuenta_destinatario != []:
                 print(f"Nombre Destinatario: {destinatario[1].nombre} | Numero de cuenta: {destinatario[1].cuentas_usuarios[0]}")
                 numero_de_cuenta = input("Ingresa el numero de cuenta exacto, esta arriba: ")
            
                while numero_de_cuenta != destinatario[1].cuentas_usuarios[0]:
                 monto_transferencia = input("Ingresa el numero de cuenta exacto para la transferencia: ")
                
                monto_transferencia = input("Ingresa el monto de transferencia: ")
            
                while not monto_transferencia.isdigit():
                 monto_transferencia = input("Ingresa el monto de transferencia valido: ")
                
                monto_transferencia = int(monto_transferencia)
            
                if monto_transferencia < self.usuarios[cuenta_emisor_indice].cuentas_usuarios[1]:
                 self.usuarios[cuenta_emisor_indice].cuentas_usuarios[1] -= monto_transferencia
                 self.usuarios[cuenta_destinatario_indice].cuentas_usuarios[1] += monto_transferencia
                 print(f"Transferencia con exito, Saldo emisor: {self.usuarios[cuenta_emisor_indice].cuentas_usuarios[1]} | Saldo receptor: {self.usuarios[cuenta_destinatario_indice].cuentas_usuarios[1]}")
                else: print("Saldo insuficiente")
        
        #else: print ("Destinatario no encontrado")
        return self.menu_usuario(cedula)
    
    def cerrar_session(self):
        self.usuario = None
        self.main()
        
    def menu_usuario(self, session):
        print("1. Crear cuenta bancaria")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Transferir")
        print("5. Cerrar sesion")
        
        opcion_menu = input("Elige el numero de tu opcion: ")
            
        while not opcion_menu.isdigit():
            opcion_menu = input("Opcion invalida, solo numero de opciones: ")
            
        opcion_menu = int(opcion_menu)
        
        if opcion_menu == 1:
            for usuario in enumerate(self.usuarios):
                if usuario[1].cedula == session:
                    if usuario[1].cuentas_usuarios != []:
                        print("Ya tienes una cuenta creada, no hay plastico")
                    else:
                        print(f"Cuenta vacia: {usuario[1].cuentas_usuarios}")
                        print("EN BREVE CREARAS TU CUENTA BANCARIA")
                        self.crear_cuenta(session)
        elif opcion_menu == 2:
            print("DEPOSITAR")
            self.depositar(session)
        elif opcion_menu == 3:
            print("RETIRAR")
            self.retirar(session)
        elif opcion_menu == 4:
            print("TRANSFERIR")
            self.transferir(session)
        elif opcion_menu == 5:
            print("Has cerrado tu sesion, hasta pronto")
            self.menu_iniciar_sesion('')    
        

if __name__ == '__main__':
 sistema = SistemaBancario()
 sistema.main()