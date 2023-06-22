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
    
calcular_iva()