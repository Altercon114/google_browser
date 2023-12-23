# Script de Gestión de Sitios Favoritos

Este script de Python facilita la gestión de una lista de sitios favoritos, brindando la capacidad de agregar, eliminar, cambiar el nombre y cambiar la dirección de los sitios. También puede mostrar la lista de sitios favoritos y abrir un sitio específico en el navegador.

## Requisitos

- Python 3.x
- Google Chrome (o ajustar la ruta del ejecutable del navegador según sea necesario)

## Uso

### Ejecutar el Script

\```bash
python script.py <comando> [argumentos]
\```

### Comandos Disponibles

- **\`agregar\`**: Agrega un nuevo sitio a la lista.
  \```bash
  python script.py agregar <enlace> <descriptivo>
  \```

- **\`eliminar\`**: Elimina un sitio de la lista.
  \```bash
  python script.py eliminar <índice>
  \```

- **\`cambiar_nombre\`**: Cambia el nombre de un sitio en la lista.
  \```bash
  python script.py cambiar_nombre <índice> <nuevo_nombre>
  \```

- **\`cambiar_direccion\`**: Cambia la dirección de un sitio en la lista.
  \```bash
  python script.py cambiar_direccion <índice> <nueva_direccion>
  \```

- **\`lista\`** (o **\`l\`**, **\`list\`**): Muestra la lista de sitios favoritos.
  \```bash
  python script.py lista
  \```

- Sin comando: Muestra la lista de sitios favoritos y abre un sitio específico en el navegador.
  \```bash
  python script.py
  \```

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras errores o tienes sugerencias de mejoras, siéntete libre de abrir un problema o enviar un pull request.

# google_browser.py

**Description:**
This Python script performs a Google search with specific websites as search filters. It opens the search results in Google Chrome.

**Requirements:**
- Python 3.x
- Google Chrome (or adjust the browser executable path as needed)

**Usage:**
### Run the Script

bash python google_browser.py [search_query]

**Detalles del Script:**
El script genera una URL de búsqueda de Google basada en una consulta de búsqueda proporcionada y filtra los resultados a sitios web específicos.

- **Estructura de la URL:** La URL base para la búsqueda en Google se establece en `https://www.google.com.mx/search?q=`.
- **Sitios Web a Buscar:** El script filtra los resultados de búsqueda para sitios web específicos enumerados en el array `sitios_a_buscar`.
- **Ruta de Chrome:** La ruta al ejecutable de Google Chrome en Windows se establece como `C:/Program Files/Google/Chrome/Application/chrome.exe %s`.

**Funciones:**
- **`crear_filtro()`:** Crea una cadena de filtro para sitios web específicos en la consulta de búsqueda.
- **`crear_busqueda()`:** Obtiene la consulta de búsqueda de los argumentos de la línea de comandos.
- **`crear_url()`:** Genera la URL final de búsqueda en Google con la consulta y el filtro y la abre en Google Chrome.

**Ejemplo:**
Para buscar una consulta y filtrar los resultados para sitios web específicos, ejecuta:

bash python google_browser.py tutoriales de python

Esto realizará una búsqueda en Google de "tutoriales de python" con los resultados filtrados para los sitios web especificados.


## Contribuciones:
¡Las contribuciones son bienvenidas! Si encuentras errores o tienes sugerencias de mejora, no dudes en abrir un problema o enviar una solicitud de extracción.

