import os
from PyPDF2 import PdfMerger

# Output folder
OUTPUT_FOLDER = "outputs"

# Create the output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def merge_pdfs(uploaded_files, output_filename="merged_document.pdf"):
    """
    Merge multiple PDF files into a single PDF.

    Parameters:
        uploaded_files (list): List of uploaded PDF files.
        output_filename (str): Name of the merged output PDF.

    Returns:
        str: Path to the merged PDF.
    """

    if not uploaded_files:
        raise ValueError("No PDF files were uploaded.")

    merger = PdfMerger()

    try:
        # Add each uploaded PDF
        for pdf in uploaded_files:
            pdf.seek(0)  # Reset file pointer
            merger.append(pdf)

        # Output path
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        # Save merged PDF
        with open(output_path, "wb") as output_file:
            merger.write(output_file)

        merger.close()

        return output_path

    except Exception as e:
        merger.close()
        raise Exception(f"Failed to merge PDFs: {e}")
