#TUTORIAL 53
#MULTIPLE FRAME WITHIN SAME PAGE

#create two frames side by side  with same height & width 

from reportlab.pdfgen import canvas
from reportlab.platypus import Frame
path_output = r'output/tutorial53.pdf'

pdf=canvas.Canvas(path_output)
flow_obj=[]
frame=Frame(50,150,200,300,showBoundary=1) # สร้างกรอบให้ show เส้นขอบ , มุมซ้ายล่างเริ่มที่ x=50,y=150 โดยกว้าง x สูง : 200 x 300 pixels
frame.addFromList(flow_obj, pdf)
frame=Frame(270,150,200,300,showBoundary=1)
frame.addFromList(flow_obj, pdf)
pdf.save()
