from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from typing import List, Dict, Any
from pydantic import BaseModel
from ....ai.rag.retrieval.service import RetrievalService
from ....ai.rag.indexing.pipeline import IndexingPipeline

router = APIRouter()
retrieval_service = RetrievalService()
indexing_pipeline = IndexingPipeline()

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
    filters: Dict[str, Any] = None

@router.post("/index", summary="Index a document")
async def index_document(source: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(indexing_pipeline.index_document, source)
    return {"message": "Document indexing started in background", "source": source}

@router.post("/search", summary="Semantic Search")
async def search_documents(request: SearchRequest):
    results = await retrieval_service.retrieve(request.query, request.top_k, request.filters)
    return {"results": results}

@router.post("/upload", summary="Upload and process document")
async def upload_document(file: UploadFile = File(...)):
    # Placeholder for actual file upload saving and indexing
    return {"message": f"File {file.filename} uploaded and queued for processing"}

@router.delete("/document/{doc_id}", summary="Delete document from index")
async def delete_document(doc_id: str):
    return {"message": f"Document {doc_id} deleted"}

@router.get("/collections", summary="List vector collections")
async def list_collections():
    return {"collections": ["default-collection"]}

@router.get("/statistics", summary="Get RAG statistics")
async def get_statistics():
    return {
        "indexed_documents": 0,
        "indexed_chunks": 0,
        "embedding_count": 0,
        "average_chunk_size": 1000
    }

@router.get("/models", summary="List supported embedding models")
async def list_models():
    return {"models": ["BAAI/bge-m3", "text-embedding-3-small"]}
