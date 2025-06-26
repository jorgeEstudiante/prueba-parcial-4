### ### ### ### ### ### ### ### ### ### ### ### ### ### 
entradas_disponibles = 500
menu = """TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE
1.- Comprar entrada a “los Fortificados”.
2.- Comprar entrada a “los Iluminados”.
3.- Stock de entradas para ambos conciertos.
4.- Salir.
"""
mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTVwXYZ'
numeros = '1234567890'
### ### ### ### ### ### ### ### ### ### ### ### ### ### 

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
def opcion_uno():
    try:
        nombre = input('Ingrese nombre de comprador: ')
    except:
        print('error')
    try:
        entrada = input('Ingrese tipo de entrada (G/V): ')
    except:
        print('error')
    while True:
        try:
            codigo = input('Ingrese código de confirmación: ')
        except:
            print('error')
        for a in codigo:
            if a not in mayusculas:
                print('Código no válido. Intente otra vez.')
                continue
        for a in codigo:
            if a not in numeros:
                print('Código no válido. Intente otra vez.')
                continue
        for a in codigo:
            if a == ' ':
                print('Código no válido. Intente otra vez.')
                continue
        if len(codigo) < 6:
            print('Código no válido. Intente otra vez.')
            continue
        else:
            print('Código validado.')
            print('¡Entrada registrada con éxito para “los Fortificados”!')
    return
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
def opcion_dos():
    nombre = input('Ingrese nombre de comprador: ')
    entrada = input('Ingrese tipo de entrada (CV/PAL): ')
    while True:
        codigo = input('Ingrese código de confirmación: ')
        for a in codigo:
            if a not in mayusculas:
                print('Código no válido. Intente otra vez.')
                continue
        for a in codigo:
            if a not in numeros:
                print('Código no válido. Intente otra vez.')
                continue
        for a in codigo:
            if a == ' ':
                print('Código no válido. Intente otra vez.')
                continue
        if len(codigo) < 6:
            print('Código no válido. Intente otra vez.')
            continue
        else:
            print('Código validado.')
            print('¡Entrada registrada con éxito para “los Iluminados”!')
    return
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
def opcion_tres():
    print(f'''Entradas disponibles para “los Fortificados”: {entradas_disponibles}
Entradas disponibles para “los Iluminados”:   {entradas_disponibles}
''')
    return
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 

### ### ### ### ### ### ### ### ###
def opcion_cuatro():
    print('Programa terminado...')
    return
### ### ### ### ### ### ### ### ### 

### ### ### ### ### ### ### ### ### ### ###
while True:
    print(menu)
    try:
        opcion = int(input('¿su eleccion?: '))
    except:
        print('error')
    if opcion == 1:
        opcion_uno()
    elif opcion == 2:
        opcion_dos()
    elif opcion == 3:
        opcion_tres()
    elif opcion == 4:
        opcion_cuatro()
        break
### ### ### ### ### ### ### ### ### ### ### 