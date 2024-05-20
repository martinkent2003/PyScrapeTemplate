from fpdf import FPDF

#create FPDF object
#layout ('P','L') = (portrait, landscape)
#unit ('mm','cm','in') = unit of measurement
#format ('A3','A4' (default),'A5','Letter','Legal') = paper format
pdf = FPDF('P','mm','Letter')

# Add a page    
pdf.add_page()

# set font
# font ('Arial', 'Times', 'Courier', 'Helvetica', 'Symbol', 'ZapfDingbats')
# style ('', 'B', 'I', 'U') = (regular, bold, italic, underline)
pdf.set_font('helvetica', '', 16)

#add text
#w = width
#h = height
pdf.cell(40,100,'Hello World!', ln = True, border=True)
pdf.cell(80, 10, 'Goodbye World')

pdf.output('pdfSample1.pdf')