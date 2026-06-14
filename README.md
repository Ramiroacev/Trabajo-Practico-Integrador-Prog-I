# Trabajo-Practico-Integrador-Prog-I
Trabajo Práctico Integrador Final de Programación I - TUPaD - UTN

## Integrantes
* **Acevedo Ramiro** M26 C1-10
* **Nuñez Dario** M26 C1-26

## Descripción del Dataset
El dataset de análisis se encuentra almacenado dentro de la carpeta `/datos` y cuenta con la siguiente información estructurada:
* **Nombre:** (string) Nombre del país.
* **Población:** (int) Cantidad de habitantes del país.
* **Superficie en Km2:** (int) Superficie total del país en km2.
* **Continente:** (string) Nombre del continente al cual pertenece el país.

## Estructura del Proyecto
- `main.py` → archivo principal con el menú
- `modulos/paises.py` → funciones de gestión de países
- `modulos/utilidades.py` → funciones auxiliares
- `datos/paises_dataset.csv` → dataset de países


## Instrucciones de Ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Ramiroacev/Trabajo-Practico-Integrador-Prog-I.git
   ```

2. Ingresar a la carpeta del proyecto:

   ```bash
   cd Trabajo-Practico-Integrador-Prog-I/tp-integrador
   ```

3. Ejecutar el programa:

   ```bash
   python3 proyecto/main.py
   ```

    El mismo generará un Menú interactivo en el cual el usuario podrá generar distintos tipos de
    reportes por pantalla.Ejemplo:
          Ingrese una de las opciones del menú: 3 (Buscar un País por nombre)
          Ingrese el nombre a buscar: Argentina
          
          Salida:
          Nombre: Argentina, Población: 45376763, Superficie: 2780400 km², Continente: América

## Requisitos
* ** Python 3
