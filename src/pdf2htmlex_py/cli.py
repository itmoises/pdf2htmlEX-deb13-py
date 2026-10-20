"""Command-line entry point."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .engine import Pdf2HtmlExError, build_image, convert, version


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        prog="pdf2htmlEX-deb13-py",
        description="Compila pdf2htmlEX en Debian 13 con Docker y convierte PDF a HTML.",
    )
    root.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    commands = root.add_subparsers(dest="command", required=True)

    build = commands.add_parser("build", help="compilar el motor dentro de Docker")
    build.add_argument("--source", type=Path, required=True, help="raíz del checkout pdf2htmlEX")
    build.add_argument("--tag", default="pdf2htmlex-deb13-py:local")

    conversion = commands.add_parser("convert", help="convertir un PDF a HTML")
    conversion.add_argument("pdf", type=Path)
    conversion.add_argument("-o", "--output", type=Path)
    conversion.add_argument("--tag", default="pdf2htmlex-deb13-py:local")
    conversion.add_argument(
        "--option", action="append", default=[], metavar="ARG",
        help="opción nativa de pdf2htmlEX (repetible), por ejemplo --option=--zoom --option=25",
    )

    commands.add_parser("version", help="mostrar la versión del motor compilado")
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        if args.command == "build":
            build_image(args.source, args.tag)
            print(f"Motor compilado en la imagen Docker: {args.tag}")
        elif args.command == "convert":
            result = convert(args.pdf, args.output, tag=args.tag, options=args.option)
            print(result)
        elif args.command == "version":
            print(version())
        return 0
    except (Pdf2HtmlExError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        if isinstance(exc, KeyboardInterrupt):
            return 130
        print(f"Error durante la operación: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

