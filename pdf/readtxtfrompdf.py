from pypdf import PdfReader
def extract_text_from_pdf(filename):

    reader = PdfReader(filename)
    text = ''
    for i in range(len(reader.pages)):
        text += reader.pages[i].extract_text()
    print(f"Number of Pages: {len(reader.pages)}")
    return text

filename = 'sample.pdf'
text = extract_text_from_pdf(filename)
print(f"  \n Text from file ********** \n {text} \n")

