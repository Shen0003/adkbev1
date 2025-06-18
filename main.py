from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="Simple FastAPI App", version="1.0.0")

# Add this block:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or use ["http://localhost:3000"] to restrict to your frontend
    allow_credentials=True,
    allow_methods=["*"],  # allows POST, GET, etc.
    allow_headers=["*"],  # allows Authorization, Content-Type, etc.
)

@app.get("/")
async def root():
    return {"message": "Hello World! FastAPI is running on Vercel"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is working properly"}

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com"
    }

@app.post("/api/users")
async def create_user(user_data: dict):
    return {
        "message": "User created successfully",
        "user_data": user_data,
        "status": "created"
    }

@app.get("/api/items")
async def get_items(skip: int = 0, limit: int = 10):
    items = [
        {"id": i, "name": f"Item {i}", "description": f"Description for item {i}"}
        for i in range(skip, skip + limit)
    ]
    return {"items": items, "total": len(items)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
