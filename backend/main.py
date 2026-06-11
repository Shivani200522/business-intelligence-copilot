from fastapi import FastAPI

from backend.api.routes import router

app = FastAPI(
    title="Business Intelligence Copilot"
)

app.include_router(router)