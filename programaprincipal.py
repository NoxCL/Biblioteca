import funcionesbiblioteca as fb

while True:
    print('Menú de la Biblioteca "El Peruano Analfabeta"')
    print('')
    print('1. Registrar préstamo')
    print('2. Listar todos los préstamos')
    print('3. Imprimir recibo de préstamo')
    print('4. Salir del programa')
    print('')
    
    op = input('Seleccione una opción: ')
    print('')

    if op == '1':
            fb.registrar_prestamo()
    elif op == '2':
            fb.listar_prestamos()
    elif op == '3':
            fb.imprimir_recibo_prestamo()
    elif op == '4':
            fb.salir_programa()
    else:
            print('Opción no válida. Por favor, intente de nuevo.')