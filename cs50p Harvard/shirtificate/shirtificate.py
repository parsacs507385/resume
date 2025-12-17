from fpdf import FPDF
class Pdf():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align=("c"))
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=60, y=140, txt=f"{name} took CS50!")

    def save(self, file_name):
        self._pdf.output(file_name)


name = str(input("Name: ").strip().title())
pdf = Pdf(name)
pdf.save("shirtificate.pdf")
