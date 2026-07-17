from utils.export import (
    export_text_to_pdf,
    export_text_to_docx,
    export_text_to_txt
)

text = "Hello World"

pdf_file = export_text_to_pdf(text)

docx_file = export_text_to_docx(text)

txt_file = export_text_to_txt(text)
