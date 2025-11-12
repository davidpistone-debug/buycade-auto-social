#!/usr/bin/env python3
import json, os, time, hashlib, random, datetime
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA = os.path.join(ROOT, "data", "items.json")
CFG  = os.path.join(ROOT, "data", "config.json")
OUTJ = os.path.join(ROOT, "docs", "featured.json")

def pick_item(items, seed=None):
    # Deterministic daily rotation based on date in configured timezone
    tz = "America/Chicago"
    if os.path.exists(CFG):
        with open(CFG) as f:
            tz = json.load(f).get("timezone", tz)
    now = datetime.datetime.now(ZoneInfo(tz))
    day_key = now.strftime("%Y-%m-%d")
    h = hashlib.sha256(day_key.encode()).hexdigest()
    rnd = int(h[:8], 16)
    idx = rnd % len(items)
    return items[idx]

def main():
    with open(DATA) as f:
        items = json.load(f)
    item = pick_item(items)
    # write featured.json
    featured = {
        "title": item["title"],
        "url": item["url"],
        "image": item["image"],
        "description": item["description"],
        "tags": item.get("tags", []),
        "timestamp": int(time.time())
    }
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    with open(OUTJ, "w") as f:
        json.dump(featured, f, indent=2)
    print("Wrote docs/featured.json")

if __name__ == "__main__":
    main()
