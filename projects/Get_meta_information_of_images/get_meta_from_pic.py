from PIL import Image
from PIL.ExifTags import TAGS
from author_utils import get_file_security, get_author
from gps_utils import get_location
import os
import sys
from datetime import datetime

def get_exif(image):
    image.verify()
    return image._getexif()


def get_labeled_exif(exif):
    return {TAGS.get(key): val for key, val in exif.items()}

im = Image.open(sys.argv[1])

# get the image name
name = im.filename

# get the image size
w, h = im.size

# get the image file extension
_, file_extension = os.path.splitext(sys.argv[1])

# get the exif information
exif = get_exif(im)
labeled = get_labeled_exif(exif)

# get the file creation time
ctime = os.path.getctime(sys.argv[1])

# output information
print(f"ImageName: {name}")
print(f"size: {w}x{h}")
print(f"FileExtension: {file_extension}")
if ('ExifImageWidth' in labeled.keys()):
    print(f"ImageWidth: {labeled['ExifImageWidth']}")
else:
    print("No ImageWidth")

if ('ExifImageHeight' in labeled.keys()):
    print(f"ImageHeight: {labeled['ExifImageHeight']}")
else:
    print("No ImageHeight")

if ('DateTimeOriginal' in labeled.keys()):
    print(f"DateTimeOriginal: {labeled['DateTimeOriginal']}")
else:
    print("No DateTimeOriginal")

print(
    f"CreateDate: {datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')}"
)
print(f"Author: {get_author(sys.argv[1])}")
print(f"Location: {get_location(sys.argv[1])}")
