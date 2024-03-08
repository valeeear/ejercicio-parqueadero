import os
motos = 0
carros = 0
bicicletas = 0
patinetas = 0
controlBln = True
while controlBln == True:
    opcionStr =  input('Que tipo de vehiculo vas a ingresar?\n1.moto\n2.carros\n3.bicicletas\n4.patinetas\n5. Ver todas las salidas y entradas\n->')
    os.system('cls')
    if opcionStr == '1':
        movimientoStr = input('Que movimiento vas a hacer\n1.Entrada\n2.Salida\n->')
        cantidad_motosInt = int(input('Cual es la cantidad->?'))
        if movimientoStr == '1':
            motos += cantidad_motosInt
        if movimientoStr == '2':
            if motos >= cantidad_motosInt:
                motos -= cantidad_motosInt
            else:
                print('La cantidad de vehiculos a sacar no puede ser mayor a la que hay')
    if opcionStr == '2':
        os.system('cls')
        movimientoStr = input('Que movimiento vas a hacer\n1.Entrada\n2.Salida\n->')
        os.system('cls')
        cantidad_carroInt = int(input('Cual es la cantidad->?'))
        if movimientoStr == '1':
            carros += cantidad_carroInt
        if movimientoStr == '2':
            if carros >= cantidad_carroInt:
                carros -= cantidad_carroInt
            else: 
                print('La cantidad de vehiculos a sacar no puede ser mayor a la que hay')
    if opcionStr == '3':
        os.system('cls')
        movimientoStr = input('Que movimiento vas a hacer\n1.Entrada\n2.Salida\n->')
        os.system('cls')
        cantidad_bicicletasInt = int(input('Cual es la cantidad->?'))
        if movimientoStr == '1':
            bicicletas += cantidad_bicicletasInt
        if movimientoStr == '2':
            if  bicicletas >= cantidad_bicicletasInt:
                bicicletas -= cantidad_bicicletasInt
            else:
                print('La cantidad de vehiculos a sacar no puede ser mayor a la que hay')
    if opcionStr == '4':
        os.system('cls')
        movimientoStr = input('Que movimiento vas a hacer\n1.Entrada\n2.Salida\n->')
        os.system('cls')
        cantidad_patinetasInt = int(input('Cual es la cantidad->?'))
        if movimientoStr == '1':
            patinetas += cantidad_patinetasInt
        if movimientoStr == '2':
            if patinetas >= cantidad_patinetasInt:
                patinetas -= cantidad_patinetasInt
            else: 
                print('La cantidad de vehiculos a sacar no puede ser mayor a la que hay')                

    os.system('cls')
    if opcionStr == '5':

        print('El total de todos los ingresos fueron:')
        print(cantidad_motosInt, 'MOTOS' )  
        print(cantidad_carroInt, 'CARROS')
        print(cantidad_bicicletasInt, 'BICICLETAS')
        print(cantidad_patinetasInt, 'PATINETAS')          
        break                
        
   

    