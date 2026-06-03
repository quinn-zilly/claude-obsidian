import os
os.environ["TORCH_DEVICE"] = "cuda"

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)
rendered = converter("../.raw/Joshi et al. - 2015 - When Can Women Close the Gap A Meta-Analytic Test of Sex Differences in Performance and Rewards.pdf")
text, _, metadata = text_from_rendered(rendered)

with open("Joshi et al. - 2015 - When Can Women Close the Gap A Meta-Analytic Test of Sex Differences in Performance and Rewards.pdf", "x", encoding="utf-8") as file:
        file.write(text)