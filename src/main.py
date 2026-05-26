import torch 
from transformers import pipeline
from transformers import CLIPModel, CLIPProcessor
from diffusers import StableDiffusionInpaintPipeline, AutoPipelineForInpainting
from PIL import image
import numpy as np



#Using Pytorch CUDA compatibility 
device = torch.device ("cuda" if torch.cuda.is_available() else "cpu")
print (f"Using device: {device}")

dtype = torch.float16 if device == "cuda" else torch.float32

class CLIPDeepDream:
    def __init__(self):
        
    def load_sd_model():
        """
        Load and configure the Stable Diffusion pipeline with model quantization
        """
        model_id = "runwayml/stable-diffusion-inpainting"
        
        pipeline = AutoPipelineForInpainting.from_pretrained(
            model_id,
            torch_dtype=torch.float16
        )
        pipeline.to(device)
        return pipeline