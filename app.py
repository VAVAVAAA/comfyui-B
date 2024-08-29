import os


# 定义根目录路径
root_dir = "/home/xlab-app-center"
os.chdir(root_dir)

# 定义 ComfyUI 的安装路径
ui_path = os.path.join(root_dir, "ComfyUI")
os.makedirs(ui_path, exist_ok=True)  # 如果路径不存在，则创建

# 使用 git clone 下载 ComfyUI 仓库到 ui_path
os.system(f"git clone https://github.com/comfyanonymous/ComfyUI.git {ui_path}")

# 解压缩函数，由于不再使用 7z 文件下载，这部分代码可以省略
# archive_path = os.path.join(root_dir, "comfyUI.7z")
# with py7zr.SevenZipFile(archive_path, mode='r') as z:  # 使用 py7zr 打开下载的 7z 文件
#     z.extractall(path=ui_path)  # 解压所有文件到目标目录 ui_path 中
# os.remove(archive_path)  # 删除下载的 7z 文件，以节省磁盘空间

# 切换到 ComfyUI 目录
os.chdir(ui_path)

# 安装 Git LFS（大文件存储）并重置 Git 仓库状态
os.system("git lfs install")
os.system("git reset --hard")

# 运行 ComfyUI 主程序
os.system("python main.py --dont-print-server --preview-method auto --enable-cors-header --use-pytorch-cross-attention")

