import os
os.system("pip install py7zr")

import py7zr
os.chdir(f"/home/xlab-app-center")
ui = "/home/xlab-app-center"
ui_path = os.path.join(ui, "ComfyUI")
os.makedirs(ui_path, exist_ok=True)
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://github.com/comfyanonymous/ComfyUI/releases/download/v0.1.3/ComfyUI_windows_portable_nvidia.7z -o comfyUI.7z")
# 解压文件
with py7zr.SevenZipFile(archive_path, mode='r') as z:  # 使用 py7zr 打开下载的 7z 文件
    z.extractall(path=ui_path)  # 解压所有文件到目标目录 ui_path 中
# 删除下载的7z文件
os.remove(archive_path)  # 删除下载的 7z 文件，以节省磁盘空间
os.chdir(f"/home/xlab-app-center/ComfyUI")
os.system(f"git lfs install")
os.system(f"git reset --hard")
os.system(f"python main.py --dont-print-server --preview-method auto --enable-cors-header --use-pytorch-cross-attention")
