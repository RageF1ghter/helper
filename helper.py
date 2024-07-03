from huggingface_hub import hf_hub_download

model_repo = "CompVis/stable-diffusion-v-1-4-original"  # Replace with the correct model repo if different
model_filename = "sd-v1-4.ckpt"  # Replace with the correct model filename if different
local_path = "/home/zyc/stable-diffusion-webui/models/Stable-diffusion/sd-v1-4.ckpt"  # Path to save the model

# Download the model
hf_hub_download(repo_id=model_repo, filename=model_filename, local_dir=local_path)