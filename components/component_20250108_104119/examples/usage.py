```python
# Example 1: Basic Usage of Document Indexing
import os
import asyncio
from typing import List
from your_package import Document, DocumentIndex, open_document, index_documents, search_documents

# Initialize the document index
index = DocumentIndex()

# Example document paths
doc_paths = ['doc1.txt', 'doc2.txt']

# Index documents asynchronously
async def main(doc_paths: List[str]) -> None:
    await index_documents(doc_paths, index)

# Execute the indexing
asyncio.run(main(doc_paths))

# Example usage of searching documents
search_term = 'example'
results = index.search(search_term)

# Print out found documents
for document in results:
    print(f"Found document: {document.id}")  # Expected output: Found document: <document_id>


# Example 2: Handling Document Not Found Error
try:
    async with open_document('non_existent_file.txt') as doc:
        print(doc)
except DocumentNotFoundError as e:
    print(e)  # Expected output: Document not found: non_existent_file.txt


# Example 3: Using LRU Cache for Document Loading
from your_package import load_document

# Load a document with caching
doc = load_document('doc1.txt')
print(f"Loaded document: {doc.id}")  # Expected output: Loaded document: doc1.txt

# Subsequent calls will return the cached document
cached_doc = load_document('doc1.txt')
print(cached_doc is doc)  # Expected output: True (indicating it uses the cached version)


# Example 4: Best Practices with Async Context Manager
async def safe_document_handling(file_path: str) -> None:
    try:
        async with open_document(file_path) as doc:
            print(f"Document Content: {doc.content}")  # Expected to print the content of the document
    except DocumentNotFoundError as e:
        print(e)  # Handle the error gracefully

# Test the safe document handling
asyncio.run(safe_document_handling('doc1.txt'))


# Example 5: Performance Tips with Async Document Indexing
async def index_multiple_documents(doc_paths: List[str]) -> None:
    await asyncio.gather(*(index_documents([path], index) for path in doc_paths))

# Perform indexing of multiple documents concurrently
asyncio.run(index_multiple_documents(doc_paths))
```