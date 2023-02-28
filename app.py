from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="My First API",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "Users Routes",
    }]
)

app.include_router(user)
