import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("Text Files/*.txt")
pdf = FPDF(orientation="P", unit='mm', format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem.capitalize()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename, ln=1)

    df = pd.read_csv(filepath, sep='\t', header=None, names=["Info"])
    content = df["Info"].values[0]
    pdf.set_font(family="Times", size=14)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")
