"""
FastAPI application
"""
from fastapi import FastAPI
from .router import router
from .s3 import connect, create_bucket


app = FastAPI(
    title="Datasets Backend",
    description="Backend server for datasets application",
    version="0.1.0",
)


@app.on_event("startup")
def connect_on_startup():
    """
    Connect to S3 server on startup
    """
    connect()
    create_bucket()


app.include_router(router)
