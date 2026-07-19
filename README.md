# 🌦️ Weather Analytics ETL Pipeline

<div align="center">

# 🌍 Weather Analytics ETL Pipeline

### *Building an End-to-End Weather Data Engineering Pipeline using Python, MySQL, ETL & GitHub Actions*

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=24&duration=3500&pause=800&color=00BFFF&center=true&vCenter=true&width=700&lines=Weather+Analytics+ETL+Pipeline;Python+%7C+MySQL+%7C+ETL+%7C+GitHub+Actions;Data+Engineering+Project;Automated+Weather+Analytics" />
</p>

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?logo=pandas)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-success?logo=githubactions)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Graphs-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

### 🚀 End-to-End Data Engineering Project

Extract ➜ Transform ➜ Load ➜ Analyze ➜ Visualize ➜ Automate

</div>

---

# 📖 Project Overview

This project demonstrates how a **real-world ETL (Extract, Transform, Load)** pipeline works by collecting live weather information from the **Open-Meteo API**, processing it with Python, storing it inside a **MySQL database**, generating analytical reports, visualizations, and automating the entire workflow using **GitHub Actions**.

Instead of only displaying live weather, the project stores historical snapshots that can later be analyzed for trends, comparisons, and reporting.

---

# ✨ Features

* 🌍 Fetch live weather data for multiple cities
* 🗺️ Automatic geocoding (city → latitude & longitude)
* 🔄 Complete ETL pipeline
* 🗄️ Store data in MySQL
* 📊 Generate CSV reports
* 📈 Generate weather graphs
* ❓ Automatically generate FAQ reports
* ⚙️ GitHub Actions automation
* 🧪 Unit testing with Pytest
* 📁 Clean project architecture

---

# 🏗️ Project Architecture

```mermaid
flowchart TD

A[City Names]
B[Open-Meteo Geocoding API]
C[Latitude & Longitude]
D[Weather API]
E[Extract]
F[Transform]
G[Load]
H[(MySQL)]
I[Pandas Analysis]
J[Graphs]
K[FAQ Report]
L[GitHub Actions]

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> H
H --> I
I --> J
I --> K
L --> E
```

---

# 🛠️ Tech Stack

| Technology     | Purpose           |
| -------------- | ----------------- |
| Python         | Core Programming  |
| Open-Meteo API | Live Weather Data |
| MySQL          | Database          |
| SQLAlchemy     | ORM               |
| Pandas         | Data Analysis     |
| Matplotlib     | Visualization     |
| Git            | Version Control   |
| GitHub         | Repository        |
| GitHub Actions | Automation        |
| Pytest         | Testing           |

---

# 📂 Project Structure

```text
weather-analytics-etl/

├── .github/
│   └── workflows/
│       └── weather-etl.yml
│
├── reports/
│   ├── graphs/
│   ├── current_weather.csv
│   ├── daily_forecast.csv
│   └── faq_report.md
│
├── tests/
│
├── config.py
├── database.py
├── extract.py
├── transform.py
├── load.py
├── etl_pipeline.py
├── analysis.py
├── main.py
├── weather_codes.py
├── schema.sql
├── requirements.txt
└── README.md
```

---

# 🔄 ETL Workflow

## ① Extract

✔ Convert city names into coordinates

✔ Fetch weather information

✔ Receive JSON response

---

## ② Transform

✔ Remove unnecessary fields

✔ Convert timestamps

✔ Handle missing values

✔ Convert weather codes into readable descriptions

✔ Prepare structured records

---

## ③ Load

✔ Insert data into MySQL

✔ Prevent duplicate records

✔ Store execution logs

✔ Maintain historical weather data

---

# 🗄️ Database Schema

### Locations

```text
id
city
country
latitude
longitude
timezone
```

### Weather Records

```text
temperature
humidity
pressure
wind_speed
precipitation
weather_condition
recorded_at
```

### Daily Forecast

```text
forecast_date
min_temperature
max_temperature
precipitation
wind_speed
sunrise
sunset
```

### ETL Logs

```text
city
status
started_at
completed_at
records_loaded
error_message
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/USERNAME/weather-analytics-etl.git

cd weather-analytics-etl
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/weather_analytics

CITIES=Bengaluru,Chennai,Hyderabad,Mumbai,Delhi
```

---

## Run the Project

```bash
python main.py
```

Expected output:

```text
Step 1: Running ETL pipeline...

[SUCCESS] Bengaluru
[SUCCESS] Chennai
[SUCCESS] Hyderabad
[SUCCESS] Mumbai
[SUCCESS] Delhi

Step 2: Creating graphs...

Project completed successfully.
```

---

# 📊 Output

The project generates

```
reports/

current_weather.csv

daily_forecast.csv

faq_report.md

graphs/

max_temperature_trend.png

city_temperature_comparison.png

precipitation_by_city.png

temperature_vs_humidity.png
```

---

# 📈 Sample Analysis

The project answers questions such as:

* What is the current weather in each city?
* Which city has the highest temperature?
* Which city has the lowest temperature?
* Which city has the highest rainfall?
* Which city has the strongest wind?
* Which weather condition is most common?
* How does humidity vary with temperature?

---

# ⚙️ GitHub Actions Workflow

Every push to **main** automatically:

```text
Checkout Code

↓

Install Python

↓

Install Dependencies

↓

Run Tests

↓

Run ETL Pipeline

↓

Generate Reports

↓

Upload Reports
```

---

# 👨‍💻 Team Workflow

```mermaid
gitGraph

commit id:"Initial"

branch API

branch Database

branch ETL

branch Analytics

branch Documentation

checkout API
commit

checkout Database
commit

checkout ETL
commit

checkout Analytics
commit

checkout Documentation
commit

checkout main

merge API

merge Database

merge ETL

merge Analytics

merge Documentation
```

---

# 🧪 Run Tests

```bash
pytest
```

---

# 🌟 Future Improvements

* 📊 Power BI Dashboard
* 🤖 Machine Learning Weather Prediction
* 📱 Mobile Application
* ☁️ AWS Deployment
* 🐳 Docker Support
* 📈 Interactive Dashboards
* 📩 Email Weather Alerts
* 🌍 Global City Support

---

# 🤝 Contributors

| Member   | Responsibility                 |
| -------- | ------------------------------ |
| Member 1 | API Integration                |
| Member 2 | Database                       |
| Member 3 | ETL Pipeline                   |
| Member 4 | Analytics & Visualization      |
| Member 5 | Documentation & GitHub Actions |

---

<div align="center">

### ⭐ If you found this project helpful, consider giving it a Star!

**Built with ❤️ using Python, MySQL, ETL, and GitHub Actions**

</div>
