# SunSeat - Touch Grass in 20 minutes

Offline-first sunny-bench finder. Enter location + minutes + needs, get 3 sun pockets + 60-sec Gemma-local mission card. Screen <60s, rest outside.

This is a submission for the Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass.

## Quickstart (local, 5 min)

```bash
cd sunseat
pip install -r requirements.txt
# optional open-weight local run:
# ollama pull gemma2:2b && ollama serve
uvicorn backend.main:app --reload --port 8000
# open http://localhost:8000
```

No keys needed. Sentry / SerpApi / TabPFN are optional and guarded.

## Why open matters

- OSM exposes `surface/smoothness/incline/bench/toilets` - closed maps hide them. Needed for flat/quiet/toilet filtering.
- Gemma 2B via Ollama runs on trail with no signal, $0, private. Closed APIs need internet + per-token $$ + location upload.
- Swap model in one env var: `OLLAMA_MODEL=llama3.2:1b`.
- TabPFN picks best hour from local weather CSV history. No cloud training.

## Deploy to Render (Best Use of Render)

1. Push this folder as its own repo (must be brand-new for judging).
2. Render -> New Web Service -> Docker -> Dockerfile in root.
3. Free plan is fine. Set `OLLAMA_MODEL=gemma2:2b`. Hosted demo uses honest template fallback (no GPU on free), local run uses Gemma - include Ollama screenshot in DEV post.

## API

- `GET /api/health`
- `GET /api/sun?lat,lon`
- `GET /api/weather?lat,lon` (Open-Meteo, offline fallback)
- `POST /api/pockets {lat,lon,minutes,needs[]}` (Overpass + score + TabPFN best-hour)
- `POST /api/brief {pocket,weather,minutes,needs}` (Ollama Gemma, fallback guarded)
- `GET /api/foliage?location=` (SerpApi live if key, else cached)

## Prize paths included

- Gemma: `OLLAMA_MODEL=gemma2:2b` local call in `backend/main.py:gemma_brief`
- TabPFN: `best_hour_tabpfn()` tries TabPFNRegressor, falls back to heuristic with log
- Render: Dockerfile + render.yaml
- SerpApi: `/api/foliage`
- Sentry: `SENTRY_DSN` init
- Copilot: built with Copilot CLI (note in post + keep Actions workflow if you add one)
- Entire/DevRelay: link agent session in post
- ElevenLabs: use `frontend Speak` for draft, generate final narration MP3 for demo video

## Offline proof for judges

1. Load once online, then airplane mode, reload `/` - cached `localStorage sunseat_last` still renders.
2. Screenshot Ollama terminal: `ollama run gemma2:2b` + `/api/brief mode:local-open-weight`.
3. Outside photo: sunny bench + mission card.

## License

MIT - see LICENSE.
