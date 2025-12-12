from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import connect_to_mongo, close_mongo_connection
from app.core.config import settings
from app.routers import org, auth  # <--- IMPORTANT: Verify "auth" is imported here

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)

# Register the routers
app.include_router(org.router)
app.include_router(auth.router)  # <--- IMPORTANT: This line must exist!

@app.get("/health")
def health_check():
    return {"status": "ok", "db": "connected"}