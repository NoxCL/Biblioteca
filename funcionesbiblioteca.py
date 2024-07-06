import datetime

prestamos = []

def validar_fecha(texto_fecha):
#esta funcion permite verificar que las fechas ingresadas sean correctas
    try:
        fecha = datetime.datetime.strptime(texto_fecha, '%Y-%m-%d')
        return fecha
    except ValueError:
        return None

def registrar_prestamo():
#aqui se pide el nombre al usuario
    while True:
        nombre = input('Ingrese el nombre y apellido del usuario: ')
        if nombre:
            break
        else:
            print('El nombre ingresado no es válido. Por favor, intente de nuevo.')
    
#aqui se le pide una identificacion del libro, tiene que ser numerica y contener como minimo 4 digitos
    while True:
        id_libro = input('Ingrese la identificación del libro (ID): ')
        if id_libro.isdigit() and len(id_libro) >= 4:
            id_libro = int(id_libro)
            break
        else:
            print('El ID del libro debe ser un número de al menos cuatro dígitos. Por favor, intente de nuevo.')
    
#aqui se ingresa la fecha de prestamo, el programa verifica si las fechas son validas, e impide que se pueda ingresar
#una fecha de devolucion anterior a la de prestamo
    while True:
        fecha_prestamo_texto = input('Ingrese la fecha de préstamo (YYYY-MM-DD): ')
        fecha_prestamo = validar_fecha(fecha_prestamo_texto)
        if fecha_prestamo:
            break
        else:
            print('La fecha de préstamo no es válida. Por favor, intente de nuevo.')
    
    while True:
        fecha_devolucion_texto = input('Ingrese la fecha de devolución (YYYY-MM-DD): ')
        fecha_devolucion = validar_fecha(fecha_devolucion_texto)
        if fecha_devolucion:
            if fecha_devolucion >= fecha_prestamo:
                break
            else:
                print('La fecha de devolución no puede ser anterior a la fecha de préstamo. Por favor, intente de nuevo.')
        else:
            print('La fecha de devolución no es válida. Por favor, intente de nuevo.')

#creacion del diccionario resultante con los valores pedidos anteriormente
    prestamo = {
        'nombre': nombre,
        'id_libro': id_libro,
        'fecha_prestamo': fecha_prestamo,
        'fecha_devolucion': fecha_devolucion
    }
    prestamos.append(prestamo)
    print('')
    print('Préstamo registrado exitosamente.')

def listar_prestamos():
#se  verifica si existen prestamos registrados y se enumeran para imprimir en la terminal
    if not prestamos:
        print('No hay préstamos registrados.')
        print('')
        return

    for i, prestamo in enumerate(prestamos, start=1):
        print(f'{i}. Nombre: {prestamo['nombre']}, ID del libro: {prestamo['id_libro']}, Fecha de préstamo: {prestamo['fecha_prestamo']}, Fecha de devolución: {prestamo['fecha_devolucion']}')

def imprimir_recibo_prestamo():
#al igual que la funcion anterior esta tambien verifica si existen prestamos registrados, pero creando en este caso
#un archivo .txt que actua como boleta para ser impresa.
    if not prestamos:
        print('No hay préstamos registrados.')
        print('')
        return

    listar_prestamos()
    try:
        indice_prestamo = int(input('Seleccione el número del préstamo para imprimir el recibo: ')) - 1
        if indice_prestamo < 0 or indice_prestamo >= len(prestamos):
            print('Número de préstamo no válido.')
            print('')
            return
    except ValueError:
        print('Entrada no válida.')
        print('')
        return

    prestamo = prestamos[indice_prestamo]
    texto_recibo = (
        f'Recibo de Prestamo\n'
        f'Nombre: {prestamo['nombre']}\n'
        f'ID del libro: {prestamo['id_libro']}\n'
        f'Fecha de prestamo: {prestamo['fecha_prestamo']}\n'
        f'Fecha de devolución: {prestamo['fecha_devolucion']}\n'
    )

    with open('recibo_prestamo.txt', 'w') as archivo:
        archivo.write(texto_recibo)
    
    print('Recibo de préstamo generado exitosamente.')
    print('')

def salir_programa():
#funcion simple que termina el programa
    print('Saliendo del programa...')
    exit()
