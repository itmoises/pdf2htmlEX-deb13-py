# pdf2htmlEX-deb13-py

Interfaz Python para compilar y ejecutar el motor nativo `pdf2htmlEX`. La
conversión mantiene el texto como texto HTML con posición y fuentes, y puede
usar imágenes de fondo para conservar la composición compleja del PDF.

## Requisitos
Tener instalado
- Python 3.9 o posterior
- Docker Desktop instalado y en ejecución

La compilación ocurre en un contenedor Debian 13 Trixie, así se evita depender de las
versiones de Poppler y FontForge instaladas en macOS. La imagen creada se llama
`pdf2htmlex-deb13-py:local` por defecto.

El constructor instala OpenJDK 21, que está disponible en Trixie, y ajusta el
chequeo de formatos de gettext usado por la versión de FontForge de este
checkout.

## Instalar y compilar (Muy sencillo Windows y MacOS)

Crear una carpeta donde se descargará (Con https o ssh):

ejemplo: proyectos, dentro de esa carpeta el git clone descargará los 2 proyectos

git clone https://github.com/pdf2htmlEX/pdf2htmlEX.git
git clone https://github.com/itmoises/pdf2htmlEX-deb13-py.git

Entrar a esta carpeta: pdf2htmlEX-deb13-py 
Ejecutar los comandos

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
 
 
## Límites

Este proyecto es una capa Python y un constructor Docker, no una reescritura en
Python del motor C++. Se apoya en la rama de código fuente indicada por
`--source`. Las fuentes, recursos, licencias y requisitos de esa copia de
`pdf2htmlEX` siguen aplicando (el motor está bajo GPLv3+).
