from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI(title="Audacia - Voice Conversion Backend (scaffold)")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/train")
async def train_model(file: UploadFile = File(...)):
    # Placeholder endpoint: accept archive of training samples and enqueue training job
    return JSONResponse(status_code=501, content={"detail": "Training endpoint not implemented in scaffold. Use worker tasks."})


@app.post("/tts/synthesize")
async def synthesize(text: str):
    # Placeholder TTS synth endpoint
    return JSONResponse(status_code=501, content={"detail": "TTS synth not implemented in scaffold."})


@app.post("/replace")
async def replace_audio(file: UploadFile = File(...)):
    # Placeholder for offline replacement
    return JSONResponse(status_code=501, content={"detail": "Replace endpoint not implemented in scaffold."})


@app.websocket('/vc/stream')
async def vc_stream():
    # WebSocket VC endpoint placeholder. Implement chunked audio exchange here.
    return JSONResponse(status_code=501, content={"detail": "WebSocket VC not implemented in scaffold."})
