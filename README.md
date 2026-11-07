# Chat Analysis App [![CI Status](https://github.com/sidrahmukati/WhatsApp_chat_analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/sidrahmukati/WhatsApp_chat_analyzer/actions/workflows/ci.yml) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A Streamlit-based web application that analyzes WhatsApp chat history, generates rich visual insights, word clouds, and detailed user activity statistics.

## Features
- **Activity Timelines:** Analyze message volume trends by daily, monthly, and hourly patterns.
- **User Statistics:** Breakdown of total messages, words, media shared, and links sent per participant.
- **Emoji & Word Analysis:** Discover the most frequently used emojis and custom word clouds.
- **Interactive Filtering:** Filter and analyze individual users or group-wide conversations.

## Technologies Used
- Python
- Streamlit
- Pandas & NumPy
- Matplotlib & Seaborn
- Docker & GitHub Actions (CI)

## Project Structure
```text
WhatsApp_chat_analyzer/
├── .github/workflows/ci.yml
├── data/sample_chat.txt
├── app.py
├── helper.py
├── preprocessor.py
├── Dockerfile
├── requirements.txt
└── README.md

## How to Run Locally

1. Clone the repository:

```bash
git clone [https://github.com/sidrahmukati/WhatsApp_chat_analyzer.git](https://github.com/sidrahmukati/WhatsApp_chat_analyzer.git)
cd WhatsApp_chat_analyzer
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```
## Try with Sample Data

Want to test the app right away without exporting your own personal chat? You can use the pre-formatted sample chat file located at `data/sample_chat.txt` in this repository! Just upload it into the app web interface.

## Deployment

This application can be deployed using Streamlit Community Cloud by connecting the GitHub repository and selecting `app.py` as the main application file, or containerized using the provided `Dockerfile`.

## 🚀 Live Demo
Check out the live app here: [WhatsApp Chat Analyzer](https://whatsappchatanalyzer--001.streamlit.app/)
