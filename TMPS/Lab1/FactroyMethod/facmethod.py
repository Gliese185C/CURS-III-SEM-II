from abc import ABC, abstractmethod
import pdfkit
from docx import Document


class DocumentFormat(ABC):
    @abstractmethod
    def create_document(self, content):
        pass


class PDF(DocumentFormat):
    def create_document(self, content):
        pdfkit.from_string(content, 'output.pdf')


class DOCX(DocumentFormat):
    def create_document(self, content):
        document = Document()
        document.add_paragraph(content)
        document.save('output.docx')


class HTML(DocumentFormat):
    def create_document(self, content):
        with open('output.html', 'w') as f:
            f.write(content)


class DocumentFactory:
    @staticmethod
    def create_document_format(format_type: str) -> DocumentFormat:
        if format_type == 'pdf':
            return PDF()
        elif format_type == 'docx':
            return DOCX()
        elif format_type == 'html':
            return HTML()
        else:
            raise ValueError(f"Unsupported document format type: {format_type}")


if __name__ == "__main__":
    format_type = 'pdf'
    content = 'Hello world!'

    document_format = DocumentFactory.create_document_format(format_type)
    document_format.create_document(content)
