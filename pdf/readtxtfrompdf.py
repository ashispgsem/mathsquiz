import PyPDF2

def extract_text_from_pdf(filename):
    with open(filename, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        text = ''
        for page in range(pdf.getNumPages()):
            text += pdf.getPage(page).extractText()
        return text

filename = 'sample.pdf'
text = extract_text_from_pdf(filename)
print(text)
