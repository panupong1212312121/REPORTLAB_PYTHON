#tutorial 47
#CREATE EDITABLE LISTBOX IN PDF
from reportlab.pdfgen import canvas
from reportlab.lib import colors
path_output = r'output/tutorial47.pdf'

pdf=canvas.Canvas(path_output)
pdf.drawCentredString(40,100,"list box1")
x=pdf.acroForm
x.listbox(value="INDIA", 
          fillColor=colors.lightskyblue, 
          borderColor=colors.black, 
          textColor=colors.red, 
          borderWidth=1, borderStyle="solid", 
          width=100, height=100, 
          x=90, y=80, 
          tooltip="listbox1 example", 
          name="listbox1", 
          options=["AUSTRALIA","USA","UK","INDIA","GERMANY","CANADA","FRANCE","UAE","IRAN","ITALY","PORTUGAL","BELGIUM"])
pdf.save()