from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def show_form():
    return FileResponse("Dir_for_photo/form.html")

@app.post("/Dir_for_photo")
def add_foto():
    pass