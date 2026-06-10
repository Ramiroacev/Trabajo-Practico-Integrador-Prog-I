from pathlib import Path
import csv
import os

# windows y en linux por lo que hace el proyecto portable
BASE_DIR = Path(__file__).resolve().parent.parent

# Rutas
ARCHIVO_CSV = BASE_DIR / "datos" / "paises_dataset.csv"


def agregar_pais():
    """Agregar un país con todos sus datos obligatorios"""
    try:
        pais = pedir_nombre('\nIngrese el nombre del País: ', 'pais')
        poblacion = pedir_entero(f'\nIngrese la población de {pais}: ', 1)
        superficie = pedir_entero(f'\nIngrese la superficie de {pais}: ', 1)
        continente = pedir_nombre(f'\nIngrese el continente al que pertenece {pais}: ', 'continente')
    
    except ValueError as e:
        print(f"Error, {e}")

    nuevo_pais = {
        'nombre': pais,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }

    try:
        columnas = ['nombre', 'poblacion', 'superficie', 'continente']

        with open (ARCHIVO_CSV, 'a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=columnas)

            writer.writerow(nuevo_pais)
            print("Datos guardados correctamente.")

    except PermissionError:
        print(f"Error: El archivo '{ARCHIVO_CSV}' está siendo usado por otro programa. Cérralo e intenta de nuevo.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ARCHIVO_CSV}' en el directorio actual.")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def actualizar_datos():
    """Actualizar datos de superficie o población de un país"""
    pass


def buscar_pais():
    """Buscar un país por nombre con coincidencia total o parcial"""
    pass


def filtrar_paises():
    """Filtrar paises por continente, rango de población, rango de superficie"""
    pass


def ordenar_paises():
    """Ordenar paises por nombre, población, superficie (asc o desc)"""
    pass


def mostrar_estadisticas():
    """Mostrar estadisticas de mayor y menor población, promedio de población y sup. cant. de paises de contintente"""
    pass


def lectura():
    """Lee el archivo CSV y devuelve un diccionario."""
    try:
        with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
            # Guardamos los datos en una lista, ya que al llegar al return, el archivo se cierra
            return list(csv.DictReader(archivo))

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ARCHIVO_CSV}' en el directorio actual.")
        return [] # Devolvemos una lista vacía para evitar que el programa rompa después
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return [] # Devolvemos una lista vacía para evitar que el programa rompa después
    
def pedir_entero (mensaje, minimo=0):
    """Verifica que el número ingresado sea válido"""
    try:
        # Pedimos un número
        numero = int(input(mensaje).strip())
        
        # Verificamos si es menor al minimo recibido por parametro
        if numero < minimo:
            raise ValueError(f'Error, el valor ingresado debe ser mayor a {minimo}')

        # Caso negativo retornamos el valor
        return numero
    
    # Si no es un número entero capturamos el error
    except ValueError:
        print('Error, el valor ingresado debe ser solo un número válido')               

def pedir_nombre (mensaje, tipo):
    """Verifica el nombre ingresado para que el mismo no este vacío, repetido o se haya ingresado un número"""
    nombre = input(mensaje).strip().title()

    # Verificamos si el nombre esta vacío
    if not nombre:
        raise ValueError(f"El nombre del {tipo} no puede estar vacío.")

    # Verificamos que el nombre ingresado sean letras sino generamos un error
    if nombre.isdigit():
        raise ValueError (f'El nombre del {tipo} debe contener solo letras') 

    if tipo == 'pais':
        paises = lectura()

        # Verificamos si el pais ya esta cargado
        for pais in paises:
            if nombre == pais['nombre']:
                # Caso afirmativo generamos un error
                raise ValueError (f'El {tipo} ingresado ya se encuentra caragado en la lista')
    
    return nombre