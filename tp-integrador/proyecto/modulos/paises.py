import csv
from modulos.utilidades import lectura, guardar_paises, pedir_entero, pedir_nombre, mostrar_pais
from modulos.utilidades import ARCHIVO_CSV
GUIONES = '-'*40

def agregar_pais():
    """Agregar un país con todos sus datos obligatorios"""
    try:
        pais = pedir_nombre('\nIngrese el nombre del País: ', 'pais')
        poblacion = pedir_entero(f'\nIngrese la población de {pais}: ', 1)
        superficie = pedir_entero(f'\nIngrese la superficie de {pais}: ', 1)
        continente = pedir_nombre(f'\nIngrese el continente al que pertenece {pais}: ', 'continente')

        nuevo_pais = {
            'nombre': pais,
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente
        }

        columnas = ['nombre', 'poblacion', 'superficie', 'continente']

        with open(ARCHIVO_CSV, 'a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=columnas, delimiter=';')
            writer.writerow(nuevo_pais)
            print("Datos guardados correctamente.")

    except PermissionError:
        print(f"Error: El archivo '{ARCHIVO_CSV}' está siendo usado por otro programa. Cérralo e intenta de nuevo.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ARCHIVO_CSV}' en el directorio actual.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def actualizar_datos(): #opcion 2
    """Actualizar datos de superficie o población de un país"""
    paises = lectura()
    if not paises:
        print("No hay datos cargados.")
        return

    nombre = input("Ingrese el nombre del país a actualizar: ").strip().title()
    encontrado = False

    for pais in paises:
        if pais['nombre'] == nombre:
            print(f"Datos actuales de {nombre}: Población={pais['poblacion']}, Superficie={pais['superficie']}")
            pais['poblacion'] = str(pedir_entero("Ingrese nueva población: ", 1))
            pais['superficie'] = str(pedir_entero("Ingrese nueva superficie: ", 1))
            encontrado = True
            break

    if encontrado:
        guardar_paises(paises)
        print("Datos actualizados correctamente.")
    else:
        print("País no encontrado.")


def buscar_pais(): #opcion 3
    """Buscar un país por nombre con coincidencia total o parcial"""
    paises = lectura()
    if not paises:
        print("No hay datos cargados.")
        return

    termino = input("Ingrese el nombre a buscar: ").strip().lower()

    resultados = [
        p for p in paises
        if termino in p['nombre'].lower()
    ]

    if resultados:
        print(GUIONES)
        print(' '*5+'PAISES ENCONTRADOS CON')
        print(' '*5+f'{termino.upper()}')
        print(GUIONES)
        for p in resultados:
            mostrar_pais(p)
    else:
        print("No se encontraron coincidencias.")


def filtrar_paises():   #opcion 4
    """Filtrar paises por continente, rango de población, rango de superficie"""
    paises = lectura()
    if not paises:
        print("No hay datos cargados.")
        return

    print("1: Filtrar por continente")
    print("2: Filtrar por rango de población")
    print("3: Filtrar por rango de superficie")
    opcion = pedir_entero(f"\nElija opción de filtro: ", 1)
    tipo_filtro = ''

    if opcion == 1:
        cont = input("Ingrese continente: ").strip().title()
        filtrados = [p for p in paises if p['continente'] == cont]
        tipo_filtro = 'CONTINENTE'
    elif opcion == 2:
        min_p = pedir_entero("Ingrese población mínima: ", 0)
        max_p = pedir_entero("Ingrese población máxima: ", min_p)
        filtrados = [p for p in paises if min_p <= int(p['poblacion']) <= max_p]
        tipo_filtro = 'POBLACIÓN'
    elif opcion == 3:
        min_s = pedir_entero("Ingrese superficie mínima: ", 0)
        max_s = pedir_entero("Ingrese superficie máxima: ", min_s)
        filtrados = [p for p in paises if min_s <= int(p['superficie']) <= max_s]
        tipo_filtro = 'SUPERFICIE'
    else:
        print("Opción inválida.")
        return

    if filtrados:
        print(GUIONES)
        print(' '*5+'PAISES FILTRADOS POR:')
        print(' '*5+f'{tipo_filtro}')
        print(GUIONES)
        for p in filtrados:
            mostrar_pais(p)
    else:
        print("No se encontraron países con ese criterio.")


def ordenar_paises():   #opcion 5
    """Ordenar paises por nombre, población, superficie (asc o desc)"""
    paises = lectura()
    if not paises:
        print("No hay datos cargados.")
        return

    print("1: Ordenar por nombre")
    print("2: Ordenar por población")
    print("3: Ordenar por superficie")
    opcion = pedir_entero("Elija opción de ordenamiento: ", 1)
    orden = input("Ascendente (A) o Descendente (D)? ").strip().upper()
    tipo = ''
    formato = ''
    reverse = True

    if orden == 'A':
        reverse = False
        formato = 'ASCENDENTE'
    elif orden == 'D':
        reverse = True
        formato = 'DESCENDENTE'

    if opcion == 1:
        paises.sort(key=lambda p: p['nombre'], reverse=reverse)
        tipo = 'NOMBRE'
    elif opcion == 2:
        paises.sort(key=lambda p: int(p['poblacion']), reverse=reverse)
        tipo = 'POBLACIÓN'
    elif opcion == 3:
        paises.sort(key=lambda p: int(p['superficie']), reverse=reverse)
        tipo = 'SUPERFICIE'
    else:
        print("Opción inválida.")
        return
    
    print(GUIONES)
    print(' '*5+'PAISES ORDENDOS POR:')
    print(' '*5+f'{tipo}, {formato}')
    print(GUIONES)
    for p in paises:
        mostrar_pais(p) #print(p)

def mostrar_estadisticas():   #opcion 6
    """Mostrar estadisticas de mayor y menor población, promedio de población y sup. cant. de paises de contintente"""
    paises = lectura()
    if not paises:
        print("No hay datos cargados.")
        return

    poblaciones = [int(p['poblacion']) for p in paises]
    superficies = [int(p['superficie']) for p in paises]

    mayor = max(paises, key=lambda p: int(p['poblacion']))
    menor = min(paises, key=lambda p: int(p['poblacion']))
    promedio_p = sum(poblaciones) / len(poblaciones)
    promedio_s = sum(superficies) / len(superficies)

    # Cantidad de países por continente
    continentes = {}
    for p in paises:
        cont = p['continente']
        continentes[cont] = continentes.get(cont, 0) + 1
    
    print(GUIONES)
    print(' '*10+'ESTADISTICAS')
    print(GUIONES)

    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de población: {promedio_p:.2f}")
    print(f"Promedio de superficie: {promedio_s:.2f}")
    print("Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"{cont}: {cant}")


