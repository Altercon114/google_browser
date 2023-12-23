#Crear un código que nos permita almacenar los enlaces de nuestras páginas preferidas

import sys
import webbrowser
import pickle

# Lista original
# sitios_favoritos_original = [
#     ('https://www.youtube.com/', 'Youtube'),
#     ('https://space.bilibili.com/526489877/', 'Calendario Google'),
#     ('https://chat.openai.com/', 'ChatGPT'),
#     ('https://drive.google.com/drive/my-drive', 'Mi Drive'),
# ]

# Función para cargar la lista desde un archivo
def cargar_lista():
    try:
        with open('sitios_favoritos.pkl', 'rb') as file:
            lista_cargada = pickle.load(file)
            if not lista_cargada:
                return []
            return lista_cargada
    except FileNotFoundError:
        return []

# Función para guardar la lista en un archivo
def guardar_lista(lista):
    try:
        with open('sitios_favoritos.pkl', 'wb') as file:
            pickle.dump(lista, file)
    except Exception as e:
        print(f"Error al guardar la lista: {e}")

# Inicializar la lista
sitios_favoritos = cargar_lista()

# Ruta al ejecutable de Google Chrome en Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def seleccionar_pagina(indice_deseado):
    cantidad_sitios = len(sitios_favoritos)
    if 0 <= indice_deseado < cantidad_sitios:
        return sitios_favoritos[indice_deseado][0]
    else:
        print(f"Ese índice no existe. Debe ser un número entre 0 y {cantidad_sitios-1}.")
        return None

def generar_busqueda():
    indice_deseado = int(sys.argv[1])
    final_url = seleccionar_pagina(indice_deseado)
    if final_url:
        webbrowser.get(chrome_path).open(final_url)

def imprimir_lista():
    for index, (enlace, descripcion) in enumerate(sitios_favoritos):
        print(f"{index}: {descripcion}")

def agregar_sitio(enlace, descripcion):
    sitios_favoritos.append((enlace, descripcion))
    guardar_lista(sitios_favoritos)
    print(f"Se agregó el sitio: {descripcion} ({enlace})")

def eliminar_sitio(indice):
    if 0 <= indice < len(sitios_favoritos):
        sitio_eliminado = sitios_favoritos.pop(indice)
        guardar_lista(sitios_favoritos)
        print(f"Se eliminó el sitio: {sitio_eliminado[1]} ({sitio_eliminado[0]})")
    else:
        print(f"Ese índice no existe. Debe ser un número entre 0 y {len(sitios_favoritos)-1}.")

def cambiar_nombre_sitio(indice, nuevo_nombre):
    if 0 <= indice < len(sitios_favoritos):
        viejo_nombre = sitios_favoritos[indice][1]
        sitios_favoritos[indice] = (sitios_favoritos[indice][0], nuevo_nombre)
        guardar_lista(sitios_favoritos)
        print(f"Se cambió el nombre del sitio: {viejo_nombre} a {nuevo_nombre}")
    else:
        print(f"Ese índice no existe. Debe ser un número entre 0 y {len(sitios_favoritos)-1}.")

def cambiar_direccion_sitio(indice,nuevo_enlace):
    if 0 <= indice < len(sitios_favoritos):
        viejo_enlace = sitios_favoritos[indice][0]
        sitios_favoritos[indice] = (nuevo_enlace, sitios_favoritos[indice][1])
        guardar_lista(sitios_favoritos)
        print(f"Se cambió el nombre del sitio: {viejo_enlace} a {nuevo_enlace}")
    else:
        print(f"Ese índice no existe. Debe ser un número entre 0 y {len(sitios_favoritos)-1}.")

# Verificar si se proporcionaron argumentos desde la terminal
if len(sys.argv) > 1:
    comando = sys.argv[1].lower()

    if comando == 'agregar':
        # Verificar si se proporcionaron suficientes argumentos para agregar un sitio
        if len(sys.argv) == 4:
            enlace_nuevo = sys.argv[2]
            descripcion_nueva = sys.argv[3]
            agregar_sitio(enlace_nuevo, descripcion_nueva)
        else:
            print("Por favor, proporcione un enlace y una descripción para agregar.")
    elif comando == 'eliminar':
        # Verificar si se proporcionó un índice para eliminar un sitio
        if len(sys.argv) == 3:
            indice_eliminar = int(sys.argv[2])
            eliminar_sitio(indice_eliminar)
        else:
            print("Por favor, proporcione el índice del sitio que desea eliminar.")
    elif comando == 'cambiar_nombre':
        # Verificar si se proporcionaron suficientes argumentos para cambiar el nombre de un sitio
        if len(sys.argv) == 4:
            indice_cambiar_nombre = int(sys.argv[2])
            nuevo_nombre = sys.argv[3]
            cambiar_nombre_sitio(indice_cambiar_nombre, nuevo_nombre)
        else: 
            print('Por favor, proporcione el índice del sitio que desea cambiar el nombre.')
    elif comando == 'cambiar_direccion':
        # Verificar si se proporcionaron suficientes argumentos para cambiar el enlace del sitio
        if len(sys.argv) == 4:
            indice_cambiar_direccion = int(sys.argv[2])
            nueva_direccion = sys.argv[3]
            cambiar_direccion_sitio(indice_cambiar_direccion,nueva_direccion)
        else:
            print('Por favor, proporcione el índice del sitio que desea cambiar la dirección.')
    elif comando in ['lista']:
        imprimir_lista()
    else:
        generar_busqueda()
else:
    imprimir_lista()
