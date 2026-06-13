from modulos.paises import agregar_pais, actualizar_datos, buscar_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas, pedir_entero, lectura, mostrar_pais

GUIONES = '-'*40
print(GUIONES)
print(' '*10+'BIENVENIDOS AL SISTEMA')
print(' '*12+'DE GESTIÓN DE PAISES')


def menu():
    """Menú persistente con match-case"""
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

        opcion = pedir_entero('\nIngrese una de las opciones del menú: ', 1)

        match opcion:
            case 1:
                agregar_pais()
            case 2:
                actualizar_datos()
            case 3:
                buscar_pais()
            case 4:
                filtrar_paises()
            case 5:
                ordenar_paises()
            case 6:
                mostrar_estadisticas()
            case 7:
                print('Gracias, nos vemos la próxima!')
                break
            case _:
                print('Error, debe ingresar un valor entre 1 y 7\n')


if __name__ == '__main__':
    menu()
    