import os
from PIL import Image

# Create output folder
OUTPUT_FOLDER = "outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def convert_images_to_pdf(uploaded_images, output_filename="images_to_pdf.pdf"):
    """
    Convert one or more uploaded images into a single PDF.

    Parameters:
        uploaded_images (list): List of uploaded image files.
        output_filename (str): Name of the output PDF.

    Returns:
        str: Path to the generated PDF.
    """

    if not uploaded_images:
        raise ValueError("No images were uploaded.")

    image_list = []

    for image_file in uploaded_images:
        image = Image.open(image_file)

        # Convert RGBA or P mode to RGB
        if image.mode != "RGB":
            image = image.convert("RGB")

        image_list.append(image)

    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    # Save images as one PDF
    first_image = image_list[0]

    if len(image_list) == 1:
        first_image.save(output_path)
    else:
        first_image.save(
            output_path,
            save_all=True,
            append_images=image_list[1:]
        )

    return output_path
