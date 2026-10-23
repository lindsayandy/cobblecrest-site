import sys, glob
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter

def font(name, pat):
    f = glob.glob(f"/usr/share/fonts/**/{pat}", recursive=True)
    if f: pdfmetrics.registerFont(TTFont(name, f[0])); return name
    return None
reg = font("Carlito", "Carlito-Regular.ttf") or "Helvetica"
bold = font("Carlito-Bold", "Carlito-Bold.ttf") or "Helvetica-Bold"

def notice_pdf(title, out):
    h = ParagraphStyle("h", fontName=bold, fontSize=16, leading=20, spaceAfter=12)
    b = ParagraphStyle("b", fontName=reg, fontSize=12, leading=17, spaceAfter=10)
    doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=72, rightMargin=72, topMargin=90, bottomMargin=72,
                            title=f"{title} - Fan Content notice")
    doc.build([
        Paragraph("Fan Content Notice", h),
        Paragraph(f"<i>{title}</i> is unofficial Fan Content permitted under the Fan Content Policy. "
                  "Not approved/endorsed by Wizards. Portions of the materials used are property of "
                  "Wizards of the Coast. ©Wizards of the Coast LLC.", b),
        Paragraph("This guide is free to read and share. Published by Cobblecrest Chronicles, LLC. "
                  "More at cobblecrestchronicles.com.", b),
    ])

src, title, out, tmp = sys.argv[1:5]
notice_pdf(title, tmp)
r = PdfReader(src); n = PdfReader(tmp).pages[0]
w = PdfWriter()
w.add_page(r.pages[0]); w.add_page(n)
for p in r.pages[1:]: w.add_page(p)
w.add_metadata({"/Title": title, "/Author": "Cobblecrest Chronicles, LLC"})
with open(out, "wb") as f: w.write(f)
print(out, len(PdfReader(out).pages), "pages")
