# pdf2htmlEX-deb13-py

Interfaz Python para compilar y ejecutar el motor nativo `pdf2htmlEX`. La
conversión mantiene el texto como texto HTML con posición y fuentes, y puede
usar imágenes de fondo para conservar la composición compleja del PDF.

## Requisitos

- Python 3.9 o posterior
- Docker Desktop instalado y en ejecución
- Un checkout completo de `pdf2htmlEX` (se usa el que está en
  `../pdf2htmlEX` en este espacio de trabajo)
- Conexión a Internet durante la primera compilación para descargar dependencias

La compilación ocurre en un contenedor Debian 13 Trixie, así se evita depender de las
versiones de Poppler y FontForge instaladas en macOS. La imagen creada se llama
`pdf2htmlex-deb13-py:local` por defecto.

El constructor instala OpenJDK 21, que está disponible en Trixie, y ajusta el
chequeo de formatos de gettext usado por la versión de FontForge de este
checkout.

## Instalar y compilar

Desde esta carpeta:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
pdf2htmlEX-deb13-py build --source ../pdf2htmlEX
```

La primera compilación puede tardar varios minutos. También se puede invocar sin
instalar el comando usando `PYTHONPATH=src python -m pdf2htmlex_py.cli ...`.

## Convertir

```bash
pdf2htmlEX-deb13-py convert documento.pdf
pdf2htmlEX-deb13-py convert documento.pdf --output salida/documento.html
pdf2htmlEX-deb13-py convert documento.pdf --option=--zoom --option=25
pdf2htmlEX-deb13-py version
```

Para probar el PDF de ejemplo incluido en esta carpeta:

```bash
pdf2htmlEX-deb13-py convert test.pdf
```

Se produce un HTML y, dependiendo de las opciones del motor, archivos de apoyo
junto a él. Conviene conservarlos con el HTML. Los argumentos `--option` se
reenvían al ejecutable nativo en el orden indicado. Para consultar opciones
adicionales, ejecute el motor dentro de Docker con `--help`.

## Uso desde Python

```python
from pathlib import Path
from pdf2htmlex_py import convert

html = convert(Path("documento.pdf"), Path("salida/documento.html"))
print(html)
```

El motor prioriza conservar la apariencia y los elementos de texto. No puede
reconstruir como HTML semántico la estructura lógica de todos los PDF; PDFs
escaneados conservarán su aspecto, pero no ganarán texto seleccionable mediante
OCR automáticamente.

## Límites

Este proyecto es una capa Python y un constructor Docker, no una reescritura en
Python del motor C++. Se apoya en la rama de código fuente indicada por
`--source`. Las fuentes, recursos, licencias y requisitos de esa copia de
`pdf2htmlEX` siguen aplicando (el motor está bajo GPLv3+).
