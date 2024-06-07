#tutorial 36
#create index

#reportlab graphics sub package

path_output = r'output/tutorial36.pdf'

#RECTANGLE DRAWING
from reportlab.graphics import shapes,renderPDF
from reportlab.lib import colors
drawing_obj=shapes.Drawing(500,200) # สร้างหน้ากระดาษเปล่า ยาว x กว้าง : 500 x 200 pixels
drawing_obj.add(shapes.Rect(10,10,250,100,fillColor=colors.blue)) # สร้าง rect โดยมุมซ้ายล่างอยู่ที่ (10,10) & กว้าง x สูง : 250 x 100 
renderPDF.drawToFile(drawing_obj,path_output,msg="tutorial36")

#CIRCLE DRAWING
from reportlab.graphics import shapes,renderPDF
from reportlab.lib import colors
drawing_obj=shapes.Drawing(500,200)
drawing_obj.add(shapes.Circle(100,60,50,fillColor=colors.blue)) # สร้าง circle โดย center อยู่ที่ (100,60) , radius = 50
renderPDF.drawToFile(drawing_obj,path_output,msg="tutorial36")