from openvino.runtime import Core
from transformers import CLIPProcessor
from PIL import Image
import numpy as np

class CLIPEmbeddingExtractor:
    def __init__(self,
                 image_model_path="clip_ov/image_encoder/openvino_model.xml",
                 text_model_path="clip_ov/text_encoder/openvino_model.xml"):
        self.core = Core()
        self.image_model = self.core.compile_model(image_model_path, "CPU")
        self.text_model = self.core.compile_model(text_model_path, "CPU")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.image_input = self.image_model.input(0)
        self.text_input = self.text_model.input(0)

    def extract_image_embedding(self, image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="np")
        pixel_values = inputs["pixel_values"]
        outputs = self.image_model({self.image_input.any_name: pixel_values})
        return list(outputs.values())[0].squeeze()

    def extract_text_embedding(self, text):
        inputs = self.processor(text=[text], return_tensors="np")
        input_ids = inputs["input_ids"]
        outputs = self.text_model({self.text_input.any_name: input_ids})
        return list(outputs.values())[0].squeeze()
