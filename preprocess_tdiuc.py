import json
import os
import shutil
import subprocess

# Paths
TDIUC_JSON = "../tdiuc/tdiuc_annotations.json"
COCO_IMAGE_DIR = "../coco/train2014/"
OUTPUT_DIR = "../processed_tdiuc/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load TDIUC data
with open(TDIUC_JSON, 'r') as f:
    tdiuc_data = json.load(f)

# Process first 100 entries (for demo)
for annotation in tdiuc_data["annotations"][:100]:
    image_id = annotation["image_id"]
    answer = annotation["answers"][0]["answer"]
    image_path = os.path.join(COCO_IMAGE_DIR, f"COCO_train2014_{str(image_id).zfill(12)}.jpg")
    if os.path.exists(image_path):
        try:
            # Copy image
            output_image = os.path.join(OUTPUT_DIR, f"{image_id}.jpg")
            shutil.copy(image_path, output_image)
            # Save answer as text
            with open(os.path.join(OUTPUT_DIR, f"{image_id}.txt"), "w") as f:
                f.write(answer)
            # Create a 5-second video (simulated)
            output_video = os.path.join(OUTPUT_DIR, f"{image_id}.mp4")
            subprocess.run([
                "ffmpeg", "-loop", "1", "-i", output_image, "-c:v", "libx264",
                "-t", "5", "-pix_fmt", "yuv420p", output_video, "-y"
            ], check=True)
            print(f"Processed {image_id}")
        except Exception as e:
            print(f"Error processing {image_id}: {e}")