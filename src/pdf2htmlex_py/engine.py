"""Build and run pdf2htmlEX using a local Docker installation."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Sequence


class Pdf2HtmlExError(RuntimeError):
    """Raised when the builder or native converter fails."""


def _docker() -> str:
    executable = shutil.which("docker")
    if not executable:
        raise Pdf2HtmlExError(
            "Docker no está instalado o no está en PATH. Instala Docker Desktop y vuelve a intentarlo."
        )
    return executable


def _ensure_docker_running() -> str:
    executable = _docker()
    result = subprocess.run(
        [executable, "info"], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise Pdf2HtmlExError(
            "Docker está instalado, pero el daemon no está disponible. "
            "Abre Docker Desktop, espera a que indique que está en ejecución "
            "y vuelve a lanzar el comando."
        )
    return executable


IMAGE_TAG = "pdf2htmlex-deb13-py:local"


def build_image(source: Path, tag: str = IMAGE_TAG) -> None:
    """Compile the supplied pdf2htmlEX source tree inside a Linux container."""
    source = source.expanduser().resolve()
    if not (source / "buildScripts/buildInstallLocallyApt").is_file():
        raise Pdf2HtmlExError(
            f"No encuentro buildScripts/buildInstallLocallyApt en {source}. "
            "Indica la raíz de un checkout completo de pdf2htmlEX con --source."
        )
    dockerfile = Path(__file__).resolve().parents[2] / "Dockerfile.builder"
    command = [_ensure_docker_running(), "build", "--tag", tag, "--file", str(dockerfile), str(source)]
    subprocess.run(command, check=True)


def convert(
    pdf: Path,
    output: Path | None = None,
    *,
    tag: str = IMAGE_TAG,
    options: Sequence[str] = (),
) -> Path:
    """Convert a PDF and return the resulting HTML path."""
    pdf = pdf.expanduser().resolve()
    if not pdf.is_file():
        raise Pdf2HtmlExError(f"No existe el PDF: {pdf}")
    if pdf.suffix.lower() != ".pdf":
        raise Pdf2HtmlExError(f"El archivo debe tener extensión .pdf: {pdf}")

    output = (output or pdf.with_suffix(".html")).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        _ensure_docker_running(), "run", "--rm", "--network", "none",
        "--mount", f"type=bind,src={pdf.parent},dst=/input,readonly",
        "--mount", f"type=bind,src={output.parent},dst=/output",
        "--workdir", "/output",
        "--entrypoint", "pdf2htmlEX", tag,
        *options,
        f"/input/{pdf.name}", output.name,
    ]
    subprocess.run(command, check=True)
    if not output.is_file():
        raise Pdf2HtmlExError(f"La conversión terminó, pero no se creó {output}")
    return output


def version(tag: str = IMAGE_TAG) -> str:
    """Return the engine version from the locally built image."""
    result = subprocess.run(
        [_ensure_docker_running(), "run", "--rm", "--network", "none", "--entrypoint", "pdf2htmlEX", tag, "--version"],
        check=True,
        capture_output=True,
        text=True,
    )
    return (result.stdout or result.stderr).strip()

