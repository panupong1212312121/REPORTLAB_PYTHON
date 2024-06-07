#tutorial 14
#textobject word spacing
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

path_output = r'output/tutorial14.pdf'

pdf=canvas.Canvas(path_output,bottomup=0)
pdf.translate(cm, cm)

textobject=pdf.beginText() # สร้างก้อน object สำหรับ text (textobject)
textobject.setTextOrigin(10, 10) # text เริ่มต้นให้ห่างจากขอบซ้ายไป 10 ขอบล่างหรือบนขึ้นกับ bottomup = ? ไป 10 
text="please subscribe to our channel total technology"

for i in range(15):
    textobject.textLine() # เพิ่มบรรทัดใหม่ของข้อความลงในวัตถุข้อความ (textobject)
    textobject.setWordSpace(i+1) # กำหนดระยะห่างระหว่างคำในบรรทัดข้อความ
    
pdf.drawText(textobject)
pdf.save()
