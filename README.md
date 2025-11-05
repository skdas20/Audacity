# Audacia (scaffold)

This repository contains a scaffold for a voice conversion / TTS system inspired by the blueprint you provided. It includes a minimal backend (FastAPI), a tiny Next.js frontend scaffold, and a docker-compose file to run services locally.

IMPORTANT: I will not assist with scraping or cloning public figures' voices without explicit consent. Non-consensual voice cloning and mass scraping of copyrighted audio is unethical and may be illegal. See the "Safe, legal data" section below for alternatives.

What was added
- `docker-compose.yml` — services: backend, frontend, redis, minio, worker
- `backend/` — minimal FastAPI scaffold, `Dockerfile`, `requirements.txt`
- `frontend/` — minimal Next.js scaffold, `Dockerfile`, `package.json`

Quick start (development)

1. Build and start services:

```bash
docker compose up --build
```

2. Backend will be available at http://localhost:8000 (health: `/health`).
3. Frontend dev server at http://localhost:3000.

Safe, legal data sources (use these instead of scraping celebrities):
- VCTK (multi-speaker English dataset) — good for VC experiments.
- LibriTTS / LibriSpeech — audiobook-derived speech (respect license).
- Common Voice (Mozilla) — public voice contributions with licenses.

If you want to experiment with voice cloning, use only:
- your own recordings, or
- recordings for which you have explicit written consent/licence, or
- public-domain / appropriately licensed datasets.

Next steps I can do for you
- Add a training script that consumes a local dataset and runs a small demo training loop (on consenting data).
- Wire a Celery worker + example job for offline conversion.
- Add GPU-ready Docker config (with NVIDIA container toolkit) and model-loading stubs for RVC / HiFi-GAN.

If you want to proceed with lawful experiments, tell me which of the above next steps to implement and which dataset you will use (or upload a small sample of consenting audio) and I will continue.
# Audacity
The Unmatched realtime voice cloning application
