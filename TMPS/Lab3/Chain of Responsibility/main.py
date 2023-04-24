from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, document: str) -> Optional[str]:
        pass


class DocumentHandler(Handler):
    """
    Конкретный обработчик для документов.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, document: str) -> str:
        if self._next_handler:
            return self._next_handler.handle(document)
        return None


class XmlHandler(DocumentHandler):
    def handle(self, document: str) -> str:
        if document.endswith('.xml'):
            return f"XmlHandler: обработал документ {document}"
        else:
            return super().handle(document)


class JsonHandler(DocumentHandler):
    def handle(self, document: str) -> str:
        if document.endswith('.json'):
            return f"JsonHandler: обработал документ {document}"
        else:
            return super().handle(document)


class CsvHandler(DocumentHandler):
    def handle(self, document: str) -> str:
        if document.endswith('.csv'):
            return f"CsvHandler: обработал документ {document}"
        else:
            return super().handle(document)


def client_code(handler: Handler) -> None:

    documents = ["file4.yaml","file1.xml", "file2.csv", "file3.json", ]

    for document in documents:
        print(f"\nClient: кто обработает {document}?")
        result = handler.handle(document)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {document} не может быть обработан.", end="")


if __name__ == "__main__":
    xml_handler = XmlHandler()
    json_handler = JsonHandler()
    csv_handler = CsvHandler()

    xml_handler.set_next(json_handler).set_next(csv_handler)

    print("Цепочка: XmlHandler > JsonHandler > CsvHandler")
    client_code(xml_handler)



