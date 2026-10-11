import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MODEL = os.getenv("OLLAMA_MODEL", "gemma3:270m")
PROOF = os.getenv("PROOF_FILE", "docs/ollama-proof.json")

import backend.main as m
from fastapi.testclient import TestClient

m.OLLAMA_MODEL = MODEL
c = TestClient(m.app)
j = c.post(
    "/api/brief",
    json={
        "pocket": {"name": "Sunny edge 1", "lat": 13.08, "lon": 80.27},
        "weather": {"current": {"temperature_2m": 30, "cloud_cover": 20}},
        "minutes": 20,
        "needs": ["quiet"],
    },
).json()
with open(PROOF, "w") as f:
    json.dump(j, f, indent=2)
print(j.get("mode"), j.get("model"))
print((j.get("text") or "")[:500].encode("ascii", "ignore").decode())
