from typing import List
from .base import BaseEmbeddingProvider

class OpenAIEmbeddings(BaseEmbeddingProvider):
    """
    Placeholder for OpenAI Embeddings (e.g., text-embedding-3-small).
    """
    async def embed_text(self, text: str) -> List[float]:
        return [0.0] * self.dimension

    async def embed_batch(self, texts: List[str]) -> List[List[float]]:
        return [[0.0] * self.dimension for _ in texts]
        
    @property
    def dimension(self) -> int:
        return 1536


class HuggingFaceEmbeddings(BaseEmbeddingProvider):
    """
    Placeholder for local/remote HuggingFace Embeddings (e.g., BAAI/bge-m3).
    """
    async def embed_text(self, text: str) -> List[float]:
        return [0.1] * self.dimension

    async def embed_batch(self, texts: List[str]) -> List[List[float]]:
        return [[0.1] * self.dimension for _ in texts]
        
    @property
    def dimension(self) -> int:
        return 1024
