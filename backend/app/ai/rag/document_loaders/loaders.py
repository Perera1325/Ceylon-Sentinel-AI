from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseDocumentLoader(ABC):
    @abstractmethod
    async def load(self, source: Any) -> List[Dict[str, str]]:
        """Load document and return list of text content with initial metadata."""
        pass

class TextLoader(BaseDocumentLoader):
    async def load(self, source: str) -> List[Dict[str, str]]:
        with open(source, 'r', encoding='utf-8') as f:
            content = f.read()
        return [{"text": content, "metadata": {"source": source, "type": "text"}}]

class PDFLoader(BaseDocumentLoader):
    """Placeholder for PyPDF or unstructured PDF loading."""
    async def load(self, source: str) -> List[Dict[str, str]]:
        return [{"text": "Extracted PDF text", "metadata": {"source": source, "type": "pdf"}}]

class JSONLoader(BaseDocumentLoader):
    """Placeholder for JSON loading."""
    async def load(self, source: str) -> List[Dict[str, str]]:
        return [{"text": "Extracted JSON text", "metadata": {"source": source, "type": "json"}}]
