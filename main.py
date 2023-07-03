from typing import Union
import test,utils
from fastapi import FastAPI, File, UploadFile
import shutil
import os
import uuid

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



path = [utils.path_images,utils.path_videos]
for i in path:
    os.makedirs(i, exist_ok=True)
    assert os.path.isdir(i)


@app.post('/upload_images')
def upload_image(file: UploadFile = File(...)):
    file_extension = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(path_images, filename)
    with open(file_path, "wb") as image:
        shutil.copyfileobj(file.file, image)
    print(file_path)
    return {'file_name': file.filename, 'path': f'http://localhost:8000/resources/photos/{filename}'}

    # file_path = f"images/{file.filename}"  # Specify the path where you want to save the image
    # with open(file_path, "wb") as image:
    #     shutil.copyfileobj(file.file, image)
    # return {"filename": file.filename}
