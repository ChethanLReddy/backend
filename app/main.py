from typing import Union
from .database import get_db,engine
from .utils import paths
from fastapi import FastAPI, File, UploadFile,status, Depends,Body
from sqlalchemy.orm import Session
import shutil
import os
import uuid
from . import models,schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



path = [paths.path_images,paths.path_videos]
for i in path:
    os.makedirs(i, exist_ok=True)
    assert os.path.isdir(i)


@app.post('/upload_images',status_code=status.HTTP_200_OK)
def upload_image(data: schemas.upload_image = Depends(), file: UploadFile = File(...),db : Session = (Depends(get_db))):
    print(data)
    file_extension = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(paths.path_images, filename)
    with open(file_path, "wb") as image:
        shutil.copyfileobj(file.file, image)
    print(file_path)
    data.iamge_path = file_path
    
    data_create = models.images(id = 1,**data.dict())
    db.add(data_create)
    db.commit()
    db.refresh(data_create)
    return data_create

    # file_path = f"images/{file.filename}"  # Specify the path where you want to save the image
    # with open(file_path, "wb") as image:
    #     shutil.copyfileobj(file.file, image)
    # return {"filename": file.filename}
    # ,


@app.post('/test_schema',status_code=status.HTTP_200_OK)
def test_schema(payload : schemas.upload_image):
    print(payload)
    return payload



