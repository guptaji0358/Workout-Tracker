# Workout-Tracker
DAY - 38/100 - Project - Python X Workout Tracker

# 🏋️ Workout Tracker – Nutrition + Google Sheets API Integration

A Python-based backend project that:

- Accepts natural language workout input  
- Calculates calories using the Nutrition API  
- Formats duration (minutes → hours/minutes)  
- Stores workout data in Google Sheets via Sheety API  
- Uses Bearer Authentication for secure access  

---

## 🚀 Features

- Natural language exercise parsing  
- Automatic calorie calculation  
- Smart duration formatting:
  - `45` → `45 Minutes`
  - `100` → `1 Hour 40 Minutes`
  - `300` → `05 Hour`
- Multi-exercise support
- Secure API authentication (Nutrition + Sheety)
- Clean backend structure

---

## 🛠 Technologies Used

- Python 3
- `requests` library
- Nutrition API (100 Days of Python)
- Sheety API
- Google Sheets

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/guptaji0358/Workout-Tracker.git
cd workout-tracker
```

Install dependencies:

```bash
pip install requests
```

Or if using requirements file:

---

## 🔑 Setup Instructions

### 1️⃣ Setup Nutrition API

1. Go to:  
   https://app.100daysofpython.dev
2. Register / Login
3. Generate:
   - APP_ID
   - API_KEY

Paste them inside `main.py`:

```python
APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"
```

---

### 2️⃣ Setup Google Sheet

1. Create a new Google Sheet
2. Add columns exactly like this:

| Date | Time | Exercise | Duration | Calories |

3. Save it

---

### 3️⃣ Setup Sheety

1. Go to: https://sheety.co
2. Create a new project
3. Paste your Google Sheet URL
4. Enable:
   - GET
   - POST
5. Go to Authentication → Enable **Bearer Token**
6. Create a secret token

Copy:

- Your Sheety endpoint URL
- Your Bearer token

Paste into `main.py`:

```python
Sheety_Endpoint_base_URL = "YOUR_SHEETY_ENDPOINT"

sheety_headers = {
    "Authorization": "Bearer YOUR_BEARER_TOKEN"
}
```

---

## ▶️ Running the Project

```bash
python 38_WORKOUT_TRACKER.py
```

Example input:

```
I ran for 2 hours and walked for 30 minutes
```

The script will:

- Call Nutrition API
- Format duration
- Send data to Google Sheets
- Print status code

---

## 🔐 Security Note

Do NOT upload:

- APP_ID
- API_KEY
- Bearer Token
- Real Sheety endpoint

If making the project public, replace them with placeholders.

---

## 📂 Project Structure

```
workout-tracker/
│
├── main.py
└── README.md
```

---

## 📈 Example Output (Google Sheet)

| Date       | Time     | Exercise | Duration        | Calories |
|------------|----------|----------|-----------------|----------|
| 23/02/2026 | 21:48:34 | Running  | 01 Hour 30 Minutes | 650 |

---

## 🎯 Learning Outcome

This project demonstrates:

- REST API integration
- JSON handling
- Authentication headers
- Backend data transformation
- Multi-API communication
- Clean architecture practices

---

## 💪 Author
Robin Gupta
Built as part of the **100 Days of Python** challenge.

---

⭐ If you found this helpful, consider starring the repo!
