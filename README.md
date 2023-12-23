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

# google_browser
Repository that contains the code that allows doing optimized google searches trhough the terminal 

## Where does this idea come from?: 

This code comes from this video:
https://www.youtube.com/watch?v=6wwHv-cyOd0
