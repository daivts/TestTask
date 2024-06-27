from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from transformers import pipeline

from utils import calculate_lengths

app = FastAPI()

summarizer = pipeline("summarization", model="Falconsai/text_summarization")


@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "")
    summarization_len = data.get("summarization_len", 0)
    if not text:
        return {"error": "No text provided"}

    min_length, max_length = calculate_lengths(text, int(summarization_len))
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary


@app.get("/", response_class=HTMLResponse)
async def read_index():
    html_path = Path("index.html")
    return HTMLResponse(content=html_path.read_text(), status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
