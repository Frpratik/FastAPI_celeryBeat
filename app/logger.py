import logging
import sys

# Configure root logger
logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),   # console logs
        logging.FileHandler("logs/app.log")  # logs saved to file
    ]
)

logger = logging.getLogger("app")
