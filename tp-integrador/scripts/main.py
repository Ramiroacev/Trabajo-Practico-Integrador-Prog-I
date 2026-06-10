from paises import agregar_pais, actualizar_datos, buscar_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas, pedir_entero


GUIONES = '-'*40
print(GUIONES)
print(' '*10+'BIENVENIDOS AL SISTEMA')
print(' '*12+'DE GESTIÓN DE PAISES')


def menu():
    """Menú persistente con las distintas opciones"""
    opcion = 0
    while True:
        print('\n'+GUIONES)
        print(' '*12+'MENU DE OPCIONES')
        print(GUIONES)
        print('1: Agregar un País')
        print('2: Actualizar datos (Población y Superficie)')
        print('3: Buscar un País por nombre')
        print('4: Filtrar Paises')
        print('5: Ordenar Paises')
        print('6: Mostrar Estadísticas')
        print('7: Salir')
        print(GUIONES)
 
        # Solicitamos al usuario que ingrese una opción del menu
        # y verificamos el valor con la funcion pedir_entero
        opcion = pedir_entero('\nIngrese una de las opciones del menú: ', 1)

        # Verificamos que la opción ingreseada no sea mayor a 7
        if opcion > 7:
            print('Error, debe ingresar un valor entre 1 y 7\n')
            continue
        
        # OPCION 7 - SALIR
        if opcion == 7:
            print('Gracias, nos vemos la próxima!')
            break

        # OPCION 1 - AGREGAR UN PAIS       
        if opcion == 1:
            agregar_pais()
         
        # OPCION 2 - ACTUALIZAR DATOS
        if opcion == 2:
            actualizar_datos()

        # OPCION 3 - BUSCAR PAIS POR NOMBRE
        elif opcion == 3:
            buscar_pais()

        # OPCION 4 - FILTRAR PAISES
        elif opcion == 4:
            filtrar_paises()

        # OPCION 5 - ORDENAR PAISES
        elif opcion == 5:
            ordenar_paises()

        # OPCION 6 - MOSTRAR ESTADISTICAS
        elif opcion == 6:
            mostrar_estadisticas()



if __name__ == '__main__':
    menu()