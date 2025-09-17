# FastAPI News Fetcher with Celery & MySQL

This project is a **FastAPI-based backend** that integrates with the **News API**, uses **Celery** for periodic background tasks, and stores fetched news in a **MySQL database**. It provides an API endpoint to query news articles by date and includes logging, error handling, and a custom middleware for measuring request processing time.

---

## 🚀 Features

- Fetches news from the News API every minute with **Celery**.
- Stores news articles in a **MySQL database**.
- Provides a REST endpoint to query news by date.
- Implements logging with levels: `INFO`, `WARNING`, `ERROR`.
- Handles API and database errors gracefully.
- Includes a custom middleware to measure request processing time (`total_time_taken` in every API response).

---

## 🛠 Tech Stack

- **Python** (latest version)
- **FastAPI**
- **Celery**
- **Redis** (as Celery broker)
- **MySQL**
- **News API**

---

## ⚙️ Installation

### 1. Clone this repo
git clone https://github.com/your-username/fastapi-news-fetcher.git
cd fastapi-news-fetcher

### 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate # On Linux / macOS
venv\Scripts\activate # On Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up environment variables  
```
Create a `.env` file in the root directory:
NEWS_API_KEY=your_news_api_key_here
DATABASE_URL=mysql+mysqlconnector://user:password@localhost:3306/newsdb
REDIS_URL=redis://localhost:6379/0
```
---

## ▶️ Running the Application

### Start FastAPI server
uvicorn app.main:app --reload

### Start Celery worker
celery -A app.tasks.celery_app worker --loglevel=info

### Start Celery beat (for periodic tasks)
celery -A app.tasks.celery_app beat --loglevel=info

---

## 📡 API Endpoints

### Fetch news by date
GET /news?date=YYYY-MM-DD

#### Example request:
curl "http://127.0.0.1:8000/news?date=2025-09-17"

#### Example response:
```
{
"date": "2025-09-17",
"articles": [
{
"title": "Breaking News Example",
"description": "Some description...",
"source": "BBC",
"url": "https://example.com/article"
}
],
"total_time_taken": "12ms"
}
```

---

## 📝 Logging

- **INFO** → Successful operations (API calls, DB inserts).
- **WARNING** → Recoverable problems (partial failures).
- **ERROR** → Critical failures (News API down, DB connection issues).

---

## 🛡 Error Handling

- Gracefully handles **News API failures** (timeouts, bad responses).
- Handles **MySQL errors** with logging + safe fallbacks.
- Returns **user-friendly error messages** in API responses.

---

## 📂 Project Structure
```
fastapi-news-fetcher/
│── app/
│ ├── main.py # FastAPI entry point
│ ├── tasks.py # Celery tasks
│ ├── models.py # SQLAlchemy models
│ ├── database.py # DB connection setup
│ ├── crud.py # DB operations
│ ├── api.py # Routes / endpoints
│ ├── middleware.py # Custom middleware
│ └── utils.py # Helpers & logging config
│── requirements.txt
│── .env
│── README.md
```
---

## 📖 License

This project is licensed under the MIT License.
