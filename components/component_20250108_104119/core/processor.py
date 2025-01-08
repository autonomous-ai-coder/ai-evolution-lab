```python
import os
import json
import mmap
import asyncio
from typing import List, Dict, Optional, Union
from dataclasses import dataclass, field
from collections import defaultdict
from contextlib import asynccontextmanager
from functools import lru_cache, wraps


class DocumentNotFoundError(Exception):
    """Exception raised when a document is not found in the index."""
    pass


@dataclass
class Document:
    """Represents a text document with its metadata."""
    
    id: str
    content: str
    format: str = field(default='txt')


class DocumentIndex:
    """Handles indexing and searching of documents."""

    __slots__ = ('_index', '_document_store', '_documents')

    def __init__(self):
        self._index: Dict[str, List[str]] = defaultdict(list)
        self._document_store: Dict[str, Document] = {}
        self._documents: List[str] = []

    def add_document(self, document: Document) -> None:
        """Adds a document to the index.

        Args:
            document: The document to add.
        """
        self._document_store[document.id] = document
        self._documents.append(document.id)
        self._index_document(document)

    def _index_document(self, document: Document) -> None:
        """Indexes the content of a document.

        Args:
            document: The document to index.
        """
        for word in document.content.split():
            self._index[word].append(document.id)

    def search(self, query: str) -> List[Document]:
        """Searches for documents matching the query.

        Args:
            query: The search term.

        Returns:
            A list of matching documents.
        """
        matching_ids = set(self._index.get(query, []))
        return [self._document_store[doc_id] for doc_id in matching_ids]


@asynccontextmanager
async def open_document(file_path: str) -> Optional[Document]:
    """Asynchronously opens a document and yields its content.

    Args:
        file_path: Path to the document.

    Yields:
        Document object with the content.
    """
    if not os.path.exists(file_path):
        raise DocumentNotFoundError(f"Document not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        yield Document(id=os.path.basename(file_path), content=content)


@lru_cache(maxsize=128)
def load_document(file_path: str) -> Document:
    """Loads a document from the file system.

    Args:
        file_path: Path to the document.

    Returns:
        Document object.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return Document(id=os.path.basename(file_path), content=f.read())


async def index_documents(doc_paths: List[str], index: DocumentIndex) -> None:
    """Indexes a list of documents asynchronously.

    Args:
        doc_paths: List of paths to documents.
        index: The DocumentIndex instance.
    """
    for path in doc_paths:
        async with open_document(path) as doc:
            if doc:
                index.add_document(doc)


async def search_documents(index: DocumentIndex, query: str) -> List[Document]:
    """Searches for documents containing the query.

    Args:
        index: The DocumentIndex instance.
        query: The search term.

    Returns:
        A list of matching documents.
    """
    return index.search(query)


def main(doc_paths: List[str], query: str) -> None:
    """Main entry point for indexing and searching documents.

    Args:
        doc_paths: List of paths to documents.
        query: The search term.
    """
    index = DocumentIndex()
    asyncio.run(index_documents(doc_paths, index))
    results = asyncio.run(search_documents(index, query))

    for document in results:
        print(f"Found document: {document.id}")


# Example usage (commented for clarity)
# doc_paths = ['doc1.txt', 'doc2.txt']
# search_term = 'example'
# main(doc_paths, search_term)
```