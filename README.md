<div align="center">

# 🧠 Smart Token Optimizer

### AI-powered prompt analysis tool with intelligent token management

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![python-dotenv](https://img.shields.io/badge/python--dotenv-Env%20Security-ECD53F?style=for-the-badge&logo=dotenv&logoColor=black)](https://pypi.org/project/python-dotenv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

<br/>

> **Optimize your AI prompts before they cost you.** Smart Token Optimizer counts tokens, enforces limits, and delivers AI-generated responses — all from the terminal.

<br/>

[🚀 Features](#-features) • [📁 Project Structure](#-project-structure) • [⚙️ Installation](#️-installation) • [🔐 Environment Setup](#-environment-setup) • [▶️ Usage](#️-usage) • [🔮 Future Plans](#-future-improvements)

</div>

---

## 📖 Overview

**Smart Token Optimizer** is a Python-based CLI tool that brings awareness and control to how you interact with large language models. Before sending any prompt to Google's Gemini API, it analyzes the token count, warns you if you're approaching the limit, and only then generates an AI response.

This project demonstrates real-world API integration, secure credential management, and practical token-cost awareness — skills directly relevant to building production-grade AI applications.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔢 **Token Counter** | Counts the number of tokens in any user prompt before API call |
| ⚠️ **Limit Checker** | Compares token count against a predefined threshold |
| 🚨 **Smart Warning** | Displays a clear warning message if the prompt is too large |
| 🤖 **AI Response** | Sends prompt to Google Gemini and streams back the response |
| 🔐 **Secure API Keys** | Credentials stored safely using `.env` file — never hardcoded |
| 🧩 **Minimal & Modular** | Clean, readable Python code — easy to extend |

---

## 📁 Project Structure

```
smart-token-optimizer/
│
├── main.py                 # Entry point — runs the full token check + AI flow
├── token_utils.py          # Token counting and limit validation logic
├── gemini_client.py        # Gemini API integration (google-genai)
├── .env                    # 🔒 Secret API key (never commit this!)
├── .env.example            # ✅ Safe template to share with others
├── .gitignore              # Ensures .env is excluded from version control
├── requirements.txt        # All project dependencies
└── README.md               # You are here
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.10 or higher
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Step-by-Step Setup

**1. Clone the repository**

```bash
git clone https://github.com/your-username/smart-token-optimizer.git
cd smart-token-optimizer
```

**2. Create and activate a virtual environment**

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```
google-genai
python-dotenv
```

---

## 🔐 Environment Setup

This project uses `python-dotenv` to load your API key securely from a `.env` file. Your key is **never hardcoded** in the source code.

### Step 1 — Create your `.env` file

```bash
cp .env.example .env
```

### Step 2 — Add your API key

```env
# .env
GEMINI_API_KEY=your_actual_api_key_here
```

### `.env.example` (safe to commit ✅)

```env
# .env.example — copy this file to .env and fill in your key
GEMINI_API_KEY=your_gemini_api_key_here
```

> ⚠️ **Never commit your `.env` file.** It is listed in `.gitignore` by default.

---

## ▶️ Usage

Run the main script:

```bash
python main.py
```

You will be prompted to enter your text. The tool will:
1. Count the tokens in your input
2. Check against the token limit
3. Show a warning if the limit is exceeded
4. Send the prompt to Gemini and display the AI response

### Code Snippet — Core Logic

```python
# main.py
from token_utils import count_tokens, is_within_limit
from gemini_client import get_gemini_response

TOKEN_LIMIT = 500

user_prompt = input("Enter your prompt: ")
token_count = count_tokens(user_prompt)

print(f"\n🔢 Token Count: {token_count}")

if not is_within_limit(token_count, TOKEN_LIMIT):
    print(f"⚠️  Warning: Prompt exceeds the {TOKEN_LIMIT}-token limit!")
else:
    print("✅ Token count is within the safe limit.")

print("\n🤖 Gemini Response:\n")
print(get_gemini_response(user_prompt))
```

---

## 🖥️ Example Output

```
Enter your prompt: Explain the concept of machine learning in simple terms.

🔢 Token Count: 12
✅ Token count is within the safe limit.

🤖 Gemini Response:

Machine learning is a way of teaching computers to learn from examples,
rather than explicitly programming every rule. Instead of writing code
that says "if this, do that," you show the computer thousands of examples
and it figures out the patterns on its own...
```

**When the token limit is exceeded:**

```
Enter your prompt: [very long prompt...]

🔢 Token Count: 623
⚠️  Warning: Prompt exceeds the 500-token limit!
Consider shortening your prompt before sending it to the model.
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 **Python 3.10+** | Core programming language |
| 🤖 **Google Gemini API** (`google-genai`) | AI response generation |
| 🔑 **python-dotenv** | Secure environment variable management |

---

## 🔮 Future Improvements

- [ ] 🌐 **Web UI** — Build a Streamlit interface for non-technical users
- [ ] 📊 **Token Cost Estimator** — Show estimated API cost per prompt based on token count
- [ ] 🗂️ **Prompt History** — Save and review past prompts and their token stats
- [ ] 🧪 **Multi-model Support** — Extend to support OpenAI, Claude, and other APIs
- [ ] 📈 **Analytics Dashboard** — Visualize token usage trends over time
- [ ] ⚡ **Async Streaming** — Stream Gemini responses token-by-token for better UX

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m "Add: your feature description"`
4. **Push** to your branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

Please make sure your code follows existing style conventions and includes comments where needed.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built by [Himanshi Chouhan](https://github.com/your-username)**

*If you found this useful, consider giving it a ⭐ — it helps others discover it!*

</div>
