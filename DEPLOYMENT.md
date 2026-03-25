# 🚀 EduBot Deployment Guide

## Option 1 — GitHub Pages (Free, Simplest)

> ⚠️ With GitHub Pages the API key is visible in the HTML source. Only use this for demos/development.

1. Push your code to GitHub
2. Go to **Settings → Pages**
3. Under **Source**, select `Deploy from a branch` → `main` → `/ (root)`
4. Click **Save**
5. Your site will be live at `https://YOUR_USERNAME.github.io/REPO_NAME`

---

## Option 2 — Netlify (Recommended for Production)

Netlify lets you set environment variables server-side via Functions, keeping your key hidden.

### Steps:
1. Push this repo to GitHub
2. Go to [netlify.com](https://netlify.com) → **Add new site** → **Import from Git**
3. Select your GitHub repo
4. Build settings:
   - **Build command:** *(leave empty)*
   - **Publish directory:** `.`
5. Click **Deploy site**
6. After deploy, go to **Site settings → Environment variables**
7. Add: `ANTHROPIC_API_KEY` = `sk-ant-api03-...`

> To use the key server-side (hidden), you'll need a Netlify Function (advanced). For now the static approach works fine for demos.

---

## Option 3 — Vercel (Fast & Free)

1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the project directory
3. Follow the prompts
4. Set your API key: `vercel env add ANTHROPIC_API_KEY`

---

## Option 4 — Python Proxy Server (Most Secure)

Run `server.py` on any cloud VM (Railway, Render, Fly.io, DigitalOcean).

### Setup:
```bash
# 1. Clone the repo on your server
git clone https://github.com/YOUR_USERNAME/edubot-student-assistant.git
cd edubot-student-assistant

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variable
cp .env.example .env
nano .env   # add your ANTHROPIC_API_KEY

# 5. Run the server
python server.py
# or in production:
gunicorn server:app --bind 0.0.0.0:5000
```

### Update index.html to use the proxy:
Find the `fetch` call in `getBotReply()` and change:
```js
// FROM:
const response = await fetch("https://api.anthropic.com/v1/messages", {
  headers: { "Content-Type": "application/json" },

// TO:
const response = await fetch("/api/chat", {
  headers: { "Content-Type": "application/json" },
```
Remove the `x-api-key` header line — the server adds it automatically.

---

## 🔐 Security Checklist

- [ ] Never commit `.env` to Git (it's in `.gitignore`)
- [ ] Change admin credentials before going live
- [ ] Use the proxy server approach for production
- [ ] Enable HTTPS on your hosting platform
- [ ] Rotate your API key regularly
- [ ] Set API usage limits in the Anthropic console

---

## 🛠 Local Development

```bash
# Simple — no server needed
open index.html

# With Python HTTP server
python3 -m http.server 8000
# Visit: http://localhost:8000

# With proxy server (API key hidden)
cp .env.example .env
# Edit .env with your key
python server.py
# Visit: http://localhost:5000
```
