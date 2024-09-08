import os
import shutil

os.system(f"git clone https://git.homegu.com/comfyanonymous/ComfyUI")
os.system(f"git lfs install")
# os.system(f"git reset --hard")
os.system("pip install --upgrade transformers==4.44.2")
os.system("pip install --upgrade torch==2.1.2 torchvision==0.16.0")
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.system("pip install --upgrade huggingface_hub")


os.system(f"git clone https://git.homegu.com/ltdrdata/ComfyUI-Manager.git ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-Manager")
os.system(f"git clone https://git.homegu.com/ty0x2333/ComfyUI-Dev-Utils ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-Dev-Utils") # 显示节点运行时间
os.system(f"git clone https://git.homegu.com/Nuked88/ComfyUI-N-Sidebar ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-N-Sidebar")
os.system(f"git clone https://git.homegu.com/AIGODLIKE/AIGODLIKE-ComfyUI-Translation ComfyUI/home/xlab-app-center/custom_nodes/AIGODLIKE-ComfyUI-Translation")
os.system(f"git clone https://git.homegu.com/rgthree/rgthree-comfy ComfyUI/home/xlab-app-center/custom_nodes/rgthree-comfy")

os.system(f"git clone https://git.homegu.com/MinusZoneAI/ComfyUI-Kolors-MZ ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-Kolors-MZ") # 可图
os.system(f"git clone https://git.homegu.com/SeaArtLab/comfyui_storydiffusion ComfyUI/home/xlab-app-center/custom_nodes/comfyui_storydiffusion") # 可图
os.system(f"git clone https://git.homegu.com/yolain/ComfyUI-Easy-Use ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-Easy-Use")
os.system(f"git clone https://git.homegu.com/xinsir6/ControlNetPlus ComfyUI/home/xlab-app-center/custom_nodes/ControlNetPlus") # 全能xl调用
os.system(f"git clone https://git.homegu.com/kijai/ComfyUI-segment-anything-2 ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-segment-anything-2") # 第二代抠图
os.system(f"git clone https://git.homegu.com/kijai/ComfyUI-KJNodes ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-KJNodes")

os.system(f"git clone https://git.homegu.com/john-mnz/ComfyUI-Inspyrenet-Rembg ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-Inspyrenet-Rembg") # 抠背景
os.system(f"git clone https://git.homegu.com/Fannovel16/comfyui_controlnet_aux ComfyUI/home/xlab-app-center/custom_nodes/comfyui_controlnet_aux")
os.system(f"git clone https://git.homegu.com/ltdrdata/ComfyUI-Impact-Pack ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-Impact-Pack")
os.system(f"git clone https://git.homegu.com/ltdrdata/ComfyUI-Inspire-Pack ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-Inspire-Pack")
os.system(f"git clone https://git.homegu.com/ssitu/ComfyUI_UltimateSDUpscale ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI_UltimateSDUpscale")

os.system(f"git clone https://git.homegu.com/cubiq/ComfyUI_IPAdapter_plus ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI_IPAdapter_plus")
os.system(f"git clone https://git.homegu.com/Kosinkadink/ComfyUI-VideoHelperSuite ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-VideoHelperSuite")
os.system(f"git clone https://git.homegu.com/Nourepide/ComfyUI-Allor ComfyUI/home/xlab-app-center/custom_nodes/ComfyUI-Allor") # 硬件性能检测
os.system(f"git clone https://git.homegu.com/StartHua/Comfyui_CXH_joy_caption  ComfyUI/home/xlab-app-center/custom_nodes/Comfyui_CXH_joy_caption") # 支持多个视觉反推模型
os.system(f"git clone https://git.homegu.com/miaoshouai/ComfyUI-Miaoshouai-Tagger /home/xlab-app-center/custom_nodes/ComfyUI-Miaoshouai-Tagger") # 全新的视觉反推模型，显存更小

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://download.openxlab.org.cn/repos/file/mofashi/comfy/main?filepath=flux1-dev-fp8.safetensors&sign=071a1a24fac222d47b1ea471c6bd8f7f&nonce=1725718046851 -d ComfyUI/models/checkpoints -o flux1-dev-fp8.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors?download=true -d ComfyUI/models/checkpoints -o flux1-dev-fp8.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://civitai.com/api/download/models/782002 -d ComfyUI/models/checkpoints -o Jugg_Xl_by_RunDiffusion.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://download.openxlab.org.cn/models/ninjawick/realistic-vision-5.1/weight//Realistic_Vision_V6.0_NV_B1_inpainting.safetensors -d ComfyUI/models/checkpoints -o Realistic_Vision_V6.0_NV_B1_inpainting.safetensors")
# lora
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/ByteDance/Hyper-SD/resolve/main/Hyper-FLUX.1-dev-16steps-lora.safetensors?download=true -d ComfyUI/home/xlab-app-center/models/loras -o Hyper-FLUX.1-dev-16steps-lora.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/ByteDance/Hyper-SD/resolve/main/Hyper-FLUX.1-dev-8steps-lora.safetensors?download=true -d ComfyUI/home/xlab-app-center/models/loras -o Hyper-FLUX.1-dev-8steps-lora.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/Shakker-Labs/FLUX.1-dev-LoRA-blended-realistic-illustration/resolve/main/FLUX-dev-lora-blended_realistic_illustration.safetensors?download=true -d ComfyUI/home/xlab-app-center/models/loras -o A_写实插画结合_flux.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/Shakker-Labs/FLUX.1-dev-LoRA-add-details/resolve/main/FLUX-dev-lora-add_details.safetensors?download=true -d ComfyUI/home/xlab-app-center/models/loras -o FLUX-dev-lora-add_details增加细节.safetensors")
# controlnet
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro/resolve/main/diffusion_pytorch_model.safetensors?download=true -d ComfyUI/home/xlab-app-center/models/controlnet -o FLUX.1-dev-ControlNet-Union-Pro.safetensors")
# 反推模型
os.system("huggingface-cli download --resume-download google/siglip-so400m-patch14-384 --local-dir /home/xlab-app-center/models/clip/siglip-so400m-patch14-384")

os.system("ls /home/xlab-app-center/ComfyUI")
#os.system("ls /home/xlab-app-center/")
os.chdir(f"/home/xlab-app-center/ComfyUI")
os.system(f"python main.py --listen 0.0.0.0 --port 7860 --enable-cors-header")

