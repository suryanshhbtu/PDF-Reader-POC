import fitz  # PyMuPDF
import os
from datetime import datetime

def pdf_to_text_with_pymupdf(pdf_path, output_txt_path):
    print("Extracting text using PyMuPDF...")
    
    # Open the PDF file
    doc = fitz.open(pdf_path)
    full_text = ""

    # Loop through each page
    for page_num in range(len(doc)):
        print(f"Extracting page {page_num + 1}...")
        page = doc.load_page(page_num)
        text = page.get_text()
        full_text += f"\n--- Page {page_num + 1} ---\n{text}\n"

    # Write the extracted text to a .txt file
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(full_text)

    print(f"Text successfully written to {output_txt_path}")

# Example usage
if __name__ == "__main__":
    input_pdf = "../report.pdf"  # Replace with your actual PDF path
    
    # Create output directory if it doesn't exist
    output_dir = "../outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Generate timestamped output file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_txt = os.path.join(output_dir, f"output_text_pymupdf_{timestamp}.txt")

    pdf_to_text_with_pymupdf(input_pdf, output_txt)
