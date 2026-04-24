📦 viewerinfo — Streamlit Viewer Analytics Package
viewerinfo is a lightweight, modular Python package that captures browser, device, IP, and geolocation information from Streamlit apps.
It also includes a ready‑to‑use Viewer Analytics Dashboard that logs visits and visualizes usage patterns.

This package is designed for:

Classroom analytics

Product usage tracking

Device/browser compatibility insights

Lightweight visitor logging for Streamlit apps

🚀 Features
✔ Device & Browser Detection
Parses user‑agent strings to extract:

Browser + version

Operating system + version

Device type (PC / Mobile / Tablet)

✔ IP Detection
Automatically extracts IP from Streamlit request headers.

✔ Geolocation (when deployed)
Uses public IP to fetch:

Country

Region

City

Latitude / Longitude

✔ Logging
Every visit is appended to a CSV log:

Code
examples/logs/viewer_log.csv
✔ Analytics Dashboard
A Streamlit dashboard that displays:

Live viewer info

Aggregated browser/OS stats

Device type distribution

Country distribution (when deployed)

Filters + charts

Raw data table

📁 Project Structure
Code
viewerinfo/
│
├── viewerinfo/                 # Core package
│   ├── ip.py
│   ├── device.py
│   ├── geo.py
│   ├── logger.py
│   ├── streamlit_adapter.py
│   └── __init__.py
│
├── examples/
│   ├── streamlit_example.py    # Minimal usage example
│   ├── viewer_dashboard.py     # Full analytics dashboard
│   └── logs/                   # Auto‑generated logs
│
├── pyproject.toml
└── README.md
🛠 Installation
Clone the repo:

bash
git clone https://github.com/<your-username>/<repo-name>.git
cd viewerinfo
Create and activate a virtual environment:

bash
python -m venv venv
venv\Scripts\activate
Install the package in editable mode:

bash
pip install -e .
Install Streamlit:

bash
pip install streamlit
🧪 Quick Start
1. Run the minimal example
bash
python -m streamlit run examples/streamlit_example.py
This displays the raw viewer info as JSON.

2. Run the full analytics dashboard
bash
python -m streamlit run examples/viewer_dashboard.py
This opens:

Live viewer info

Browser/OS charts

Device type distribution

Filters

Logged history

📊 Dashboard Preview
The dashboard automatically logs each visit and visualizes:

Browser distribution

OS distribution

Device type

Country (when deployed)

Raw data table

Logs are stored in:

Code
examples/logs/viewer_log.csv
🌐 Deployment Notes
Localhost cannot provide:

Real IP

Real geolocation

To get full analytics, deploy using:

Streamlit Cloud

ngrok

Reverse proxy (nginx)

Public server

Once deployed, the dashboard will show:

Real IP

Real country

Real city

Real lat/long

🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to modify.

📄 License
This project is licensed under the MIT License.