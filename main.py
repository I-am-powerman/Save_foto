from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def show_form():
    return FileResponse("Dir_for_photo/form.html")

@app.post("/download")
async def upload_foto(file:UploadFile = File(...)):
    file_location = f"Dir_for_photo/{file.filename}"

    with open(file_location, "wb") as file_object:
        while contents := await file.read(1024):
            file_object.write(contents)

    return {"info": f"File {file.filename} saved at {file_location}"}