#Crear un código que nos permita almacenar los enlaces de nuestras páginas preferidas

import sys
import webbrowser

#Sitios de internet que estarán dentro de la búsqueda

sitios_favoritos = [
    'https://www.youtube.com/',  # 0
    'https://space.bilibili.com/526489877/',  # 1
    'https://campusvirtual.mexico.unir.net/my/', #2
    'https://chat.openai.com/', # 3
    'https://www.youtube.com/@News_ABEMA' # 4
]

# Ruta al ejecutable de Google Chrome en Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def seleccionar_pagina():
    if len(sys.argv) != 2:
        print("Por favor, ingrese un índice válido.")
        return None
    indice_deseado = int(sys.argv[1])
    if 0 <= indice_deseado < len(sitios_favoritos):
        return sitios_favoritos[indice_deseado]
    else:
        print("Ese índice no existe.")
        return None

def generar_busqueda():
    final_url = seleccionar_pagina()
    if final_url:
        webbrowser.get(chrome_path).open(final_url)


generar_busqueda()
