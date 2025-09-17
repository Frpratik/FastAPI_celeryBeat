import time
from starlette.middleware.base import BaseHTTPMiddleware

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        total_time = (time.time() - start) * 1000
        if response.headers.get("content-type") == "application/json":
            response_body = b""
            async for chunk in response.body_iterator:
                response_body += chunk
            import json
            data = json.loads(response_body)
            data["total_time_taken_ms"] = round(total_time, 2)
            from starlette.responses import JSONResponse
            response = JSONResponse(content=data, status_code=response.status_code)
        return response
