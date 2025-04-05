from diffusers import StableDiffusionPipeline
import torch
import os

# Paths
OUTPUT_DIR = "../outputs/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load model
model_id = "runwayml/stable-diffusion-v1-5"
try:
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Generate image
prompt = "A photo of a cat on a couch"
try:
    image = pipe(prompt).images[0]
    output_path = os.path.join(OUTPUT_DIR, "generated_image.png")
    image.save(output_path)
    print(f"Image saved to {output_path}")
except Exception as e:
    print(f"Error generating image: {e}")