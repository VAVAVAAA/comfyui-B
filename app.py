import os
os.chdir(f"/home/xlab-app-center")
ui = "/home/xlab-app-center"
ui_path = os.path.join(ui, "ComfyUI")
os.makedirs(ui_path, exist_ok=True)
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://hf-mirror.com/datasets/Carmeninkunming/fast-repo-kaggle/resolve/main/cui-2024-8.tar.lz4?download=true -o cui.tar.lz4 && tar -xI lz4 -f cui.tar.lz4 --directory={ui_path} && rm {ui}/cui.tar.lz4")
os.chdir(f"/home/xlab-app-center/ComfyUI")
os.system(f"git lfs install")
os.system(f"git reset --hard")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://hf-mirror.com/LyliaEngine/Pony_Diffusion_V6_XL/resolve/main/ponyDiffusionV6XL_v6StartWithThisOne.safetensors -d /home/xlab-app-center/ComfyUI/models/checkpoints/ -o ponyDiffusionV6XL_v6StartWithThisOne.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://hf-mirror.com/LyliaEngine/Pony_Diffusion_V6_XL/resolve/main/sdxl_vae.safetensors -d /home/xlab-app-center/ComfyUI/models/vae/ -o sdxl_vae.safetensors")
os.system(f"python main.py --dont-print-server --preview-method auto --enable-cors-header --use-pytorch-cross-attention")
