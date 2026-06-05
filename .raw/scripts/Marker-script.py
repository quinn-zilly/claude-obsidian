#! python3.12

import tkinter as tk
from tkinter import filedialog

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    input_path = filedialog.askopenfilename(
        title="Select input PDF",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
    )
    if not input_path:
        raise SystemExit("No input file selected.")

    output_path = filedialog.asksaveasfilename(
        title="Save Markdown as",
        defaultextension=".md",
        filetypes=[("Markdown files", "*.md"), ("All files", "*.*")],
    )
    if not output_path:
        raise SystemExit("No output file selected.")

    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )

    rendered = converter(input_path)
    text, _, images = text_from_rendered(rendered)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)
