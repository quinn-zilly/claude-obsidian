#!/usr/bin/env python3
"""Convert a PDF in .raw/input/ to markdown in .raw/output/ using marker.

marker is only installed in the Python 3.12 interpreter at the path below.
Whatever interpreter launches this script (python, python3, py, Cowork's
sandboxed default), the bootstrap block re-execs under that 3.12 interpreter so
`import marker` always succeeds. Override the target with env PDF_TO_MD_PYTHON.
"""

import os
import sys
from pathlib import Path

# --- bootstrap: re-exec under the Python 3.12 install that has marker ---
_DEFAULT_PY312 = r"C:\Users\quinn\AppData\Local\Programs\Python\Python312\python.exe"
_TARGET_PY = os.environ.get("PDF_TO_MD_PYTHON", _DEFAULT_PY312)


def _resolved(p: str) -> str:
    try:
        return os.path.realpath(p).lower()
    except OSError:
        return (p or "").lower()


if _resolved(sys.executable) != _resolved(_TARGET_PY):
    if not os.path.isfile(_TARGET_PY):
        sys.stderr.write(
            "Error: Python 3.12 interpreter with marker not found at:\n"
            f"  {_TARGET_PY}\n"
            "Set env PDF_TO_MD_PYTHON to the correct python.exe, or install "
            "marker there (py -3.12 -m pip install marker-pdf).\n"
        )
        sys.exit(1)
    # Replace current process; stdout/stderr/exit code pass straight through.
    os.execv(_TARGET_PY, [_TARGET_PY, os.path.abspath(__file__), *sys.argv[1:]])
# --- end bootstrap (only the 3.12 interpreter reaches past this point) ---

import argparse

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a PDF in .raw/input/ to markdown in .raw/output/")
    parser.add_argument("input", help="PDF filename inside .raw/input/ (e.g. Campbell.pdf)")
    parser.add_argument("output", help="Markdown filename to create in .raw/output/ (e.g. Campbell.md)")
    args = parser.parse_args()

    root = Path(__file__).parent.parent
    input_path = root / ".raw" / "input" / args.input
    output_path = root / ".raw" / "output" / args.output

    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    converter = PdfConverter(artifact_dict=create_model_dict())
    rendered = converter(str(input_path))
    text, _, images = text_from_rendered(rendered)

    with open(output_path, "x", encoding="utf-8") as f:
        f.write(text)

    print(f"Converted: .raw/input/{args.input} → .raw/output/{args.output}")
