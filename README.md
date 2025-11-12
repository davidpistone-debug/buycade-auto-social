# Buycade Auto‑Social (Free, No Paid Apps)

This repo powers your **Auto‑Social Exposure System**: it rotates a featured product or collection, generates
an **RSS feed** and a **JSON feed**, and (optionally) **auto‑posts** to social channels using *free* tools:
- **IFTTT Webhooks** (free) → posts to Facebook Page, Twitter/X, Pinterest, Tumblr, etc.
- **Mastodon** (optional) via API (free and open).

> Host this repo on GitHub. Enable **GitHub Pages** with the `/docs` folder.  
> A scheduled GitHub Action runs daily to pick an item, build feeds, and (optionally) post.

---

## 🧩 How it Works
1) You maintain a simple list in **`data/items.json`** (products, collections, quests).  
2) **`scripts/rotate.py`** picks the next featured item.  
3) **`scripts/build_feed.py`** renders:
   - `docs/featured.json` (machine‑readable)
   - `docs/feed.xml` (RSS — perfect for IFTTT)  
4) **GitHub Actions** (`.github/workflows/auto-social.yml`) runs on a schedule:
   - Commits the new feed files
   - *Optional:* Notifies IFTTT via Webhook
   - *Optional:* Posts to Mastodon

---

## ✅ Quick Start (10–15 min)

### 0) Create the repository
1. Download this ZIP and unzip it.
2. Create a new **private** repo on GitHub (e.g., `buycade-auto-social`).
3. Upload all files.  
4. In the repo, go to **Settings → Pages** and set **Source = Deploy from a branch**, Branch = `main`, Folder = `/docs`. Save.

Your feeds will be live at:
- `https://<your-username>.github.io/buycade-auto-social/featured.json`
- `https://<your-username>.github.io/buycade-auto-social/feed.xml`

### 1) Edit your items
Open `data/items.json` and add your products/collections (title, url, image, description, tags).

### 2) (Optional) Connect IFTTT (free)
- Go to IFTTT → Create **Webhooks** → **Receive a web request** (event name: `buycade_ping`).
- In the action step, choose where to post (e.g., Facebook Page post or Pinterest pin) and compose the post using the JSON values:
  - `{Value1}` → title
  - `{Value2}` → url
  - `{Value3}` → caption
  - `{Value4}` → image
- Copy your IFTTT Webhooks key from the **Webhooks** service page (Documentation).
- In GitHub repo → **Settings → Secrets and variables → Actions → New repository secret**:  
  - `IFTTT_KEY` = your key (the long hex string)
- The workflow will call: `https://maker.ifttt.com/trigger/buycade_ping/with/key/$IFTTT_KEY` with JSON values.

### 3) (Optional) Mastodon auto‑post
- Create a Mastodon account (or use your existing instance).
- Create an application in Mastodon → get **Access Token**.
- In GitHub repo Secrets, add:
  - `MASTODON_BASE_URL` (e.g., `https://mastodon.social`)
  - `MASTODON_TOKEN` (your token)
- The workflow will run `scripts/mastodon_post.py` to publish the caption + URL.

### 4) Turn on the schedule
- The GitHub Action is already set to run **daily at 14:00 America/Chicago** (edit cron as you wish).
- You can also run it manually via the **Actions** tab (workflow `Run Auto‑Social`).

---

## 📝 Caption Styles
Edit `templates/captions.txt` — one caption per line with placeholders:
- `{title}` — item title
- `{url}` — canonical link
- `{tags}` — hashtags (auto‑built from item tags)
- `{cta}` — call‑to‑action (from `data/config.json`)

Example line:
```
🕹️ {title} — new drop just landed. {cta} {url} {tags}
```

---

## 🔧 Files You’ll Tweak Most
- `data/items.json` — your rotating list
- `templates/captions.txt` — voice and style
- `data/config.json` — timezone, schedule hints, default CTA, brand hashtags

---

## 🆘 Troubleshooting
- If Pages doesn’t load your feed, re‑save the Pages setting and wait 2–3 minutes.
- If IFTTT doesn’t post, check the **Run Logs** in GitHub Actions and IFTTT Activity Log.
- If an image 404s on social, ensure the `image` URL is public (Shopify CDN or your own).

---

## ✨ Extending
- Add Discord/Telegram bots for alerts.
- Add Bluesky, Reddit, or Threads via their APIs (or via IFTTT where available).
- Add UTM parameters to URLs for tracking (Plausible-friendly).

Enjoy owning your exposure. 🎮
