from abc import ABC, abstractmethod
from typing import List

class BaseEmbeddingProvider(ABC):
    """
    Abstract interface for all Embedding Providers.
    """
    
    @abstractmethod
    async def embed_text(self, text: str) -> List[float]:
        """Embed a single string of text."""
        pass

    @abstractmethod
    async def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a batch of texts."""
        pass
        
    @property
    @abstractmethod
    def dimension(self) -> int:
        """Return the dimension of the embeddings produced by this provider."""
        pass
