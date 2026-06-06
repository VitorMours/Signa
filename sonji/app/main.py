from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import v1_router
from app.core.config import config
from app.core.logging import setup_logger
import uvicorn

app = FastAPI(title = config.title, description = "An api for the sonji project")

logger = setup_logger(__name__)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  
    allow_methods=["*"],     
    allow_headers=["*"],     
)

app.add_api_route("/health", lambda: {"status": "ok"}, methods=["GET"])
app.include_router(v1_router)

logger.info("API initialized successfully")

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )