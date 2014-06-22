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
