#tutorial 18
#Intra paragrpah mark-up

#with underline & strikethrough markup 

from reportlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

path_output = r'output/tutorial19.pdf'

pdf=SimpleDocTemplate(path_output)
flow_object=[]
styles=getSampleStyleSheet()
text='''
     this is normal text with out <strike>strike</strike> and <u>underline</u>.
     '''
paragraph_text=Paragraph(text,style=styles["Normal"])
flow_object.append(paragraph_text)
pdf.build(flow_object)

# strike : ขีดค่า 