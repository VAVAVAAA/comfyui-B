import os
import shutil
#os.chdir(f"/home/xlab-app-center")
os.system(f"git clone https://github.com/comfyanonymous/ComfyUI")
os.system(f"git lfs install")
# os.system(f"git reset --hard")
os.system("pip install --upgrade transformers==4.44.2")
os.system("pip install --upgrade torch==2.1.0 torchvision==0.16.0")
# os.system("git pull https://github.com/comfyanonymous/ComfyUI.git main")

os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Manager ComfyUI/custom_nodes/ComfyUI-Manager")
os.system(f"git clone https://github.com/ty0x2333/ComfyUI-Dev-Utils ComfyUI/custom_nodes/ComfyUI-Dev-Utils")
os.system(f"git clone https://github.com/Nuked88/ComfyUI-N-Sidebar ComfyUI/custom_nodes/ComfyUI-N-Sidebar")
os.system(f"git clone https://github.com/AIGODLIKE/AIGODLIKE-ComfyUI-Translation ComfyUI/custom_nodes/AIGODLIKE-ComfyUI-Translation")

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors?download=true -d ComfyUI/models/checkpoints -o flux1-dev-fp8.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://civitai.com/api/download/models/782002 -d ComfyUI/models/checkpoints -o Jugg_Xl_by_RunDiffusion.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://download.openxlab.org.cn/models/ninjawick/realistic-vision-5.1/weight//Realistic_Vision_V6.0_NV_B1_inpainting.safetensors -d ComfyUI/models/checkpoints -o Realistic_Vision_V6.0_NV_B1_inpainting.safetensors")

os.system(f"python ComfyUI/main.py --listen 0.0.0.0 --port 7860 --enable-cors-header")

