# pyfpdf-grid
I created this Python script to generate a grid with upper-left coordinates to support another project related to laying out components in a PDF with [pypdf](https://github.com/py-pdf/pypdf).

## Description
Creates a grid with upper-left coordinates to lay out components with PyPDF in a separate script.

## Usage
No command-line arguments or input files have been implemented yet. However, you can modify the value of `gridsize` to set the size of the grid. For example:

`gridsize = int(18)` = 0.25 inches (18 pt)

`gridsize = int(36)` = 0.50 inches (72 pt)

## Dependencies

Requires [pypdf](https://github.com/py-pdf/pypdf).

# Outputs

`grid.pdf` an 8.5 x 11 PDF for printing. When printing, do not choose options such as 'fit to paper' otherwise the layout will be off.
