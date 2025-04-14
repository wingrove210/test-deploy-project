from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/items")
def get_items():
    items = [
        {
            "id": 1,
            "name": "Hello",
            "role": "admin"
        },
        {
            "id": 2,
            "name": "Hello",
            "role": "admin"
        },
                {
            "id": 3,
            "name": "Hello",
            "role": "admin"
        }
    ]
    return items

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)