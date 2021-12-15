from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"API": "Fast"}


@app.post("/", status_code=201)
async def post_root(t, h, c):
    return {'t': t, 'h': h, 'c': c}


@app.put("/{object_id}", status_code=200)
async def put_root(object_id: str,
                   t: Optional[int] = None,
                   h: Optional[int] = None,
                   c: Optional[int] = None):
    return {object_id: {'t': t, 'h': h, 'c': c}}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload=True,
                # ssl_keyfile="./key.pem",
                # ssl_certfile="./cert.pem"
                )
