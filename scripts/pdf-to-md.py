#! python3.12

import argparse
import sys
from pathlib import Path

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
