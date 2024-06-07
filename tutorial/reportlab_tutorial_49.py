#tutorial 49
#CREATE PORTRAIT ORIENTATIONS IN PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape
from reportlab.lib.units import cm
path_output = r'output/tutorial48.pdf'

pdf=canvas.Canvas(path_output)
pdf.setPageSize([100,900])
pdf.translate(cm, cm)
pdf.drawCentredString(30,50,"portrait orientation")
pdf.save()
#CREATE LANDSCAPE ORIENTATION IN PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape
from reportlab.lib.units import cm
pdf=canvas.Canvas(path_output,pagesize=letter)
pdf.translate(cm, cm)
pdf.setPageSize(landscape(letter))
pdf.drawCentredString(30,50,"landscape")
pdf.save()

#HOW TO  CREATE LANDSCAPE ORIENTATION WITH CUSTOM SIZE
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape
from reportlab.lib.units import cm
pdf=canvas.Canvas(path_output)
pdf.translate(cm, cm)
pdf.setPageSize([950,550])
pdf.drawCentredString(30,50,"landscape")
pdf.save()



