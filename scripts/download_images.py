import os
import urllib.request

image_dir = "data/images"
os.makedirs(image_dir, exist_ok=True)

image_urls = {
    "cat.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg",
    "dog.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg",
}


for filename, url in image_urls.items():
    filepath = os.path.join(image_dir, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filepath)
    else:
        print(f"{filename} already exists.")
