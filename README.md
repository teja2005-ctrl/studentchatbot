 🎓 EduBot — AI Student Assistant

An AI-powered chatbot for college students built with vanilla HTML/CSS/JS and the Claude API. Students can instantly get answers about admissions, fees, courses, exams, placements, and more.

![EduBot Preview](docs/preview.png)

---

## ✨ Features

- 💬 **AI Chat** — Powered by Claude (claude-sonnet) via Anthropic API
- 📚 **Knowledge Base** — Fast local KB lookup before hitting the API
- ⚑ **Flag System** — Students can flag incorrect answers for admin review
- 🔐 **Admin Portal** — Manage flagged answers and add new Q&A entries
- 📋 **Conversation History** — Session-based chat log in the sidebar
- 🎨 **Futuristic Dark UI** — Responsive, animated, polished interface
- ⚡ **No Backend Required** — Fully static, deploy anywhere

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/edubot-student-assistant.git
cd edubot-student-assistant
```

### 2. Add your Anthropic API key

Open `index.html` and find the `getBotReply` function. Replace the fetch headers section to include your key, **or** use the recommended environment approach via a proxy (see [Deployment](#deployment)).

> ⚠️ **Never commit your API key directly into the HTML file.**  
> Use the environment variable / proxy approach described below.

### 3. Run locally
```bash
# No build step needed — just open in browser
open index.html

# Or serve with any static server
npx serve .
# or
python3 -m http.server 8000
```

---

## 🗂️ Project Structure

```
edubot-student-assistant/
├── index.html          # Main app (all-in-one HTML/CSS/JS)
├── README.md           # Project documentation
├── requirements.txt    # Python deps (for local dev server / proxy)
├── server.py           # Optional Python proxy server (hides API key)
├── .env.example        # Environment variable template
├── .gitignore          # Files to exclude from Git
├── netlify.toml        # Netlify deployment config
├── vercel.json         # Vercel deployment config
├── docs/
│   └── DEPLOYMENT.md   # Detailed deployment guide
└── .github/
    └── workflows/
        └── deploy.yml  # GitHub Actions CI/CD workflow
```

---

## 🌐 Deployment

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for full instructions.

### Quickest option — Netlify (recommended)
1. Push this repo to GitHub
2. Go to [netlify.com](https://netlify.com) → **Add new site** → **Import from Git**
3. Set environment variable `ANTHROPIC_API_KEY` in Netlify dashboard
4. Deploy — done!

### GitHub Pages (static, no key hiding)
```bash
git push origin main
# Enable GitHub Pages in repo Settings → Pages → Deploy from branch: main
```

---

## 🔑 Admin Access

Default credentials (change in production!):

| Field    | Value      |
|----------|------------|
| Username | `admin`    |
| Password | `admin123` |

> Update credentials by editing the `adminLogin()` function in `index.html`.

---

## 🛠️ Customization

| What to change | Where |
|---|---|
| College name & info | `systemPrompt` in `getBotReply()` |
| Knowledge base entries | `const KB = [...]` array |
| Quick topic chips | `.topic-chip` buttons in HTML |
| Sidebar info cards | `#tab-info` section in HTML |
| Color theme | `:root` CSS variables |
| Admin credentials | `adminLogin()` function |

---

## 📦 Tech Stack

- **Frontend:** Vanilla HTML5, CSS3, JavaScript (ES6+)
- **AI:** [Anthropic Claude API](https://docs.anthropic.com) (`claude-sonnet-4-20250514`)
- **Fonts:** Google Fonts (Syne, Space Mono)
- **Deployment:** Netlify / Vercel / GitHub Pages

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙌 Contributing

Pull requests welcome! Please open an issue first to discuss changes.
