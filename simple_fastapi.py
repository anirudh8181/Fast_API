from fastapi import FastAPI
from items_routes import router as items_router

app = FastAPI(title="Sample API", version="1.0.0")

# Include routers
app.include_router(items_router)

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to Sample API", "version": "1.0.0"}