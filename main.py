from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import asyncio
import httpx
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379, decode_responses=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"message": "Hello World!"}


@app.get("/overview")
async def get_overview():
    with open("./mocks/overview.json") as json_file:
        data = json.load(json_file)

    return JSONResponse(content=data)


async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as http_err:
            print(f"HTTP error occurred: {http_err} - for URL: {url}")
            return {"error": f"HTTP error occurred: {http_err} - for URL: {url}"}
        except httpx.RequestError as req_err:
            print(f"Request error occurred: {req_err} - for URL: {url}")
            return {"error": f"Request error occurred: {req_err} - for URL: {url}"}
        except Exception as err:
            print(f"An unexpected error occurred: {err} - for URL: {url}")
            return {"error": f"An unexpected error occurred: {err} - for URL: {url}"}


@app.get("/data")
async def fetch_posts():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/invalid-url",
    ]

    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)

    return {"results": results}


@app.get("/redis")
async def read_root():
    r.set("message", "Hello from Redis!")
    message = r.get("message")
    return {"message": message}


@app.get("/health")
def health_check():
    # TODO: Implement request calls to confirm services status (DB, External APIs)
    return {"status": "ok", "external_api": "ok", "database": "ok"}
