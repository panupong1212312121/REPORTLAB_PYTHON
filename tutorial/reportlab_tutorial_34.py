#tutorial 34
#page number

#how to add page number for platypus flowable
from reportlab.platypus import Paragraph,SimpleDocTemplate,PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
path_output = r'output/tutorial34.pdf'

pdf=canvas.Canvas(path_output)
pdf.drawCentredString(300,10,str(pdf.getPageNumber())) # เขียน text ตรงกลางหน้ากระดาษ
pdf.showPage() #สร้างหน้า pdf เปล่าขึ้นมา 
pdf.drawCentredString(300,10,str(pdf.getPageNumber()))
pdf.showPage()
pdf.drawCentredString(300,10,str(pdf.getPageNumber()))
pdf.showPage()
pdf.save()


