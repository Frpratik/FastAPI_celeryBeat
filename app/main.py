from fastapi import FastAPI
from .routes import router
from .middleware import TimerMiddleware

app = FastAPI(title="News API Service")

app.add_middleware(TimerMiddleware)
app.include_router(router)
