from flask import Flask, request, send_file, jsonify
from diffusers import StableDiffusionPipeline
import torch
import os
import shutil

app = Flask(__name__)
OUTPUT_DIR = "outputs/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Stable Diffusion
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")

@app.route("/generate_image", methods=["POST"])
def generate_image():
    try:
        prompt = request.json["prompt"]
        image = pipe(prompt).images[0]
        output_path = os.path.join(OUTPUT_DIR, "output.png")
        image.save(output_path)
        return send_file(output_path, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/generate_video", methods=["POST"])
def generate_video():
    try:
        prompt = request.json["prompt"]
        # Mock CogVideo (replace with real implementation)
        output_path = os.path.join(OUTPUT_DIR, "output.mp4")
        shutil.copy("../processed_tdiuc/309086.mp4", output_path)  # Placeholder
        return send_file(output_path, mimetype="video/mp4")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return send_file("static/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)