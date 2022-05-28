#search through all directories and subdirectories for webp files and convert them to jpg
from PIL import Image
import os

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.webp'):
            im = Image.open(os.path.join(dirpath, filename)).convert('RGB')
            im.save(os.path.join(dirpath, filename[:-5] + '.jpg'))

#delete all webp files
for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.webp'):
            os.remove(os.path.join(dirpath, filename))