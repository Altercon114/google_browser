import webbrowser
import sys

#Generamos el URL madre de google 
url = "https://www.google.com.mx/search?q="

#Sitios de internet que estarán dentro de la búsqueda
sitios_a_buscar = [
    'reddit.com',
    'stackoverflow.com',
    'stackexchange.com',
    'medium.com'
]

# Windows // Espacio local donde almaceno el .exe de google chrome
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

#creamos filtros para segmentar de forma correcta en el búscador
def crear_filtro():
    filter = '('
    for index, website in enumerate(sitios_a_buscar):
        filter += 'site:' + website
        if index == len(sitios_a_buscar) - 1:
            filter += ')'
        else: 
            filter += ' OR '
    return filter

def crear_busqueda():
    query = sys.argv[1:]
    return ' '.join(query)
                    
def crear_url():
    if len(sys.argv[1:]) == 0: 
        print('Por favor, ingrese un enlace valido')
    else: 
        final_url = url + crear_busqueda() + crear_filtro()
        webbrowser.get(chrome_path).open(final_url)

crear_url()
