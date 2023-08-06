import os
import PyPDF2
from PIL import Image


def generate_cover_image(pdf_path):
    # Open the PDF file
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the first page of the PDF file
    page = pdf_reader.getPage(0)

    # Convert the page to a PIL Image object
    page_image = page.to_image(resolution=72)

    # Create the cover folder if it doesn't exist
    if not os.path.exists("cover"):
        os.makedirs("cover")

    # Save the image as a JPEG file in the cover folder
    image_file = os.path.join(
        "cover", os.path.splitext(os.path.basename(pdf_path))[0] + ".jpg"
    )
    page_image.save(image_file, "JPEG")

    return image_file
