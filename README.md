# pdf2htmlEX-deb13-py

Interfaz Python para compilar y ejecutar el motor nativo `pdf2htmlEX`. La
conversión mantiene el texto como texto HTML con posición y fuentes, y puede
usar imágenes de fondo para conservar la composición compleja del PDF.

## Requisitos

- Python 3.9 o posterior, disponible como `python` (Windows) o `python3` (macOS).
- Docker Desktop instalado y en ejecución. En Windows, usa el backend WSL 2 recomendado por Docker Desktop.
- Git, para descargar este proyecto y el motor `pdf2htmlEX`.

### Descargar e instalar los requisitos

- **Python:** [python.org/downloads](https://www.python.org/downloads/). Descarga el instalador para tu sistema operativo. En Windows, durante la instalación marca **Add Python to PATH** si aparece esa opción.
- **Docker Desktop para macOS:** [guía e instalador oficial](https://docs.docker.com/desktop/setup/install/mac-install/). Elige la versión para Apple silicon o Intel según tu Mac.
- **Docker Desktop para Windows:** [guía e instalador oficial](https://docs.docker.com/desktop/setup/install/windows-install/). Se recomienda el backend WSL 2.
- **Git:** [git-scm.com/downloads](https://git-scm.com/downloads). Git es opcional si descargas los proyectos como ZIP.

Después de instalar Docker Desktop, ábrelo y espera a que indique que Docker está en ejecución antes de continuar.

La compilación ocurre en un contenedor Debian 13 Trixie, así se evita depender de las
versiones de Poppler y FontForge instaladas en el sistema anfitrión. La imagen creada se llama
`pdf2htmlex-deb13-py:local` por defecto.

El constructor instala OpenJDK 21, que está disponible en Trixie, y ajusta el
chequeo de formatos de gettext usado por la versión de FontForge de este
checkout.

## Descargar los proyectos

Descarga los dos proyectos dentro de una misma carpeta de trabajo, de modo que
queden como carpetas hermanas. Puedes usar Git o descargar los ZIP directamente.

### Opción A: con Git

Instala Git desde el enlace anterior y ejecuta estos comandos en Terminal
(macOS) o PowerShell/Windows Terminal (Windows):

```bash
mkdir proyectos
cd proyectos
git clone https://github.com/pdf2htmlEX/pdf2htmlEX.git
git clone https://github.com/itmoises/pdf2htmlEX-deb13-py.git
```

### Opción B: descarga directa, sin Git

Descarga los ZIP desde GitHub:

- [Motor pdf2htmlEX (ZIP)](https://github.com/pdf2htmlEX/pdf2htmlEX/archive/refs/heads/master.zip)
- [Interfaz pdf2htmlEX-deb13-py (ZIP)](https://github.com/itmoises/pdf2htmlEX-deb13-py/archive/refs/heads/main.zip)

Extrae ambos ZIP dentro de la misma carpeta `proyectos`. GitHub agrega el nombre
de la rama al nombre de cada carpeta extraída; renómbralas a `pdf2htmlEX` y
`pdf2htmlEX-deb13-py`, respectivamente, para que coincidan con los comandos de
esta guía. La estructura debe quedar así:

```text
proyectos/
├── pdf2htmlEX/
└── pdf2htmlEX-deb13-py/
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
