#tutorial 22
#inline image in paragraph  
from reportlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
path_output = r'output/tutorial22.pdf'

pdf=SimpleDocTemplate(path_output)
flow_object=[]
styles=getSampleStyleSheet()
styles["Normal"].spaceAfter=40 # space ระหว่าง paragraph = 40 pixels
text='''
     this is our logo <img src="logo.jpg" width="50" height="50"/>,hope you guys like it.
     '''
     
p_text=Paragraph(text,style=styles["Normal"])
flow_object.append(p_text)
text='''
     next paragraph with our logo ,<img src="logo.jpg" width="50" height="50"/>.
     '''
p_text=Paragraph(text,style=styles["Normal"])
flow_object.append(p_text)     
pdf.build(flow_object)