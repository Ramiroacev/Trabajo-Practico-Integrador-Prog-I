from pathlib import Path
import csv
import unicodedata

# Proyecto portable en Windows y Linux
BASE_DIR = Path(__file__).resolve().parent.parent

# Rutas
ARCHIVO_CSV = BASE_DIR / "datos" / "paises_dataset.csv"
#---------------------------------------------------------
#-------------FUNCIONES AUXILIARES------------------------

def lectura():     #es utilizada  por todas las funciones practicamente
    """Lee el archivo CSV y devuelve una lista de diccionarios."""
    try:                 #intenta tener acceso al archivo con los datos
        with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
            return list(csv.DictReader(archivo, delimiter=';'))   #se utiliza el delimitador ; ya que el csv esta con ese valor
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
        try:            #solo es para validar los numero ingresados
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
        try:                  #valida los nombre de paises ingresados
            nombre = input(mensaje).strip().title()
            if not nombre:
                raise ValueError(f"El nombre del {tipo} no puede estar vacío.")
            if not nombre.replace(" ", "").isalpha():
                raise ValueError(f'El nombre del {tipo} debe contener únicamente letras')

            if tipo == 'pais':
                paises = lectura()
                for pais in paises:
                    if normalizar_texto(nombre) == normalizar_texto(pais['nombre']):
                        raise ValueError(f'El {tipo} ingresado ya se encuentra cargado en la lista')
            return nombre
        except ValueError as e:
            print(f"Error: {e}")

def mostrar_pais(pais):   #evita reiterar codigo cada vez que se impreme resultado en pantalla, 
    """Imprime un país en formato legible"""        #si se quiere cambiar el formato se hace desde aca una sola ves
    print(f"Nombre: {pais['nombre']}, "
          f"Población: {pais['poblacion']}, "
          f"Superficie: {pais['superficie']} km², "
          f"Continente: {pais['continente']}")

def normalizar_texto(texto):
    texto = texto.lower()

    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )