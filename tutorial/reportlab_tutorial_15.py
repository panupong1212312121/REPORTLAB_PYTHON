#tutorial 15
#textobject setrise
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

path_output = r'output/tutorial15.pdf'

pdf=canvas.Canvas(path_output,bottomup=0)
pdf.translate(cm, cm)
textobject=pdf.beginText()
textobject.setTextOrigin(10, 10)
text="demo"
textobject.textOut(text) # textOut แสดงข้อความใน textObject 
textobject.setRise(5) # set ให้ text ต่อจากนี้สูงขึ้นจาก normal line 5 pixels
textobject.textOut("superscript")
textobject.setRise(0) # set ให้ text ต่อจากนี้สูงขึ้นจาก normal line 0 pixels
textobject.textOut("and")
textobject.setRise(-5) # set ให้ text ต่อจากนี้สูงขึ้นจาก normal line -5 pixels
textobject.textOut("subscript")
pdf.drawText(textobject)
pdf.save()


