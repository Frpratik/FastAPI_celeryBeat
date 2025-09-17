import requests
from datetime import datetime
from sqlalchemy.orm import Session
from .celery_worker import celery
from .database import SessionLocal
from .models import News
from .logger import logger

NEWS_API_KEY = "0255081ec458484ebd58577606c28506"
NEWS_API_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

@celery.task
def fetch_news():
    logger.info("Starting fetch_news task...")

    try:
        logger.info(f"Requesting news from API: {NEWS_API_URL}")
        response = requests.get(NEWS_API_URL)
        response.raise_for_status()

        articles = response.json().get("articles", [])
        logger.info(f"Fetched {len(articles)} articles from API.")

        db: Session = SessionLocal()
        added_count = 0

        for article in articles:
            try:
                news = News(
                    title=article.get("title"),
                    description=article.get("description"),
                    url=article.get("url"),
                    published_date=datetime.strptime(article["publishedAt"][:10], "%Y-%m-%d").date()
                )
                db.add(news)
                added_count += 1
            except Exception as inner_err:
                logger.warning(f"Skipping article due to error: {inner_err}")

        db.commit()
        db.close()
        logger.info(f"Successfully saved {added_count} articles to the database.")

    except Exception as e:
        logger.error(f"Error in fetch_news task: {e}")
