import os
from utils import paths

path = paths.path_images

for files in os.listdir(path):
    if files.endswith('.png'):
        print(files)