from markdowngenerator import MarkdownGenerator

def main():
    with MarkdownGenerator(
        # By setting enable_write as False, content of the file is written
        # into buffer at first, instead of writing directly into the file
        # This enables for example the generation of table of contents
        filename="example.md", enable_write=False
    ) as doc:
        doc.addHeader(1, "Hello there!")
        doc.writeTextLine(f'{doc.addBoldedText("This is just a test.")}')
        doc.addHeader(2, "Second level header.")
        table = [
            {"Column1": "col1row1 data", "Column2": "col2row1 data"},
            {"Column1": "col1row2 data", "Column2": "col2row2 data"},
        ]

        doc.addTable(dictionary_list=table)
        doc.writeTextLine("Ending the document....")

if __name__ == "__main__":
    main()