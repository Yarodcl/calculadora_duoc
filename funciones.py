def calcular_iva():
    while True:
        producto = input("Calcularemos el IVA de tú producto, por favor, ingresa el valor del mismo: ")
        try:
            producto = int(producto)
            break
        except:
            print('Los datos no son validos, reintentar')
            continue
            #Termino While
    iva = (producto * 19) / 100
    iva = round(iva, 2)
    print(f'El IVA de tú producto es: ${iva}')
    
def calcular_descuento():
    while True:
        producto = input("Calcularemos el descuento de tú producto, por favor, ingresa el valor del mismo: ")
        try:
            producto = int(producto)
            break
        except:
            print('Los datos no son validos, reintentar')
            continue
            #Termino While
            
    while True:
        porcentaje = input("Por favor, ingresa el porcentaje de descuento: ")
        try:
            porcentaje = int(porcentaje)
            break
        except:
            print('Datos no validos, reintentar')
            continue

    descuento = (producto * porcentaje) / 100
    valor_final = producto - descuento
    valor_final = round(valor_final, 2)

    print(f'El descuento de tú producto es de : ${descuento}')
    print(f"El valor final de tú producto es de: ${valor_final}")

def calcular_imc():
    while True:
        print('Para calcular tú indice de masa corporal necesitaremos tanto tú peso como tú estatura')
        peso = input("Ingresa tú peso: ")
        estatura = input("Ingresa tú estatura: ")
        try:
            peso = float(peso)
            estatura = float(estatura)
            break
        except:
            print('Datos invalidos, reintentar')
            continue

    imc = peso / (estatura ** 2)
    imc = round(imc, 1)

    if imc < 18.5:
        print(f'Su IMC es de {imc}, por lo que usted se encuentra bajo peso')
    elif imc == 18.5 or imc <= 24.9:
        print(f'Su IMC es de {imc}, por lo que usted se encuentra en un peso adecuado')
    elif imc == 25.0 or imc <= 29.9:
        print(f'Su IMC es de {imc}, por lo que usted se encuentra con sobrepeso')
    elif imc == 30.0 or imc <= 34.9:
        print(f'Su IMC es de {imc}, por lo que usted se encuentra en un nivel de obesidad grado 1')
    elif imc == 35.0 or imc <= 39.9:
        print(f'Su IMC es de {imc}, por lo que usted se encuentra en un nivel de obesidad grado 2')
    elif imc > 40:
        print(f'Su IMC es de {imc}, por lo que usted se encuentra en un nivel de obesidad grado 3')
    else:
        print('No valido')


