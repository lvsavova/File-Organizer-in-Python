from docx import *


class DocumentHandler:

    def appears_in_paragraph(self, paragraph, match_string):
        return match_string in paragraph.text

    def search_content(self, document_path, match_string):
        document = Document(document_path)
        contains_word = False
        for paragraph in document.paragraphs:
            if self.appears_in_paragraph(paragraph, match_string):
                contains_word = True
                break
        return contains_word

    def create_report(self, report_folder, log):
        document = Document()
        document.add_heading('File Organizer Report', 0)
        table = document.add_table(rows=1, cols=3)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'File'
        hdr_cells[1].text = 'Copy Destination'
        for key in log:
            row_cells = table.add_row().cells
            row_cells[0].text = key
            row_cells[1].text = log[key]
        document.save(report_folder + "\\" + "report.docx")
        return document
