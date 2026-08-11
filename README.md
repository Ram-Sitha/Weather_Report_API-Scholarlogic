# 🌦️ Weather API Data Analytics Dashboard

An end-to-end **Weather API Data Analytics Project** built using **Python, Pandas, MySQL, SQL, HTML, CSS, JavaScript, and Power BI**.

This project collects real-time weather data from the **OpenWeather API**, performs an **ETL (Extract, Transform, Load)** process using Python, stores the processed data in MySQL, performs SQL-based analysis, and presents insights through **Power BI** and a **responsive web dashboard**.

---

## 📌 Project Overview

The Weather API Data Analytics Dashboard demonstrates a complete data analytics workflow:

**OpenWeather API → Python ETL → Pandas → MySQL → SQL Analysis → Power BI / Web Dashboard**

The project is designed to demonstrate practical skills in:

* REST API integration
* Python programming
* Data extraction and transformation
* Database management
* SQL analysis
* Data visualization
* Frontend development
* Git and GitHub

---

## 🎯 Project Objectives

* Collect real-time weather data using the OpenWeather API.
* Extract and process JSON weather data using Python.
* Clean and transform data using Pandas.
* Store processed data in MySQL.
* Perform analytical queries using SQL.
* Build an interactive Power BI dashboard.
* Develop a responsive HTML/CSS/JavaScript dashboard.
* Create a reusable ETL pipeline.
* Maintain the project using Git and GitHub.

---

## 🛠️ Technology Stack

| Category             | Technology            |
| -------------------- | --------------------- |
| Programming Language | Python                |
| API                  | OpenWeather API       |
| Data Processing      | Pandas                |
| Data Format          | JSON                  |
| Database             | MySQL                 |
| Query Language       | SQL                   |
| Data Visualization   | Power BI              |
| Frontend             | HTML, CSS, JavaScript |
| Version Control      | Git, GitHub           |

---

## 🏗️ Project Architecture

```text
                    OpenWeather API
                           │
                           ▼
                  Python Extraction
                           │
                           ▼
                    Raw JSON Data
                  weather_raw.json
                           │
                           ▼
                  Pandas Transformation
                           │
                           ▼
                Processed CSV Data
              weather_processed.csv
                           │
                           ▼
                    MySQL Database
                     weather_data
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
        SQL Analysis              Web Dashboard
              │                         │
              └────────────┬────────────┘
                           ▼
                    Power BI Dashboard
```

---

## 📂 Project Structure

```text
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
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

# 🔄 ETL Pipeline

## 1️⃣ Extract

The Python extraction script connects to the OpenWeather API and retrieves real-time weather information.

The raw API response is stored as:

```text
data/raw/weather_raw.json
```

### Data collected includes:

* City
* Country
* Temperature
* Feels Like Temperature
* Humidity
* Atmospheric Pressure
* Wind Speed
* Weather Condition
* Weather Description
* Timestamp

---

## 2️⃣ Transform

The transformation process uses **Pandas** to clean and prepare the data.

### Transformation steps:

* Read JSON data.
* Extract required fields.
* Handle missing values.
* Remove duplicate records.
* Convert timestamps.
* Format weather attributes.
* Convert data into CSV format.

Output:

```text
data/processed/weather_processed.csv
```

---

## 3️⃣ Load

The processed data is loaded into a **MySQL database** using Python.

Database table:

```text
weather_data
```

The load process includes:

* MySQL connection
* Database/table creation
* CSV data insertion
* Data validation

---

# 📊 SQL Analysis

SQL queries are used to analyze the stored weather data.

### Analysis includes:

* Total number of weather records
* Average temperature
* Maximum temperature
* Minimum temperature
* Average humidity
* Average atmospheric pressure
* Average wind speed
* Weather condition distribution
* Daily weather summary
* Highest temperature records

Example:

```sql
SELECT AVG(temperature)
FROM weather_data;
```

---

# 📈 Power BI Dashboard

The Power BI dashboard provides an interactive view of the weather data.

### Dashboard Components

* 🌡️ Temperature KPI
* 💧 Humidity KPI
* 🌬️ Wind Speed KPI
* 📊 Pressure KPI
* 📈 Temperature Trend
* 💧 Humidity Trend
* 🌬️ Wind Speed Analysis
* ☁️ Weather Distribution
* 📋 Weather Summary
* 🔎 Interactive Filters

---

# 🌐 Web Dashboard

A responsive frontend dashboard has also been developed using:

* HTML
* CSS
* JavaScript

### Pages

```text
🏠 Dashboard
🌤️ Current Weather
📊 Analytics
📋 Weather History
ℹ️ About Project
```

### Features

* Responsive design
* Modern user interface
* Sidebar navigation
* Weather information cards
* Weather statistics
* Historical weather data
* Analytics section
* Project information page

---

# 📸 Screenshots

Project screenshots can be found inside:

```text
screenshots/
```

Recommended screenshots:

```text
screenshots/
│
├── dashboard.png
├── weather.png
├── analytics.png
├── history.png
├── about.png
├── powerbi.png
└── mysql.png
```

> 📌 Add your actual screenshots to the `screenshots` folder before publishing the repository.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Weather_Report_API.git
```

## 2. Navigate to the Project

```bash
cd Weather_Report_API
```

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv env
```

Activate:

```bash
env\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv env
```

Activate:

```bash
source env/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Configuration

Before running the project, configure the required API and database credentials.

Create an environment file:

```text
.env
```

Example:

```text
OPENWEATHER_API_KEY=your_api_key
MYSQL_HOST=localhost
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=weather_db
```

### ⚠️ Security

**Never upload your API key or database password to GitHub.**

Add the following to `.gitignore`:

```text
.env
env/
venv/
__pycache__/
*.pyc
```

---

# ▶️ Running the Project

## Run the complete ETL pipeline

```bash
python scripts/run_pipeline.py
```

Or execute each step separately.

### Extract

```bash
python scripts/extract.py
```

### Transform

```bash
python scripts/transform.py
```

### Load

```bash
python scripts/load.py
```

---

# 🗄️ Database Setup

Import the database schema:

```bash
mysql -u root -p < sql/schema.sql
```

Then verify the database:

```sql
SHOW DATABASES;
```

Select the weather database:

```sql
USE weather_db;
```

Check the table:

```sql
SHOW TABLES;
```

View weather data:

```sql
SELECT * FROM weather_data;
```

---

# 🚀 Features

* ✅ Real-time Weather API Integration
* ✅ Python-based ETL Pipeline
* ✅ JSON Data Processing
* ✅ Pandas Data Cleaning
* ✅ MySQL Database Integration
* ✅ SQL Data Analysis
* ✅ Power BI Dashboard
* ✅ Responsive Web Dashboard
* ✅ Git & GitHub Version Control
* ✅ Automation-ready Pipeline

---

# 🔮 Future Enhancements

The project can be extended with:

* 🌍 Multi-city weather support
* 🔮 Weather forecast analysis
* 🤖 Machine learning weather prediction
* ☁️ AWS/cloud deployment
* 🔄 Automated Power BI refresh
* 📧 Email weather alerts
* 🔐 User authentication
* 🌙 Dark mode
* 🐳 Docker containerization
* ⚙️ Jenkins CI/CD pipeline
* ☸️ Kubernetes deployment

---

# 💼 Skills Demonstrated

### Programming

* Python
* Pandas
* REST API
* JSON

### Database

* MySQL
* SQL
* Data Modeling

### Visualization

* Power BI
* Data Analytics

### Frontend

* HTML
* CSS
* JavaScript

### DevOps / Tools

* Git
* GitHub
* Linux
* Automation

---

# 👨‍💻 Developer

**Duvvuru Charan Teja**

**Python Developer | Data Analytics Learner**

### Technologies

```text
Python
MySQL
SQL
Power BI
HTML
CSS
JavaScript
Git
GitHub
```

---

# 📄 License

This project is developed for **educational and portfolio purposes**.

---

# ⭐ Support

If you find this project useful, please consider giving the repository a ⭐ on GitHub.

---

## 🙏 Thank You

Thank you for visiting this project.

Feel free to explore the source code, provide feedback, and contribute to future improvements.
