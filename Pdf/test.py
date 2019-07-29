# importing required modules 
import PyPDF2 
  
 
pdfFileObj = open('test.pdf', 'rb') 
  
 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
newFile = open('output.pdf','wb')
pdfWriter =PyPDF2.PdfFileWriter()
  
 
print(pdfReader.numPages) 
  
for page in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(page)
    pdfWriter.addPage(pageObj)
    #print(pageObj.extractText()) 


pdfWriter.write(newFile)  

pdfFileObj.close() 
newFile.close()