from pydantic import BaseModel
from fastapi import UploadFile,File
from typing import Optional

class upload_image(BaseModel):
    image_name : str
    iamge_path : Optional[str] = None