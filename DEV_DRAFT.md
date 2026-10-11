*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass](https://dev.to/challenges/hacktoberfest-week1-2026-10-05)*

## What I Built
SunSeat - 20-min sunny-bench finder for SAD, night-shift, and overstimulated brains. Enter lat/lon + minutes + needs (flat/quiet/toilet), get 3 sun pockets + 60-sec mission card. Screen <60s, rest outside.

## Demo
Live: https://sunseat.onrender.com (replace after deploy)
Video: 90s - screen search -> outside sunny bench -> mission card read aloud
Offline proof: airplane-mode reload still renders from localStorage cache.

## Code
Repo: push `sunseat/` folder as its own public repo with MIT LICENSE. Embed: `{% github yourname/sunseat %}`

Key files:
- `sunseat/backend/main.py` - FastAPI, solar calc, OSM + Open-Meteo, TabPFN best-hour, Gemma via Ollama
- `sunseat/frontend/index.html` - single-file PWA, offline cache
- `sunseat/Dockerfile` + `render.yaml` - Render deploy

## How I Built It
Open core: Gemma `gemma2:2b` via Ollama local inference does the mission card. OSM Overpass gives parks/benches/toilets + `surface/smoothness` tags. Open-Meteo gives cloud/radiation. Pure-python solar elevation scores 0-100 go-now. TabPFNRegressor predicts best hour from 72h history, falls back to heuristic with log if not installed. SerpApi live foliage when key set, else cached. Sentry tracing when DSN set. Hosted Render free uses honest template fallback (no GPU), local uses Gemma - include Ollama screenshot showing `mode:local-open-weight`.

## Why Does Open Innovation Matter?
Closed maps hide surface/smoothness/bench/toilet tags I need for flat/quiet filtering. Closed AI needs signal + per-token cost + location upload - dies on trail. SunSeat runs airplane-mode after first fetch, $0, private, swaps `OLLAMA_MODEL=llama3.2:1b` in one var. I fine-tune prompt locally, no approval.

## My Agent Session
Link DevRelay session here. Built with Copilot CLI + this agent. Include 2 screenshots: Ollama local brief + Sentry trace.

## Prize Categories
- Best Use of Gemma
- Best Use of Render
- Best Use of TabPFN
- Best Use of SerpApi
- Best Use of Sentry Agent Tracing
- Best Use of GitHub Copilot
- Best Use of Entire
- Best Use of ElevenLabs (narration MP3 for demo)

## Outside test
Went to [park name] at [time], sun_score 87, sat 15 min. Photo: bench + mission card on phone. Felt [1 line honest].
