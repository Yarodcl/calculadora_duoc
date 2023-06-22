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
    round(iva, 2)
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

    print(f'El valor de tú producto es de : ${producto}')
    print(f'El porcentaje de tú producto es de : ${porcentaje}')
    print(f'El descuento de tú producto es de : ${descuento}')
    print(f"El valor final de tú producto es de: ${valor_final}")

calcular_descuento()