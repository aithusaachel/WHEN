from fastapi import FastAPI
from app.api.routes import health

app = FastAPI(
    title = "WHEN API",
    description= "Backend for the WHEN mobile application",
    version= "1.0.0"
)

app.include_router(health.router) 
