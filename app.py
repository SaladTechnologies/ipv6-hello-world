from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/hc")
async def health_check():
    return "OK"


if __name__ == "__main__":
    uvicorn.run(app, host="::", port=1234)
