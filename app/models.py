import string
from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship


class images(Base):
    __tablename__ = 'image_store'
    id = Column(Integer, primary_key=True, nullable=False)
    image_name = Column(String,nullable=False)
    iamge_path = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    


print('created')