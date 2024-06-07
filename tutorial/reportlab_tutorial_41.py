#TUTORIAL 41
#how to generate qr code
from reportlab.graphics.barcode import qr
from reportlab.pdfgen import canvas
from reportlab.graphics import shapes,renderPDF,renderPM
path_output = r'output/tutorial41.pdf'
path_output_2 = r'output/tutorial41.png'
path_output_3 = r'output/tutorial41_2.png'

pdf=canvas.Canvas(path_output)
text="www.totaltechnologyabcd.com"
qrcode=qr.QrCodeWidget(text)
drawing_obj=shapes.Drawing()
drawing_obj.add(qrcode)
renderPDF.draw(drawing_obj,pdf,200,200)
pdf.save()

###########################################################################################
 
#how to generate qr code in png
from reportlab.graphics.barcode import qr
from reportlab.graphics import shapes,renderPM
drawing_obj=shapes.Drawing(500,500)
code="www.totaltechnoogy.com"
qrcode=qr.QrCodeWidget(code)
qrcode.barWidth=200 # ขยับไปทางขวาจากจุดเริ่มต้น (มุมซ้ายล่างหน้ากระดาษ) 200 pixels
drawing_obj.add(qrcode)
renderPM.drawToFile(drawing_obj, fn=path_output_2)

###########################################################################################

#generate qrcode using qrcode package

import qrcode
from reportlab.platypus import SimpleDocTemplate,Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

pdf=canvas.Canvas(path_output)
pdf.translate(cm,cm)
flow_obj=[]
code="www.totaltechnoogy123456.com"
qrcode=qrcode.make(code)
qrcode.save(path_output_3)
pdf.drawImage(path_output_3,10,50,800,800)
pdf.save()















