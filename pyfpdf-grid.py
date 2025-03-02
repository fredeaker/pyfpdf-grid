# Filename: pyfpdf-grid.py
# Author: Fred Eaker (fredeaker.com | https://github.com/fredeaker)
# Description: Creates a grid with upper-left coordinates for the purpose of
# laying out components with PyPDF in a seperate script.
# Usage: No command-line arguments or input files have been implemented yet.
# However you, can modify the value of gridsize to set the size of the grid.
# For example:
#
# gridsize = int(18) = 0.25 inches (18 pt)
# gridsize = int(36) = 0.50 inches (72 pt)
#
# Dependencies: Requires PyFPDF (https://pypi.org/project/fpdf/)
#
# Outputs: grid.pdf an 8.5 x 11 PDF for printing. When printing, do not choose
# options such as 'fit to paper' otherwise the layout will be off.
#
# License: GNU General Public License v3.0

from fpdf import FPDF

pdf = FPDF(orientation = 'P', unit = 'pt', format = 'Letter')
pdf.set_margins(0, 0, 0) # left, top, right
pdf.add_page()
pdf.set_font('helvetica', '', 4)
pdf.set_auto_page_break(True, int(0))

gridsize = int(18) # 0.25 inches = 18 pt
pagewidth = int(612) - gridsize # 8.5 inches = 612 pt
pageheight = int(792) - gridsize ## 11 inches = 792 pt

x = int(0)
y = int(0)

pdf.set_x(x)
pdf.set_y(y)

while (y <= pageheight):
	while (x <= pagewidth):
		pdf.cell(gridsize, gridsize, str(x) + ',' + str(y), 1) # w, h, txt, border
		x += gridsize
		pdf.set_x(x)
		# print(str(x) + ' x ' + str(y)) # debug print coordinates in console
	y += gridsize
	x = int(0)
	pdf.set_y(y)

pdf.output('grid.pdf')