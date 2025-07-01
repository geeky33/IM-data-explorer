from src.core.embeddings.extractor import CLIPEmbeddingExtractor
from src.core.embeddings.storage import EmbeddingStorage
import os

extractor = CLIPEmbeddingExtractor()
storage = EmbeddingStorage("embeddings.h5")

# Extract and save embeddings from image folder
image_dir = "data/images"
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        path = os.path.join(image_dir, filename)
        emb = extractor.extract_image_embedding(path)
        storage.save_embedding("image", filename, emb)

# Also try a few text prompts
texts = ["a cat sitting on the floor", "a golden retriever playing"]
for txt in texts:
    emb = extractor.extract_text_embedding(txt)
    storage.save_embedding("text", txt, emb)
