#!/usr/bin/env python3.12

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

if __name__ == '__main__':
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )

input_path = "input.pdf"
output_path = "output.md"


rendered = converter(input_path)
text, _, images = text_from_rendered(rendered)

with open(output_path, "x", encoding="utf-8") as file:
    file.write(text)