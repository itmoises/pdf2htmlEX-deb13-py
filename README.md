# pdf2htmlEX-deb13-py

Interfaz Python para compilar y ejecutar el motor nativo `pdf2htmlEX`. La
conversión mantiene el texto como texto HTML con posición y fuentes, y puede
usar imágenes de fondo para conservar la composición compleja del PDF.

## Requisitos

- Python 3.9 o posterior, disponible como `python` (Windows) o `python3` (macOS).
- Docker Desktop instalado y en ejecución. En Windows, usa el backend WSL 2 recomendado por Docker Desktop.
- Git, para descargar este proyecto y el motor `pdf2htmlEX`.

La compilación ocurre en un contenedor Debian 13 Trixie, así se evita depender de las
versiones de Poppler y FontForge instaladas en el sistema anfitrión. La imagen creada se llama
`pdf2htmlex-deb13-py:local` por defecto.

El constructor instala OpenJDK 21, que está disponible en Trixie, y ajusta el
chequeo de formatos de gettext usado por la versión de FontForge de este
checkout.

## Descargar los proyectos

En una terminal, crea o elige una carpeta de trabajo y descarga ambos repositorios
en carpetas hermanas. Los comandos de Git son iguales en macOS, PowerShell y
Windows Terminal:

```bash
mkdir proyectos
cd proyectos
git clone https://github.com/pdf2htmlEX/pdf2htmlEX.git
git clone https://github.com/itmoises/pdf2htmlEX-deb13-py.git
```

## Instalar y compilar

Entra a `pdf2htmlEX-deb13-py`, crea un entorno virtual y activa el entorno.

### macOS (Terminal)

```bash
cd pdf2htmlEX-deb13-py
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
pdf2htmlEX-deb13-py build --source ../pdf2htmlEX
```

### Windows (PowerShell)

```powershell
cd pdf2htmlEX-deb13-py
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
pdf2htmlEX-deb13-py build --source ..\pdf2htmlEX
```

Si PowerShell bloquea la activación del entorno virtual, permite scripts para la
sesión actual y vuelve a activarlo:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

También puedes usar `cmd.exe` en Windows en lugar de PowerShell. Activa el
entorno con `.venv\Scripts\activate.bat`; los demás comandos son los mismos,
usando `..\pdf2htmlEX` como ruta de origen.

La primera compilación puede tardar varios minutos y necesita conexión a
Internet. También se puede invocar sin instalar el comando usando
`PYTHONPATH=src python -m pdf2htmlex_py.cli ...` en macOS; en PowerShell, usa
`$env:PYTHONPATH = "src"` antes de ejecutar `python -m pdf2htmlex_py.cli ...`.

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
