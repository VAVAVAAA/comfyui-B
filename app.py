import os
import shutil
import openxlab
from openxlab.dataset import download
import subprocess
import zipfile
import requests
# 环境
os.system("pip install --upgrade transformers==4.44.2")
os.system("pip install torch==2.4.1")
os.system("pip install --upgrade torchvision")
#os.system("pip install torchaudio==2.5")
os.system("pip install --upgrade packaging")
os.system("pip install impact.subpack_nodes")


os.system("pip install openxlab")
os.system("pip install -U openxlab")
openxlab.login(ak='xa5ag8yyvwpqkxw839pw', sk='l8njwnadbjgdwxe1zn83olme31xpparlo2q7vkmo')

os.chdir("/home/xlab-app-center")
os.system(f"git clone https://gitcode.com/gh_mirrors/co/ComfyUI")

os.system("pip install comfyui-frontend-package")

# 依赖
os.system("pip install aiohttp_sse")
os.system("pip install segment_anything")
os.system("pip install opencv-python")
os.system("pip install transparent_background")
os.system("pip install rembg")
os.system("pip install piexif")
os.system("pip install accelerate>=0.25.0")
os.system("pip install blend_modes")
os.system("pip install diffusers")
# os.system("pip install insightface")
os.system("pip install ftfy")
os.system("pip install openai")
os.system("pip install onnxruntime")
os.system("pip install sageattention")
os.system("pip install color-matcher")
os.system("pip install deepdiff")
os.system("pip install cpuinfo")




# 插件
os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Manager /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Manager")
os.system(f"git clone https://github.com/ty0x2333/ComfyUI-Dev-Utils /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Dev-Utils") # 显示节点运行时间
# os.system(f"git clone https://github.com/Nuked88/ComfyUI-N-Sidebar /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-N-Sidebar")
# os.system(f"git clone https://github.com/AIGODLIKE/AIGODLIKE-ComfyUI-Translation /home/xlab-app-center/ComfyUI/custom_nodes/AIGODLIKE-ComfyUI-Translation")
os.system(f"git clone https://github.com/rgthree/rgthree-comfy /home/xlab-app-center/ComfyUI/custom_nodes/rgthree-comfy")

os.system(f"git clone https://github.com/yolain/ComfyUI-Easy-Use /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Easy-Use")
# os.system(f"git clone https://github.com/VAVAVAAA/ComfyUI-Easy-Use-A /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Easy-Use-A") # 自己fork仓库的
# #os.system(f"git clone https://github.com/xinsir6/ControlNetPlus /home/xlab-app-center/ComfyUI/custom_nodes/ControlNetPlus") # 全能xl调用
# os.system(f"git clone https://github.com/kijai/ComfyUI-segment-anything-2 /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-segment-anything-2") # 第二代抠图
os.system(f"git clone https://github.com/kijai/ComfyUI-KJNodes /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-KJNodes")

# os.system(f"git clone https://github.com/john-mnz/ComfyUI-Inspyrenet-Rembg /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Inspyrenet-Rembg") # 抠背景
# os.system(f"git clone https://github.com/Fannovel16/comfyui_controlnet_aux /home/xlab-app-center/ComfyUI/custom_nodes/comfyui_controlnet_aux")
os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Impact-Pack /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Impact-Pack")
os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Impact-Subpack /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Impact-Subpack")
# os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Inspire-Pack /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Inspire-Pack")

# os.system(f"git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI_IPAdapter_plus")

os.system(f"git clone https://github.com/Nourepide/ComfyUI-Allor /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Allor") 
os.system(f"git clone https://github.com/crystian/ComfyUI-Crystools /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Crystools") # 硬件性能检测
# os.system(f"git clone https://github.com/StartHua/Comfyui_CXH_joy_caption  /home/xlab-app-center/ComfyUI/custom_nodes/Comfyui_CXH_joy_caption") # 支持多个视觉反推模型
# os.system(f"git clone https://github.com/miaoshouai/ComfyUI-Miaoshouai-Tagger /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Miaoshouai-Tagger") # 全新的视觉反推模型，显存更小

# os.system(f"git clone https://github.com/pythongosssss/ComfyUI-Custom-Scripts /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Custom-Scripts")
os.system(f"git clone https://github.com/melMass/comfy_mtb /home/xlab-app-center/ComfyUI/custom_nodes/comfy_mtb")
os.system(f"git clone https://github.com/chflame163/ComfyUI_LayerStyle /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI_LayerStyle")
os.system(f"git clone https://github.com/cubiq/ComfyUI_essentials /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI_essentials")
os.system(f"git clone https://github.com/chrisgoringe/cg-use-everywhere /home/xlab-app-center/ComfyUI/custom_nodes/cg-use-everywhere")
# os.system(f"git clone https://github.com/chrisgoringe/cg-image-picker /home/xlab-app-center/ComfyUI/custom_nodes/cg-image-picker")
os.system(f"git clone https://github.com/ssitu/ComfyUI_UltimateSDUpscale /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI_UltimateSDUpscale --recursive")

# os.system(f"git clone https://github.com/M1kep/ComfyLiterals /home/xlab-app-center/ComfyUI/custom_nodes/ComfyLiterals") # 字符串节点
# os.system(f"git clone https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Inpaint-CropAndStitch") # 重绘
# os.system(f"git clone https://github.com/WASasquatch/was-node-suite-comfyui /home/xlab-app-center/ComfyUI/custom_nodes/was-node-suite-comfyui") 
os.system(f"git clone https://github.com/Fannovel16/ComfyUI-Frame-Interpolation /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Frame-Interpolation") # 视频补帧

os.system(f"git clone https://github.com/smthemex/ComfyUI_DiffuEraser /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI_DiffuEraser") #视频去水印
os.system(f"git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-VideoHelperSuite")
os.system(f"git clone https://github.com/chflame163/ComfyUI_LayerStyle_Advance /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI_LayerStyle_Advance")
os.system(f"git clone https://github.com/ShmuelRonen/ComfyUI-VideoUpscale_WithModel /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-VideoUpscale_WithModel")
os.system(f"git clone https://github.com/kijai/ComfyUI-WanVideoWrapper /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-WanVideoWrapper") # wan2.1视频插件



# 大模型
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/ComfyUI/models/checkpoints/{file_name}') 
 for file_name in [
     #'MYHuman-墨幽人造人15.safetensors'
 ]]

# ai去水印，lama
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/ComfyUI/models/lama/{file_name}') 
 for file_name in [
     'big-lama.pt'
 ]]

# unet模型
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/ComfyUI/models/unet/{file_name}') 
#  for file_name in [
#      'ketu_fp16.safetensors', 
#      'CogVideoX_5b_fun_GGUF_Q4_0.safetensors',
     
#  ]]
# # lora
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/ComfyUI/models/loras/{file_name}') 
#  for file_name in [
#     'pcm_sd15_smallcfg_2step_converted.safetensors'
#  ]]
# # vae
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/ComfyUI/models/vae/{file_name}') 
 for file_name in [
     'flux_vae.safetensors'
 ]]
# clip模型
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/ComfyUI/models/clip/{file_name}') 
 for file_name in [
     #'ViT-L-14-TEXT-detail-improved-hiT-GmP-TE-only-HF.safetensors', 
     'clip_l.safetensors',
     't5xxl_fp8_e4m3fn.safetensors'
 ]]
# # 视觉识别模型&大语言模型
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/ComfyUI/models/LLM/{file_name}') 
#  for file_name in [
# #     'Florence-2-large-PromptGen.safetensors'
#  ]]


# 放大模型
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/ComfyUI/models/upscale_models/{file_name}') 
 for file_name in [
     '4xNomos8kSCHAT-L.pth', 
     'RealESRGAN_x4plus.pth',
     '4x_NMKD-Siax_200k.pth'
 ]]

# # SAM检测加载器
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/ComfyUI/models/sams/{file_name}') 
#  for file_name in [
#      'sam_vit_b_01ec64.pth'
#  ]]

# # SAM2检测加载器
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/ComfyUI/models/sam2/{file_name}') 
#  for file_name in [
#      'sam2_hiera_base_plus.safetensors'
#  ]]

# # bbox检测面部模型
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/ComfyUI/models/ultralytics/bbox/{file_name}') 
#  for file_name in [
#      'face_yolov8m.pt'
#  ]]
# # controlnet
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/ComfyUI/models/controlnet/{file_name}') 
#  for file_name in [
#      'diffusion_pytorch_model.safetensors'
#  ]]

# # 数据集2-controlnet
# [download(dataset_repo='mofashi/comfy2', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/ComfyUI/models/controlnet/{file_name}') 
#  for file_name in [
#      'FLUX-dev-Controlnet-Inpainting-Alpha.safetensors'
#  ]]
# # 数据集2- lora
# [download(dataset_repo='mofashi/comfy2', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/ComfyUI/models/loras/{file_name}') 
#  for file_name in [
#      'Flux-小红书真实写真.safetensors',
#      '山水诗行_flux版',
#      '极氪白白酱Flux-人像V6MAX'
#  ]]

# # id换脸模型
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/ComfyUI/models/instantid/{file_name}') 
#  for file_name in [
#      'ip-adapter.bin'
#  ]]

# # 设置下载链接和目标 ZIP 文件的路径
# url = 'https://cdn-xlab-data.openxlab.org.cn/objects/8e182f14fc6e80b3bfa375b33eb6cff7ee05d8ef7633e738d1c89021dcf0c5c5?Expires=1727759738&OSSAccessKeyId=LTAI5tSqABbitQcgeNNd8dAE&Signature=xfpmiZOgkgb%2FgTU%2Bm%2FxV8Hpkad4%3D&response-content-disposition=attachment%3B%20filename%3D%22antelopev2.zip%22&response-content-type=application%2Foctet-stream'  # 替换为你的 ZIP 文件下载链接
# zip_file_path = 'antelopev2.zip'     # 下载后保存的 ZIP 文件名
# extract_to_path = '/home/xlab-app-center/ComfyUI/models/insightface/models/antelopev2'       # 解压后保存的目录

# # 下载 ZIP 文件
# response = requests.get(url)
# with open(zip_file_path, 'wb') as zip_file:
#     zip_file.write(response.content)

# print(f'ZIP 文件已下载到: {zip_file_path}')

# # 检查目标解压路径是否存在，如果不存在则创建
# if not os.path.exists(extract_to_path):
#     os.makedirs(extract_to_path)

# # 解压 ZIP 文件
# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     zip_ref.extractall(extract_to_path)

# print(f'解压完成，文件已解压到：{extract_to_path}')

# 大模型
#os.chdir(f"/home/xlab-app-center/ComfyUI/models/checkpoints") #模型仓库，大模型文件夹
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/MYHuman-%E5%A2%A8%E5%B9%BD%E4%BA%BA%E9%80%A0%E4%BA%BAXL_v2010-Flux-RF.safetensors?ref=main&nonce=1726399393393 -o MYHuman-墨幽人造人XL-v2010-Flux-RF.safetensors",shell=True)

#os.chdir(f"/home/xlab-app-center/ComfyUI/models/unet") # 模型仓库，unet文件夹
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/flux1-dev-fp8原始.safetensors?ref=main&nonce=1725931610381 -o flux1-dev-fp8原始.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('flux1-dev-fp8原始下载完成')
# subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/MYHuman-Flux%E5%8E%9F%E9%9A%8F%E6%8B%8D-fp16-1.1.safetensors?ref=main&nonce=1726185742539 -o MYHuman-Flux原随拍-fp16-1.1.safetensors",shell=True)
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/MYHuman-F.1-%E5%8E%9F%E5%A2%A8%E5%B9%BD%E9%9A%8F%E6%8B%8D-v1-%E9%9A%8F%E6%8B%8D.safetensors?ref=main&nonce=1726204698330 -o MYHuman-F.1-原墨幽随拍-v1-随拍.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('原墨幽随拍-v1-随拍下载完成')
# subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/CogVideoX_5b_fp8_4em.safetensors?ref=main&nonce=1726813815633 -o CogVideoX_5b_fp8_4em.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('CogVideoX_5b_fp8_4em下载完成')


#os.chdir(f"/home/xlab-app-center/ComfyUI/models/loras") #模型仓库，lora文件夹
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/%E7%AD%91%E6%A2%A6F.1_INS%E6%BB%A4%E9%95%9C_v1.0.safetensors?ref=main&nonce=1726186206302 -o 筑梦F.1_INS滤镜_v1.0.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('筑梦F.1_INS滤镜下载完成')

#os.makedirs("/home/xlab-app-center/ComfyUI/models/LLM", exist_ok=True) # 目录不存在则自动创建
#os.chdir(f"/home/xlab-app-center/ComfyUI/models/LLM") # 模型仓库，LLM文件夹
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/chatglm3-8bit.safetensors?ref=main&nonce=1725936486503 -o chatglm3-8bit.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('chatglm3-8bit下载完成')
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/Florence-2-large-PromptGen-v1.5.safetensors?ref=main&nonce=1727138430530 -o Florence-2-large-PromptGen-v1.5.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('Florence-2-large-PromptGen-v1.5下载完成')

os.makedirs("/home/xlab-app-center/ComfyUI/models/diffusion_models", exist_ok=True) # 目录不存在则自动创建
os.chdir(f"/home/xlab-app-center/ComfyUI/models/diffusion_models") # 模型仓库，LLM文件夹
subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/flux1-dev-kontext_fp8_scaled.safetensors?ref=main&nonce=1750995578624 -o flux1-dev-kontext_fp8_scaled.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('flux1-dev-kontext_fp8_scaled下载完成')
subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://modelscope.cn/models/AI-ModelScope/Wan14BT2VFusioniX/resolve/master/Wan14Bi2vFusioniX.safetensors -o Wan2.1_14B_i2v_fp8_FusioniX.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('Wan14Bi2vFusioniX下载完成')
subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://modelscope.cn/models/QuantStack/Wan2.1-14B-T2V-FusionX-VACE/resolve/master/Wan2.1_T2V_14B_FusionX_VACE-FP8_e4m3fn.safetensors -o Wan2.1_T2V_14B_FusionX_VACE-FP8_e4m3fn.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('Wan2.1_T2V_14B_FusionX_VACE-FP8_e4m3fn下载完成')


os.makedirs("/home/xlab-app-center/ComfyUI/models/text_encoders", exist_ok=True) # 目录不存在则自动创建
os.chdir(f"/home/xlab-app-center/ComfyUI/models/text_encoders") # 模型仓库，LLM文件夹
subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/master/split_files/text_encoders/umt5_xxl_fp16.safetensors -o umt5_xxl_fp16.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('umt5_xxl_fp16下载完成')


os.chdir(f"/home/xlab-app-center/ComfyUI/models/vae") # 模型仓库，LLM文件夹
subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/master/split_files/vae/wan_2.1_vae.safetensors -o wan_2.1_vae.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('wan_2.1_vae下载完成')



os.system("ls -al /home/xlab-app-center/ComfyUI")          
os.chdir(f"/home/xlab-app-center/ComfyUI")# 启动文件（勿动！）
os.system(f"python main.py --listen 0.0.0.0 --port 7860 --enable-cors-header")
#os.system(f"python main.py --cpu --listen 0.0.0.0 --port 7860 --enable-cors-header")
