import tkinter as tk
from pathlib import Path
from tkinter import filedialog

from markitdown import MarkItDown
from openrouter import OpenRouter

import os
from dotenv import load_dotenv



if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    input_path = filedialog.askopenfilename(
        title="Select input PDF",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
    )
    if not input_path:
        raise SystemExit("No input file selected.")

    output_path = Path(__file__).resolve().parent.parent / (Path(input_path).stem + ".md")

load_dotenv()

md = MarkItDown(
    enable_plugins=True,
    llm_client=OpenRouter(
    api_key=os.getenv('openrouter_key')
    ),
    llm_model="openrouter/free",
)
result = md.convert(input_path)

with open(output_path, "w", encoding="utf-8") as file:
    file.write(result.text_content)