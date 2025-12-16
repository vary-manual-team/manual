
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path, output_txt_path):
    try:
        reader = PdfReader(pdf_path)
        with open(output_txt_path, 'w', encoding='utf-8') as f:
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                f.write(f"--- Page {i+1} ---\n")
                f.write(text)
                f.write("\n\n")
        print(f"Successfully extracted text to {output_txt_path}")
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    pdf_path = "content/manual_slides.pdf"
    output_path = "content/manual_text.txt"
    extract_text_from_pdf(pdf_path, output_path)
