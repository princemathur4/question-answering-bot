import ocrmypdf
import fitz  # PyMuPDF
from io import BytesIO

def process_pdf_text(file_bytes):
    input_pdf = BytesIO(file_bytes)
    output_pdf = BytesIO()

    try:
        ocrmypdf.ocr(input_pdf, output_pdf, deskew=True, output_type='pdf', skip_text=True)
    except Exception as e:
        raise RuntimeError(f"OCR processing failed: {str(e)}")

    extracted_text = ""
    output_pdf.seek(0)  # Reset the pointer to the beginning of the output PDF
    with fitz.open("pdf", output_pdf) as doc:
        extracted_text = "\n\n".join(page.get_text() for page in doc)

    return extracted_text
