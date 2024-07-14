from fpdf import FPDF
from fpdf import Align

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 48)
pdf.cell(40, 50, "CS50 Shirtificate", align='C', center=True)
pdf.image("shirtificate.png", x=Align.C, y=80)
pdf.set_font("helvetica", size=24)
pdf.set_text_color(255, 255, 255)
pdf.cell(40, 280, f"{name} took CS50", align='C', center=True)
pdf.output("shirtificate.pdf")
