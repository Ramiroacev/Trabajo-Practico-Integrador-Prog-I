from pathlib import Path
import csv
# Proyecto portable en Windows y Linux
BASE_DIR = Path(__file__).resolve().parent.parent

# Rutas
ARCHIVO_CSV = BASE_DIR / "datos" / "paises_dataset.csv"


def lectura():
    """Lee el archivo CSV y devuelve un diccionario."""
    try:
        with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
            return list(csv.DictReader(archivo, delimiter=';'))
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ARCHIVO_CSV}' en el directorio actual.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []

def guardar_paises(paises):
    """Guarda la lista de países completa en el CSV"""
    columnas = ['nombre', 'poblacion', 'superficie', 'continente']

    with open(ARCHIVO_CSV, "w", newline='', encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=columnas, delimiter=';')
        writer.writeheader()
        writer.writerows(paises)

def pedir_entero(mensaje, minimo=0):
    """Verifica que el número ingresado sea válido y persiste hasta que lo sea"""
    while True:
        try:
            numero = int(input(mensaje).strip())

            if numero < minimo:
                print(f'Error, el valor ingresado debe ser mayor o igual a {minimo}')
                continue

            return numero

        except ValueError:
            print('Error, debe ingresar un número válido')


def pedir_nombre(mensaje, tipo):
    """Verifica el nombre ingresado para que no esté vacío, repetido o sea un número"""
    while True:
        try:
            nombre = input(mensaje).strip().title()
            if not nombre:
                raise ValueError(f"El nombre del {tipo} no puede estar vacío.")
            if not nombre.replace(" ", "").isalpha():
                raise ValueError(f'El nombre del {tipo} debe contener únicamente letras')

            if tipo == 'pais':
                paises = lectura()
                for pais in paises:
                    if nombre == pais['nombre']:
                        raise ValueError(f'El {tipo} ingresado ya se encuentra cargado en la lista')

            return nombre
        except ValueError as e:
            print(f"Error: {e}")

def mostrar_pais(pais):   #funcion auxiliar
    """Imprime un país en formato legible"""
    print(f"Nombre: {pais['nombre']}, "
          f"Población: {pais['poblacion']}, "
          f"Superficie: {pais['superficie']} km², "
          f"Continente: {pais['continente']}")