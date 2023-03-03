from app import item_resource
from fastapi import FastAPI, APIRouter
# from api_utils.token_auth import PROTECTED

api_router = APIRouter()

def create_app():
    app = FastAPI(
        title="API Items",
        description="Textual Search - Elasticsearch",
        version="0.0.1",
        openapi_url="/openapi.json",
        docs_url="/",
        redoc_url="/redoc"
    )

    app.include_router(
        item_resource.router,
        tags=["Items"]
        # dependencies=PROTECTED
    )

    return app

