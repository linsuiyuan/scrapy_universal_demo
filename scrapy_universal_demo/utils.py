import json
from pathlib import Path


def get_config(name: str):
    filepath = Path(__file__).resolve().parent / f"configs/{name}.json"
    with filepath.open("r", encoding="utf-8") as fr:
        return json.load(fr)
