import os
os.chdir(f"/home/xlab-app-center")
ui = "/home/xlab-app-center"
ui_path = os.path.join(ui, "ComfyUI")
os.makedirs(ui_path, exist_ok=True)
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/datasets/Carmeninkunming/fast-repo-kaggle/resolve/main/cui-openxlab.tar.lz4 -o cui.tar.lz4 && tar -xI lz4 -f cui.tar.lz4 --directory={ui_path} && rm {ui}/cui.tar.lz4")
os.chdir(f"/home/xlab-app-center/ComfyUI")
os.system(f"git lfs install")
os.system(f"git reset --hard")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/cyber-realistic/weight//cyberrealistic_v32.safetensors -d /home/xlab-app-center/ComfyUI/models/checkpoints/ -o cyberrealistic_v32.safetensors")
os.system(f"python main.py --dont-print-server --preview-method auto --enable-cors-header --use-pytorch-cross-attention")
##test                                  
