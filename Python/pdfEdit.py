import PyPDF2 as pf

pdf_file1 = open("MyCV_New1.pdf", 'rb')
pdf_file2 = open("MyCV_New2.pdf", 'rb')
read_file1 = pf.PdfFileReader(pdf_file1)
read_file2 = pf.PdfFileReader(pdf_file2)
writePdf = pf.PdfFileWriter()
# num1=read_file1.numPages
# num2 = read_file2.numPages
#page1 =read_file1.getPage(0).extractText()
writePdf.addPage(read_file1.getPage(0)) #use for loop for multiple pages
writePdf.addPage(read_file2.getPage(0))
output_file = open("outputfile.pdf", 'wb')
writePdf.write(output_file)
output_file.close()
pdf_file1.close()
pdf_file2.close()