import PyPDF2

def extract_pages(pdf_path, start_page, end_page, output_file):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        # Extract the specified range of pages
        with open(output_file, 'w', encoding='utf-8') as output:
            for page_num in range(start_page - 1, end_page):
                # Extract the text from each page
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    output.write(text)
                    output.write("\n")

# Define your PDF path and the page ranges based on your birth date and year
pdf_path = 'Harry_Potter_(www.ztcprep.com).pdf'

#my birthday is September 15, 1998

# Extract for file1.txt
extract_pages(pdf_path, 3108, 3118, 'file1.txt')

# Extract for file2.txt
extract_pages(pdf_path, 3192, 3202, 'file2.txt')

print("Pages extracted and saved to file1.txt and file2.txt")