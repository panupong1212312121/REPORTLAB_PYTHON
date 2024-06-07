#tutorial 16
#INTRODUCTION TO PLATYPUS
from reportlab.platypus import Spacer,SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet

path_output = r'output/tutorial16.pdf'

pdf_file=SimpleDocTemplate(path_output) # ต่างกับ class canvas คือ x,y เริ่มจากข้างบน 
flow=[]
styles=getSampleStyleSheet()
text="sample text"
par_text=Paragraph("sample text1",styles["Normal"])
flow.append(par_text)
flow.append(Spacer(1,20)) # ระยะห่างระหว่าง text โดยห่างในแนวแกน x:1 pixel , แกน y:20 pixels
par_text=Paragraph("sample text2",styles["Normal"])
flow.append(par_text)
flow.append(Spacer(1,40))
par_text=Paragraph("sample text3",styles["Normal"])
flow.append(par_text)
pdf_file.build(flow)




