# 🌦 Weather API Data Analytics Dashboard

An end-to-end **Weather API Data Analytics Project** developed using **Python, MySQL, SQL, HTML, CSS, JavaScript, and Power BI**. This project collects real-time weather data from the OpenWeather API, performs ETL (Extract, Transform, Load), stores the processed data in MySQL, analyzes the data using SQL, and visualizes insights through both a **Power BI Dashboard** and a **responsive HTML Dashboard**.

---

# 📌 Project Overview

The Weather API Data Analytics Dashboard is designed to demonstrate a complete data analytics workflow. The application fetches live weather information from the OpenWeather API, transforms the raw JSON data into a structured format, stores it in a MySQL database, performs SQL analysis, and presents meaningful insights using Power BI and a custom-built HTML dashboard.

---

# 🎯 Project Objectives

- Collect real-time weather data using OpenWeather API.
- Build a complete ETL pipeline using Python.
- Clean and transform JSON data using Pandas.
- Store processed data in MySQL.
- Perform SQL-based analysis.
- Develop an interactive Power BI Dashboard.
- Create a responsive HTML, CSS & JavaScript dashboard.
- Automate the weather data collection process.

---

# 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| API | OpenWeather API |
| Data Processing | Pandas |
| Data Format | JSON |
| Database | MySQL |
| Query Language | SQL |
| Dashboard | Power BI |
| Frontend | HTML, CSS, JavaScript |
| Version Control | Git & GitHub |

---

# 🏗 Project Architecture

```
             OpenWeather API
                    │
                    ▼
          Extract (Python Script)
                    │
                    ▼
         weather_raw.json (Raw Data)
                    │
                    ▼
        Transform (Pandas Cleaning)
                    │
                    ▼
   weather_processed.csv (Processed Data)
                    │
                    ▼
            Load into MySQL Database
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
 SQL Analysis             HTML Dashboard
        │                       │
        └───────────┬───────────┘
                    ▼
             Power BI Dashboard
```

---

# 📂 Project Folder Structure

```
Weather_Report_API/
│
├── config/
│   ├── config.py
│   └── __init__.py
│
├── data/
│   ├── raw/
│   │   └── weather_raw.json
│   │
│   └── processed/
│       └── weather_processed.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── run_pipeline.py
│
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── frontend/
│   ├── index.html
│   ├── weather.html
│   ├── analytics.html
│   ├── history.html
│   ├── about.html
│   ├── style.css
│   └── script.js
│
├── dashboard/
│   └── Weather_Dashboard.pbix
│
├── docs/
├── logs/
├── screenshots/
├── tests/
│
├── README.md
├── requirements.txt
└── main.py
```

---

# 🔄 ETL Workflow

## Step 1 – Extract

- Connect to OpenWeather API.
- Fetch live weather data.
- Store the response as JSON.

Output:

```
weather_raw.json
```

---

## Step 2 – Transform

- Read JSON file.
- Extract required weather attributes.
- Remove null values.
- Remove duplicate records.
- Convert data into CSV format.

Output:

```
weather_processed.csv
```

---

## Step 3 – Load

- Connect Python to MySQL.
- Create database table.
- Insert processed CSV data into MySQL.

Output:

```
weather_data
```

---

# 📊 SQL Analysis

The project performs various SQL analyses including:

- Total Weather Records
- Average Temperature
- Maximum Temperature
- Minimum Temperature
- Average Humidity
- Average Pressure
- Average Wind Speed
- Weather Distribution
- Daily Weather Summary
- Top Temperature Records

---

# 📈 Power BI Dashboard

The Power BI dashboard provides:

- KPI Cards
- Temperature Trend
- Humidity Trend
- Pressure Trend
- Wind Speed Analysis
- Weather Distribution
- Interactive Filters
- Weather Summary Table

---

# 🌐 HTML Dashboard

The frontend dashboard contains the following pages:

- 🏠 Dashboard
- 🌤 Current Weather
- 📊 Analytics
- 📋 Weather History
- ℹ About Project

Features:

- Responsive Design
- Modern UI
- Sidebar Navigation
- Weather Cards
- Statistics
- Weather History
- Project Information

---

# 📸 Screenshots

```
screenshots/

dashboard.png

weather.png

analytics.png

history.png

about.png

powerbi.png

mysql.png
```

(Add screenshots after completing the project.)

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Weather_Report_API.git
```

---

## Navigate to Project

```bash
cd Weather_Report_API
```

---

## Create Virtual Environment

```bash
python -m venv env
```

---

## Activate Virtual Environment

Windows

```bash
env\Scripts\activate
```

Linux / Mac

```bash
source env/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Execution Steps

Extract Data

```bash
python scripts/extract.py
```

Transform Data

```bash
python scripts/transform.py
```

Load Data

```bash
python scripts/load.py
```

Run Complete Pipeline

```bash
python scripts/run_pipeline.py
```

---

# 📋 Features

- Live Weather API Integration
- End-to-End ETL Pipeline
- JSON Processing
- Data Cleaning using Pandas
- MySQL Integration
- SQL Analytics
- Interactive Power BI Dashboard
- Responsive HTML Dashboard
- Automation Support
- Git Version Control

---

# 🚀 Future Enhancements

- Multi-City Weather Support
- Weather Forecast Analysis
- Machine Learning Prediction
- Cloud Deployment
- Power BI Scheduled Refresh
- Email Alerts
- Login Authentication
- Dark Mode

---

# 💼 Skills Demonstrated

- Python Programming
- REST API Integration
- ETL Development
- Pandas
- JSON Processing
- MySQL
- SQL
- Power BI
- HTML
- CSS
- JavaScript
- Git & GitHub
- Data Analytics
- Data Engineering Basics

---

# 👨‍💻 Developer

**Kurva Ramanjaneyulu**

**Role:** Python Developer | Data Analytics Learner

### Tech Stack

- Python
- MySQL
- SQL
- Power BI
- HTML
- CSS
- JavaScript

---

# 📄 License

This project is developed for educational and portfolio purposes.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 🙏 Thank You

Thank you for visiting this project repository. Feel free to explore the source code, provide feedback, and contribute to future improvements.
