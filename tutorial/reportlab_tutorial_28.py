#tutorial 28
#table

#create table with span
from reportlab.platypus import Paragraph,SimpleDocTemplate,Table,TableStyle
from reportlab.lib import colors

path_output = r'output/tutorial28.pdf'

pdf=SimpleDocTemplate(path_output)
flow_obj=[]
data=[[1,2,3,4,5],
      [1,2,3,4,5]]
table=Table(data)
tstyle=TableStyle([("BACKGROUND",(0,0),(-1,-1),colors.red),
                   ("GRID",(0,0),(-1,-1),1,colors.black),
                   ("SPAN",(0,0),(-4,-2)), # "SPAN" : merge cell พิกัด (0,0) ถึง (-4,-2)
                   ("SPAN",(3,0),(-1,-2))])
table.setStyle(tstyle)
flow_obj.append(table)
pdf.build(flow_obj)



 
