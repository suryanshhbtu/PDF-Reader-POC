from pdf2image import convert_from_path
import pytesseract
import os
from datetime import datetime

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

# Set path to tessdata directory
os.environ['TESSDATA_PREFIX'] = r"D:\Program Files\Tesseract-OCR\tessdata"

def pdf_to_text(pdf_path, output_txt_path):
    # Convert PDF pages to images
    print("Converting PDF pages to images...")
    images = convert_from_path(
    pdf_path,
    poppler_path=r"D:\Program Files\Poppler\poppler-24.08.0\Library\bin")


    full_text = ""

    # Loop through images and apply OCR
    for i, image in enumerate(images):
        print(f"OCR on page {i+1}...")
        text = pytesseract.image_to_string(image)
        full_text += f"\n--- Page {i+1} ---\n{text}\n"

    # Write the full text to a .txt file
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(full_text)

    print(f"Text successfully written to {output_txt_path}")


# Example usage
if __name__ == "__main__":
    input_pdf = "../report.pdf"           # Replace with your PDF file path
    
    # Create output directory if it doesn't exist
    output_dir = "../outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_txt = os.path.join(output_dir, f"output_text_{timestamp}.txt")

    pdf_to_text(input_pdf, output_txt)
