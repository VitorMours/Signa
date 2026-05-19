from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import v1_router
from app.core.config import config
api = FastAPI(title = config.title, description = "An api for the sonji project")


origins = ["*"]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  
    allow_methods=["*"],     
    allow_headers=["*"],     
)

api.add_api_route("/health", lambda: {"status": "ok"}, methods=["GET"])
api.include_router(v1_router)