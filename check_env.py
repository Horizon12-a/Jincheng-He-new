import sys
import os
import torch
import torchvision
import numpy
import pandas
import cv2
import matplotlib

print("===== 环境检查报告 =====")
print(f"Python 版本: {sys.version}")
print(f"Conda 环境名: {os.environ.get('CONDA_DEFAULT_ENV', '非 conda 环境')}")
print(f"PyTorch 版本: {torch.__version__}")
print(f"Torchvision 版本: {torchvision.__version__}")
print(f"CUDA 可用: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"GPU 名称: {torch.cuda.get_device_name(0)}")
else:
    print("GPU 名称: CPU only")

print("\n===== 依赖导入成功 =====")
print(f"numpy 版本: {numpy.__version__}")
print(f"pandas 版本: {pandas.__version__}")
print(f"opencv-python 版本: {cv2.__version__}")
print(f"matplotlib 版本: {matplotlib.__version__}")

import sklearn
print(f"scikit-learn 版本: {sklearn.__version__}")