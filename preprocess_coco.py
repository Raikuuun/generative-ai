import json
import os
from PIL import Image

# Paths
COCO_ANNOTATIONS = "../coco/annotations/captions_train2014.json"
COCO_IMAGE_DIR = "../coco/train2014/"
OUTPUT_DIR = "../processed_coco/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load annotations
with open(COCO_ANNOTATIONS, 'r') as f:
    data = json.load(f)

# Process first 1000 captions (for demo; adjust as needed)
for annotation in data["annotations"][:1000]:
    image_id = annotation["image_id"]
    caption = annotation["caption"]
    image_path = os.path.join(COCO_IMAGE_DIR, f"COCO_train2014_{str(image_id).zfill(12)}.jpg")
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            output_image_path = os.path.join(OUTPUT_DIR, f"{image_id}.jpg")
            img.save(output_image_path)
            with open(os.path.join(OUTPUT_DIR, f"{image_id}.txt"), "w") as f:
                f.write(caption)
            print(f"Processed image {image_id}")
        except Exception as e:
            print(f"Error processing {image_id}: {e}")
    else:
        print(f"Image not found: {image_path}")