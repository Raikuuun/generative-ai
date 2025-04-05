import json
import os
from PIL import Image

# Load annotations
with open('./data/coco/annotations/captions_train2014.json', 'r') as f:
    coco_data = json.load(f)

# Extract image-caption pairs
captions = [(ann['image_id'], ann['caption']) for ann in coco_data['annotations']]
with open('coco_captions.txt', 'w') as f:
    for img_id, caption in captions:
        f.write(f"{img_id:012d}\t{caption}\n")
"Annotation: Saves image IDs (padded to 12 digits) and captions to a text file."
image_dir = './data/coco/train2014/'
output_dir = './data/coco/train2014_resized/'
os.makedirs(output_dir, exist_ok=True)

for img_id, _ in captions:
    img_path = os.path.join(image_dir, f"{img_id:012d}.jpg")
    if os.path.exists(img_path):
        img = Image.open(img_path).resize((256, 256))
        img.save(os.path.join(output_dir, f"{img_id:012d}.jpg"))
"Annotation: Resizes all training images to 256x256 for Stable Diffusion."