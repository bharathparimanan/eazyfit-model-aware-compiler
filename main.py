from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000"
]

methods=[
    "GET",
    "POST",
    "PUT",
    "DELETE"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=["*"]
)

@app.get("/", tags=["default"])
def get_root():
    try:
        return {
            "data": [0],
            "message": "eazy-fit ~ your context aware compiler",
            "status": "Ok"
        }
    except RuntimeError:
        raise HTTPException(status_code=404, detail="Runtime error")
    finally:
        pass