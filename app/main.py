from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import psutil
import os

app = FastAPI()

# Mount static files under /static
app.mount("/static", StaticFiles(directory=os.path.join("app", "static")), name="static")


# Serve index.html explicitly at root
@app.get("/", response_class=HTMLResponse)
def read_index():
    with open("app/static/index.html") as f:
        return HTMLResponse(content=f.read())


# API endpoint
@app.get("/api/stats")
def get_stats():
    cpu_percents = psutil.cpu_percent(interval=0.1, percpu=True)
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    disk = psutil.disk_usage("/")
    return JSONResponse(
        content={
            "hostname": os.uname().nodename,
            "cpu": cpu_percents,
            "mem": mem.percent,
            "swap": swap.percent,
            "disk": disk.percent,
        }
    )
