import PyPDF2
read_pdf = open("GDP.pdf","rb")
reader_pdf = PyPDF2.PdfFileReader(read_pdf)
num_pages = reader_pdf.numPages
print(num_pages)
convert_pages = reader_pdf.getPage(num_pages-1)
extract_text = convert_pages.extractText()
location = open(r"F:\Python\Python_ENV\woc4.0-eventmanager-krisha-bhataria\PyScripts\GDP.txt","a")
location.writelines(extract_text)
location.close()
