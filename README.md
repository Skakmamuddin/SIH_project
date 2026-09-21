<div align="center">

# 🏔️ Landscape AI — Landslide Risk Predictor

**AI/ML-powered landslide susceptibility prediction for Northeast India**

Real-time weather • Terrain intelligence • Machine learning risk scoring • AI chat assistant • Live disaster news

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)

[🚀 Live Demo](https://sihproject-sihdisaster.streamlit.app) · [🐛 Report a Bug](https://github.com/Skakmamuddin/SIH_project/issues) · [✨ Request a Feature](https://github.com/Skakmamuddin/SIH_project/issues)

</div>

---

## 📖 About

**Landscape AI** is a landslide risk intelligence platform built for **Smart India Hackathon**, purpose-built for the terrain-sensitive, landslide-prone regions of **Northeast India**. It fuses live weather data, elevation/terrain features, and a trained machine learning model to generate an instant **landslide risk score** for any location — pinpointed via GPS or manual coordinates.

Beyond prediction, the platform layers on an **interactive risk map**, an **AI chat assistant** for natural-language guidance, and a **live news feed** for situational awareness — turning raw environmental data into something a field officer, planner, or citizen can actually act on.

<div align="center">
<img src="https://raw.githubusercontent.com/Skakmamuddin/SIH_project/main/Screenshot%202026-09-03%20164358.png" alt="App Screenshot" width="80%">
</div>

---

## ✨ Features

| | |
|---|---|
| 📍 **Smart Location Input** | One-tap GPS geolocation or precise manual lat/long entry |
| 🌦️ **Live Weather Intelligence** | Real-time temperature, humidity, rainfall & wind via Open-Meteo |
| ⛰️ **Terrain Analysis** | Elevation lookup used as a core model feature |
| 🤖 **ML Risk Prediction** | Trained classifier scores landslide susceptibility (Low / Moderate / High) |
| 🗺️ **Interactive Risk Map** | Click-to-select Folium map with color-coded risk zones |
| 💬 **AI Chat Assistant** | Natural-language Q&A powered by Mistral / Gemini |
| 📰 **News & Situation Awareness** | Live disaster and landslide-related news via Tavily search |
| 🔐 **User Accounts** | Lightweight authentication for personalized sessions |

<div align="center">
<img src="https://raw.githubusercontent.com/Skakmamuddin/SIH_project/main/chatbotscreenshot.png" alt="Chatbot Screenshot" width="80%">
</div>

---

## 🛠️ Tech Stack

<div align="center">

![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Folium](https://img.shields.io/badge/-Folium-77B829?style=flat-square&logo=leaflet&logoColor=white)

</div>

| Layer | Technology |
|---|---|
| **Frontend / App Framework** | Streamlit + `streamlit-folium` + `streamlit-geolocation` |
| **Machine Learning** | scikit-learn (Random Forest / Decision Tree), joblib |
| **Data / Numerics** | pandas, NumPy, Plotly |
| **Mapping** | Folium (Esri World Imagery tiles) |
| **Weather Data** | [Open-Meteo API](https://open-meteo.com/) |
| **AI Chat Assistant** | Mistral AI (`mistralai`), Google Gemini (`google-genai`) |
| **News & Search** | [Tavily](https://tavily.com/) search API |
| **Config** | `python-dotenv` |

---

## 📂 Project Structure

```
SIH_project/
├── Home.py                # Main entry point — dashboard, location input, risk cards
├── weather.py              # Open-Meteo weather integration
├── terrain.py               # Elevation / terrain lookup
├── train_model.py          # ML model training script
├── requirements.txt         # Python dependencies
├── run_streamlit.bat        # Windows launch script
├── assets/                  # Stylesheets & static assets
├── chatbot/                 # AI assistant logic
├── models/                  # Trained ML model artifacts
├── pages/                   # Additional Streamlit pages (Risk Map, News, etc.)
├── utils/                   # Auth, prediction, chat widget helpers
└── .env.example              # Environment variable template
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- API keys for [Open-Meteo](https://open-meteo.com/) *(no key required)*, [Tavily](https://tavily.com/), Mistral AI and/or Google Gemini

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Skakmamuddin/SIH_project.git
cd SIH_project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# then fill in your API keys in .env
```

### Environment Variables

Create a `.env` file in the project root (see `.env.example`):

```env
TAVILY_API_KEY=your_tavily_api_key
MISTRAL_API_KEY=your_mistral_api_key
GOOGLE_API_KEY=your_google_genai_api_key
```

### Run the App

```bash
streamlit run Home.py
```

The app will open at `http://localhost:8501` 🎉

---

## 🌐 Deployment

This app is deployed on **Streamlit Community Cloud**.

👉 **[Try the live app here](https://sihproject-sihdisaster.streamlit.app)**

When deploying your own instance, remember to add your API keys under **App Settings → Secrets** in TOML format:

```toml
TAVILY_API_KEY = "your-key"
MISTRAL_API_KEY = "your-key"
GOOGLE_API_KEY = "your-key"
```

---

## 🗺️ Roadmap

- [ ] Slope & soil-type integration for richer terrain features
- [ ] Historical landslide event overlay
- [ ] SMS / push alerts for high-risk zones
- [ ] Multi-language support for regional accessibility
- [ ] Mobile-first PWA experience

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source. Add your preferred license (e.g. [MIT](https://choosealicense.com/licenses/mit/)) here.

---

<div align="center">

Built with ❤️ for **Smart India Hackathon** — helping communities stay ahead of landslide risk.

⭐ **Star this repo if you find it useful!**

</div>
