# Academic Bank of Credits (ABC) Analytics System

## 📌 Project Overview
The **Academic Bank of Credits (ABC) Analytics System** is a mini data-driven platform designed to simulate the core functionality of the Government of India's **Academic Bank of Credits (ABC)** initiative.  
It allows tracking of student credits, course completion, and institutional performance, and provides analytics-ready data for dashboards and reporting.

This project is built to demonstrate:
- Data ingestion (ETL)
- Data storage using SQL
- Backend API development
- Analytics & dashboard readiness

---

## 🎯 Objectives
- Store and manage student academic credits
- Enable analytics for credit utilization and completion ratio
- Prepare clean, validated data for dashboarding tools (Power BI / Tableau)
- Simulate real-world digital governance use case

---

## 🛠️ Tech Stack
| Layer | Technology |
|------|------------|
Backend | Python, Flask |
Database | MySQL |
Data Processing | Pandas |
API | REST (Flask) |
Visualization | Power BI |
Tools | Git, VS Code |

---

## 📂 Project Structure

```
ABC_Project/
│
├── app.py
├── database.py
├── requirements.txt
│
├── data/
│ └── students.csv
│
├── templates/
│ └── index.html
│
└── dashboards/
└── abc_dashboard.pbix
```


---

## ⚙️ Features
- Load student credit data from CSV into MySQL
- Store student name, credits, and institution
- Expose REST API endpoints for data loading
- Prepare data for analytics dashboards
- Data validation and integrity checks

---

## 🗄️ Database Schema

```sql
CREATE DATABASE abc_db;

USE abc_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    credits INT,
    institution VARCHAR(100)
);
```
##1️⃣ Clone the Repository
```
git clone https://github.com/yourusername/ABC_Project.git
cd ABC_Project
```
##2️⃣ Create Virtual Environment (Optional but Recommended)
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
##3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
##4️⃣ Setup MySQL Database
###Open MySQL
```
Create database and table using the schema above
```
###Update credentials in database.py
```
host="localhost",
user="root",
password="yourpassword",
database="abc_db"
```
##5️⃣ Run the Flask App
```
python app.py
```
```
Running on http://127.0.0.1:5000/
```

##6️⃣ Load Sample Data into Database

Open browser and go to:
```
http://127.0.0.1:5000/load_data
```

You will get:
```
{"status": "Data Loaded Successfully"}

```







