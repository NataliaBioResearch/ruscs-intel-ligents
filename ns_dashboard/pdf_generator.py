from fpdf import FPDF
import os

class PDFGenerator(FPDF):
    def header(self):
        # Capçalera opcional
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Informe del Sistema", ln=True, align="C")
        self.ln(5)

    def footer(self):
        # Peu de pàgina amb número
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def add_title(pdf, title):
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, title, ln=True)
    pdf.ln(5)

def add_paragraph(pdf, text):
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, text)
    pdf.ln(3)

def add_image(pdf, image_path, w=180):
    if os.path.exists(image_path):
        pdf.image(image_path, w=w)
        pdf.ln(5)
    else:
        pdf.set_font("Arial", "I", 12)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, f"[Imatge no trobada: {image_path}]", ln=True)
        pdf.set_text_color(0, 0, 0)

def generate_pdf(output_path, sections):
    """
    Genera un PDF amb múltiples seccions.

    Args:
        output_path: ruta del PDF final
        sections: llista de dicts amb:
            {
                "title": "Títol",
                "text": "Paràgraf opcional",
                "image": "ruta opcional a imatge"
            }
    """
    pdf = PDFGenerator()
    pdf.set_auto_page_break(auto=True, margin=15)

    for sec in sections:
        pdf.add_page()

        if "title" in sec:
            add_title(pdf, sec["title"])

        if "text" in sec:
            add_paragraph(pdf, sec["text"])

        if "image" in sec:
            add_image(pdf, sec["image"])

    pdf.output(output_path)
    return output_path
