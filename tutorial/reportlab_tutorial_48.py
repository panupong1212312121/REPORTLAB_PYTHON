#tutorial 48
#CREATE WATERMARK IN PDF
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
path_output = r'output/tutorial48.pdf'

pdf=canvas.Canvas(path_output)
pdf.translate(cm, cm)
pdf.drawCentredString(200,600,"lorem ipsum test test NWLERHLWER WERLEWJR")
pdf.rotate(20)
pdf.setFontSize(60)
pdf.drawCentredString(300,30,"by total technology")
pdf.save()