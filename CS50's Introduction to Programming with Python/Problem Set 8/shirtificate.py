from fpdf import FPDF

pdf = FPDF(orientation = "P", format = "A4")
pdf.add_page()
pdf.set_auto_page_break
pdf.image("shirtificate.png")
pdf.set_text_color("#OOOOOO")
pdf.cell(30,10,"CS50 Shirtificate",border=1,align="C")
pdf.set_text_color("#FFFFFF")
pdf.output("shirtificate.pdf")
