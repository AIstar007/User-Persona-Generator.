# 🧠 Reddit User Persona Generator (Ollama Version)

A Python tool that scrapes Reddit user content (posts & comments) and generates a user persona using **free and local LLMs** powered by [Ollama](https://ollama.com).

---

## 🚀 Features

- Scrapes Reddit user’s public posts and comments (no login or API key required)
- Generates a comprehensive **user persona**
- Uses a local model like Mistral via **Ollama** — no OpenAI API needed!
- Cites the exact Reddit posts/comments used for each insight
- Outputs the result as a `.txt` file

---

## 📂 Project Structure

```
reddit-persona-generator/
│
├── main.py                  # Main script
├── reddit_scraper.py        # For scraping user posts/comments
├── persona_builder.py       # For persona generation via LLM
├── output/
│   ├── kojied.txt
│   └── Hungry-Move-6603.txt
├── requirements.txt         # All dependencies
└── README.md                # Setup + Usage Instructions
```

---

## ⚙️ Requirements

Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## 🐘 Ollama Setup (One-Time)

1. Download and install Ollama: https://ollama.com
2. In terminal, run:

```bash
ollama run mistral
```

> This will download and start the Mistral model locally (4GB).
> Keep this window running while using the tool.

---

## 🛠️ How to Use

### Step 1: Run Ollama

In one terminal:
```bash
ollama run mistral
```

### Step 2: Generate Persona

In a separate terminal:
```bash
python main.py kojied
```

Output will be saved to:

```
output/kojied.txt
```

Repeat for other users like:

```bash
python main.py Hungry-Move-6603
```

---

## ✅ Sample Output

```
USER PERSONA: kojied

1. Interests:
- Technology, AI
  (Source: https://reddit.com/...)

2. Personality:
- Curious, logical
  (Source: https://reddit.com/...)
```

---

## 🧑‍💻 Author

Built by Alen Thomas for BeyondChats internship (48-hour assignment).

---

## 🔗 Credits

- [Ollama](https://ollama.com)
- [Mistral-7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
- Reddit JSON API
