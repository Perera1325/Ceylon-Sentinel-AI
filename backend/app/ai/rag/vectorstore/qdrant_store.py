import os
from typing import List, Dict, Any, Optional
from qdrant_client import AsyncQdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from .base import BaseVectorStore

class QdrantStore(BaseVectorStore):
    """
    Qdrant implementation of the Vector Store interface.
    """
    def __init__(self):
        # In a real setup this would pull from config
        self.host = os.getenv("QDRANT_HOST", "localhost")
        self.port = int(os.getenv("QDRANT_PORT", "6333"))
        self.client = None

    async def connect(self) -> None:
        if not self.client:
            self.client = AsyncQdrantClient(host=self.host, port=self.port)

    async def create_collection(self, name: str, dimension: int) -> None:
        await self.connect()
        collections = await self.client.get_collections()
        if not any(c.name == name for c in collections.collections):
            await self.client.create_collection(
                collection_name=name,
                vectors_config=VectorParams(size=dimension, distance=Distance.COSINE),
            )

    async def upsert(self, collection: str, ids: List[str], vectors: List[List[float]], payloads: List[Dict[str, Any]]) -> None:
        await self.connect()
        points = [
            PointStruct(id=i, vector=v, payload=p)
            for i, v, p in zip(ids, vectors, payloads)
        ]
        await self.client.upsert(collection_name=collection, points=points)

    async def search(self, collection: str, query_vector: List[float], top_k: int = 5, filter_conditions: Optional[Dict] = None) -> List[Dict[str, Any]]:
        await self.connect()
        # filter_conditions mapping to Qdrant Filter would go here
        search_result = await self.client.search(
            collection_name=collection,
            query_vector=query_vector,
            limit=top_k
        )
        return [{"id": hit.id, "score": hit.score, "payload": hit.payload} for hit in search_result]

    async def delete(self, collection: str, ids: List[str]) -> None:
        await self.connect()
        await self.client.delete(collection_name=collection, points_selector=ids)
