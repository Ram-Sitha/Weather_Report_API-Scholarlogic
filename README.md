# 🌦️ Weather Analytics ETL Pipeline

> **An End-to-End Weather Data Analytics Project using Python, SQL, Weather API, ETL Pipeline, GitHub Actions, and Data Visualization.**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-success?logo=githubactions)
![API](https://img.shields.io/badge/API-Weather-blue)
![ETL](https://img.shields.io/badge/ETL-Pipeline-purple)

---

# 📖 Project Overview

Weather data is generated every second around the world. This project demonstrates how real-world weather information can be collected, processed, stored, analyzed, and visualized using an **ETL (Extract → Transform → Load)** pipeline.

The application fetches weather information from a Weather API, cleans and transforms the data using Python, stores it in a SQL database, and generates meaningful reports, graphs, and answers to frequently asked questions.

The complete workflow is automated using **GitHub Actions**, making the project production-oriented and easy to maintain.

---

# 🎯 Project Objectives

✔ Collect live weather data from an API

✔ Store weather data in a SQL database

✔ Build a complete ETL pipeline

✔ Generate analytical reports

✔ Create interactive visualizations

✔ Answer weather-related FAQs using database queries

✔ Automate the workflow using GitHub Actions

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Data Processing |
| Weather API | Live Weather Data |
| MySQL | Data Storage |
| Pandas | Data Cleaning |
| SQLAlchemy / mysql-connector | Database Connection |
| Matplotlib / Plotly | Data Visualization |
| Git | Version Control |
| GitHub | Repository Management |
| GitHub Actions | CI/CD Automation |

---

# 📂 Project Workflow

```
               Weather API
                    │
                    ▼
          Extract Weather Data
                    │
                    ▼
          Clean & Transform Data
                    │
                    ▼
            Store into Database
                    │
                    ▼
         SQL Queries & Analysis
                    │
                    ▼
         Graphs & Dashboard
                    │
                    ▼
          FAQ Generation Report
```

---

# 🔄 ETL Pipeline

## 1️⃣ Extract

Weather data is fetched from the Weather API.

Collected information includes:

- Temperature
- Maximum Temperature
- Minimum Temperature
- Humidity
- Pressure
- Wind Speed
- Weather Condition
- Sunrise
- Sunset
- Date & Time

---

## 2️⃣ Transform

The raw data is cleaned and processed.

Transformation includes:

- Removing duplicates
- Handling missing values
- Formatting timestamps
- Unit conversion
- Standardizing weather conditions
- Calculating temperature difference
- Preparing analytical datasets

---

## 3️⃣ Load

The transformed data is stored inside the SQL database.

Database operations include:

- Insert new records
- Update existing records
- Prevent duplicate entries
- Store API execution logs

---

# 🗂️ Project Structure

```
Weather-Analytics-ETL/
│
├── .github/
│   └── workflows/
│       └── weather-etl.yml
│
├── config/
│   └── config.py
│
├── database/
│   ├── schema.sql
│   ├── connection.py
│   └── queries.sql
│
├── src/
│   ├── api.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── etl_pipeline.py
│
├── analysis/
│   ├── graphs.py
│   ├── faq.py
│   └── report.py
│
├── reports/
│   └── graphs/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .env
```

---

# 🗃️ Database Design

Main Tables

### 📍 Location

Stores city information.

```
location_id
city
state
country
latitude
longitude
```

---

### 🌤️ Weather

Stores weather records.

```
weather_id
location_id
temperature
min_temperature
max_temperature
humidity
pressure
wind_speed
weather_condition
weather_description
sunrise
sunset
recorded_at
```

---

### 📝 API Logs

Stores API execution history.

```
log_id
api_time
status
city
records_loaded
error_message
```

---

# 📊 Data Analysis

The project generates:

- Temperature Trend
- Humidity Analysis
- Wind Speed Analysis
- Pressure Analysis
- Weather Condition Frequency
- City Comparison
- Temperature Distribution
- Correlation Analysis

---

# 📈 Sample Visualizations

- 📉 Temperature Trend Line Chart
- 📊 Maximum vs Minimum Temperature
- 🌧 Humidity Analysis
- 🌪 Wind Speed Trend
- ☁ Weather Condition Distribution
- 🌍 City Comparison Dashboard
- 🔥 Heatmap Correlation Matrix

---

# ❓ Frequently Asked Questions

Examples:

✔ What is today's weather in Bangalore?

✔ What is the maximum temperature?

✔ Which city has the highest humidity?

✔ Which day recorded the highest temperature?

✔ Average temperature this week?

✔ Most common weather condition?

✔ Wind speed comparison?

✔ Humidity trend?

Each answer is generated directly from SQL queries and visualized using graphs.

---

# 🤝 Team Responsibilities

## 👨‍💻 Member 1

API Integration

- Weather API
- API Testing
- JSON Parsing

---

## 👨‍💻 Member 2

Database

- Schema Design
- SQL Queries
- Database Connection


---

# 🚀 Git Workflow

```
main
│
├── feature/api
│
├── feature/database
│
├── feature/etl
│
├── feature/analytics
│
└── feature/documentation
```

Each contributor works independently.

After code review:

```
Feature Branch
        │
        ▼
Pull Request
        │
        ▼
Code Review
        │
        ▼
Merge to Main
```

---

# ⚙️ GitHub Actions

Automation Tasks

✅ Install dependencies

✅ Run ETL Pipeline

✅ Execute Tests

✅ Check Code Quality

✅ Generate Reports

✅ Verify Database Connection

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/your-username/weather-analytics-etl.git
```

Move into Project

```bash
cd weather-analytics-etl
```

Install Requirements

```bash
pip install -r requirements.txt
```

Create Environment File

```
API_KEY=YOUR_API_KEY

DB_HOST=localhost

DB_NAME=weather

DB_USER=root

DB_PASSWORD=password
```

Run ETL Pipeline

```bash
python src/etl_pipeline.py
```

---

# 📋 Expected Output

The application will

✔ Fetch Live Weather Data

✔ Store Data into MySQL

✔ Clean & Transform Records

✔ Generate Reports

✔ Produce Graphs

✔ Answer FAQs

✔ Automate Execution using GitHub Actions

---

# 🌟 Future Enhancements

- Power BI Dashboard
- Machine Learning Weather Prediction
- Air Quality Analysis
- Rainfall Forecasting
- Mobile Application
- Email Alerts
- Real-Time Weather Dashboard
- Docker Deployment
- Cloud Deployment (AWS/Azure)

---

# 👨‍💻 Contributors

| Name | Role |
|------|------|
| Member 1 | API Integration |
| Member 2 | Database |
| Member 3 | ETL Pipeline |
| Member 4 | Analytics |
| Member 5 | Documentation & CI/CD |

---

# ⭐ If you found this project useful, don't forget to Star the repository!
