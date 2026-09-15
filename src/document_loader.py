from pathlib import Path
from pypdf import PdfReader


def load_pdf(file_path):
    """
    Extract text from a PDF file.

    Returns:
        str: Extracted text from all pages.
    """

    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    reader = PdfReader(pdf_path)

    pages_text = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages_text.append(text)

    return "\n\n".join(pages_text)