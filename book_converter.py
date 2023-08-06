import os
from converter import convert_pdf_to_epub
from cover_generator import generate_cover_image

# Create input and output directories if they don't exist
if not os.path.exists("input"):
    os.makedirs("input")
if not os.path.exists("output"):
    os.makedirs("output")

# Get a list of PDF files in the input directory
pdf_files = [f for f in os.listdir("input") if f.endswith(".pdf")]

# Convert each PDF file to EPUB and save it in the output directory
for pdf_file in pdf_files:
    pdf_path = os.path.join("input", pdf_file)
    cover_path = generate_cover_image(pdf_path)
    epub_file = os.path.splitext(pdf_file)[0] + ".epub"
    epub_path = os.path.join("output", epub_file)
    convert_pdf_to_epub(pdf_path, epub_path, cover_path)
