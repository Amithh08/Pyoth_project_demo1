import os
from PyPDF2 import PdfReader, PdfWriter

# Output folder
OUTPUT_FOLDER = "outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def extract_pages(uploaded_file, pages, output_filename="extracted_pages.pdf"):
    """
    Extract specific pages from a PDF.

    Parameters:
        uploaded_file : Uploaded PDF file
        pages : String like '1,3,5' or '2-6'
        output_filename : Name of output PDF

    Returns:
        str : Output PDF path
    """

    reader = PdfReader(uploaded_file)
    writer = PdfWriter()

    total_pages = len(reader.pages)

    page_numbers = []

    pages = pages.replace(" ", "")

    # Range format (Example: 2-5)
    if "-" in pages:

        start, end = pages.split("-")

        start = int(start)
        end = int(end)

        if start < 1 or end > total_pages or start > end:
            raise ValueError("Invalid page range.")

        page_numbers = list(range(start, end + 1))

    # List format (Example: 1,3,5)
    else:

        page_numbers = [int(x) for x in pages.split(",")]

        for page in page_numbers:
            if page < 1 or page > total_pages:
                raise ValueError(f"Page {page} does not exist.")

    # Add selected pages
    for page in page_numbers:
        writer.add_page(reader.pages[page - 1])

    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)

    return output_path
