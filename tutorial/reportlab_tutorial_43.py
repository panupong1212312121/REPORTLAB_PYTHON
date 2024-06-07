#tutorial 43
#set bookmark page for pdf file

from reportlab.pdfgen import canvas
path_output = r'output/tutorial43.pdf'

pdf=canvas.Canvas(path_output)
pdf.drawCentredString(50,100,"with bookmark")
pdf.bookmarkPage("page1") # สร้าง bookmark ปลายทาง
pdf.addOutlineEntry("page1 for bookmark","page1") # สร้าง bookmark ต้นทางชื่อ "page1 for bookmark" ซึ่งเวลากดมันจะ navigate ไปยัง bookmark ปลายทางที่ชื่อว่า "page1"
pdf.showPage()
pdf.drawCentredString(10,100,"with bookmark")
pdf.bookmarkPage("page2")
pdf.addOutlineEntry("page2 for bookmark","page2")
pdf.save()