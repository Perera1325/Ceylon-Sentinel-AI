from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class BaseVectorStore(ABC):
    """
    Abstract interface for all Vector Database Providers (Qdrant, Pinecone, etc.).
    """
    
    @abstractmethod
    async def connect(self) -> None:
        """Establish connection to the vector database."""
        pass
        
    @abstractmethod
    async def create_collection(self, name: str, dimension: int) -> None:
        """Create a new collection/index if it does not exist."""
        pass
        
    @abstractmethod
    async def upsert(self, collection: str, ids: List[str], vectors: List[List[float]], payloads: List[Dict[str, Any]]) -> None:
        """Insert or update vectors and their metadata."""
        pass
        
    @abstractmethod
    async def search(self, collection: str, query_vector: List[float], top_k: int = 5, filter_conditions: Optional[Dict] = None) -> List[Dict[str, Any]]:
        """Search for similar vectors."""
        pass
        
    @abstractmethod
    async def delete(self, collection: str, ids: List[str]) -> None:
        """Delete specific vectors by ID."""
        pass
