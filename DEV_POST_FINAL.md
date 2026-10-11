*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass](https://dev.to/challenges/hacktoberfest-week1-2026-10-05)*

## What I Built
SunSeat: a 20-minute sunny-bench finder for night-shift workers, SAD winters, and overstimulated brains. Enter location + minutes + needs (flat / quiet / toilet / shade / dog), get 3 sun pockets with a 0-100 go-now score + a 60-second mission card. Screen time under a minute, the rest is outside.

I built it for myself in Chennai: short October evenings, no time for a hike, need sun fast without scrolling.

## Demo
Live: https://sun-seat.onrender.com (verified `/api/health ok`, frontend serves)
Video (90s): screen search -> walk -> sunny bench -> mission card read aloud (narration in `demo-narration.txt`, MP3 via ElevenLabs).
Offline proof: load once online, airplane mode on, reload `/` - results render from `localStorage sunseat_last`. Screenshot in repo `docs/` after you test.
Cover: `frontend/cover.svg` (1000x420).

Local fallback if needed: `pip install -r requirements.txt && uvicorn backend.main:app --port 8000`.

## Code
Repo: https://github.com/Senthil455/Sun-Seat (MIT)

- `backend/main.py` - FastAPI, solar math, OSM Overpass, Open-Meteo, `best_hour_tabpfn()`, `gemma_brief()` via Ollama
- `frontend/index.html` - single-file PWA, offline cache, free TTS Speak button
- `scripts/tabpfn_demo.py` + `data/weather_history.csv` - TabPFN evidence, CI check
- `tests/test_api.py` - 3 tests, all passing
- `Dockerfile` + `render.yaml` + `.github/workflows/ci.yml`

## How I Built It
Open core, not decoration:

1. Gemma via Ollama writes the mission card. Prompt + output logged in `/api/brief`. Local run returns `mode:local-open-weight` - proof in `docs/ollama-proof-gemma2-2b.json` (full `gemma2:2b`, tested on laptop; `docs/ollama-proof.json` shows the lighter `gemma3:270m` swap). Render free has no GPU/Ollama so it returns an honest `hosted-template-fallback` - cite the proof files as evidence.
2. OSM Overpass supplies parks / benches / toilets + `surface/smoothness/incline` tags. Open-Meteo supplies cloud + radiation. Pure-python solar elevation + transparent `sun_score()` 0-100.
3. TabPFN: `scripts/tabpfn_demo.py` trains `TabPFNRegressor` on `data/weather_history.csv` when installed, else sklearn fallback with stderr log. Backend `best_hour_tabpfn()` does the same live. Run `python scripts/tabpfn_demo.py --json` and paste output.
4. SerpApi `/api/foliage`: live search when `SERPAPI_KEY` set, else `cached-offline`. Sentry inits when `SENTRY_DSN` set - paste trace + `latency_ms` from `/api/pockets`.

Swap models in one var: `OLLAMA_MODEL=llama3.2:1b`.

## Why Does Open Innovation Matter?
Closed maps hide the tags I filter on - surface, smoothness, bench, toilets. I cannot build flat/quiet/toilet search on Google Maps API. OSM exposes them freely.

Closed AI dies on the trail: needs signal, per-token cost, uploads your location + photo. SunSeat caches OSM + weather JSON after first fetch, then Gemma 2B runs on the laptop with no internet, $0, private. I edited the prompt locally, swapped models, no approval, no bill. That offline airplane-mode run is the whole point - and only possible open.

## My Agent Session
Built with GitHub Copilot CLI + this coding agent. Session: [paste DevRelay/Entire link here]. CI run: `.github/workflows/ci.yml` (health + tabpfn check). Screenshots to attach: Ollama `mode:local-open-weight` brief, Sentry trace, airplane-mode reload.

## Prize Categories
- Best Use of Gemma (local `gemma2:2b` mission card)
- Best Use of Render (Dockerfile + live URL)
- Best Use of TabPFN (CSV forecast, `scripts/tabpfn_demo.py`)
- Best Use of SerpApi (live foliage grounding / cached fallback)
- Best Use of Sentry Agent Tracing (latency_ms + traces)
- Best Use of GitHub Copilot (Copilot CLI + Actions CI)
- Best Use of Entire (agent session link)
- Best Use of ElevenLabs (`demo-narration.txt` -> MP3 narration)

## Outside test
[Fill after you go: park name, time, sun_score, 15-min sit, 1 honest line + bench photo. Judges give bonus points for this.]

---
AI disclosure: drafted with AI assistance (agent + Copilot), tested and deployed by me. Tags: devchallenge, hf26challenge.
