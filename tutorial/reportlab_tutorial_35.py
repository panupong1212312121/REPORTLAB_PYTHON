#tutorial 35
#create index

#how to generate single word index

from reportlab.platypus import Paragraph,SimpleDocTemplate,PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.tableofcontents import SimpleIndex
from reportlab.platypus.paragraph import Paragraph
path_output = r'output/tutorial35.pdf'

pdf=SimpleDocTemplate(path_output)
flow_obj=[]
styles=getSampleStyleSheet()
text="""
this is sample <index item="index"/> without index
"""
p_text=Paragraph(text,style=styles["Normal"])

text1="""
this is sample <index item="reportlab"/> with reportlab index
"""
p_text1=Paragraph(text1,style=styles["Normal"])

text2="""

this is sample <index item="flowable"/> flowable index
"""
p_text2=Paragraph(text2,style=styles["Normal"])

index=SimpleIndex()
for i in range(1,4):
    flow_obj.append(p_text)
    flow_obj.append(PageBreak()) # PageBreak() ขึ้นหน้าใหม่
 
for i in range(1,4):
    flow_obj.append(p_text1)
    flow_obj.append(PageBreak())
 
for i in range(1,4):
    flow_obj.append(p_text2)
    flow_obj.append(PageBreak())

flow_obj.append(index)
pdf.build(flow_obj,canvasmaker=index.getCanvasMaker())