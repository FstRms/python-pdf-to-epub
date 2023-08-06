import os
from ebooklib import epub
from PyPDF2 import PdfFileReader


def convert_pdf_to_epub(pdf_path, epub_path, cover_path):
    # Create new EPUB book
    book = epub.EpubBook()

    # Set metadata
    book.set_identifier("pdf-to-epub")
    book.set_title(os.path.splitext(os.path.basename(pdf_path))[0])
    book.set_language("en")

    # Read PDF file
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        num_pages = pdf_reader.getNumPages()

        # Add chapters to EPUB book
        for page_num in range(num_pages):
            ch_title = "Chapter {}".format(page_num + 1)
            ch_content = epub.EpubHtml(title=ch_title, file_name=f"{ch_title}.xhtml")
            ch_content.content = f"<h1>{ch_title}</h1>"
            ch_content.content += pdf_reader.getPage(page_num).extractText()
            book.add_item(ch_content)
            book.toc.append(epub.Link(f"{ch_title}.xhtml", ch_title, ch_title))

        # read cover image
        with open(cover_path, "rb") as cover_content:
            cover_img = cover_content.read()

        # Add cover image
        cover_image = epub.EpubItem(
            uid="cover-image",
            file_name="cover.jpg",
            media_type="image/jpeg",
            content=cover_img,
        )
        book.add_item(cover_image)

        # Set book cover
        book.set_cover("cover.jpg", open("cover.jpg", "rb").read())

        # Add book spine
        book.spine = ["nav"]
        for chapter in book.toc:
            book.spine.append(chapter)

        # Write EPUB file
        epub.write_epub(epub_path, book, {})
