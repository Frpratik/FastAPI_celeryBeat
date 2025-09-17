from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .database import get_db
from .models import News
from .logger import logger

router = APIRouter()

@router.get("/news")
def get_news(date: str, db: Session = Depends(get_db)):
    logger.info(f"Received request for news on date: {date}")

    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        logger.warning(f"Invalid date format received: {date}")
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")

    news_list = db.query(News).filter(News.published_date == date_obj).all()
    logger.info(f"Found {len(news_list)} articles for {date_obj}")

    return {"count": len(news_list), "articles": news_list}
