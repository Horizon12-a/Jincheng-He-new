# 环境修复方案：最小修复 & 工程修复

## 基本信息
- 修复环境：Conda 虚拟环境 LX-mini
- 修复目标：解决 `requirements_broken.txt` 中的所有冲突问题

## 一、最小修复方案（改动最少）
1.  移除 `python==3.11`
2.  `torch==2.0.0` → `torch==2.0.0+cpu`
3.  `torchvision==0.16.0` → `torchvision==0.15.1+cpu`
4.  `cv2` → `opencv-python`
5.  `sklearn==0.0` → `scikit-learn==1.3.0`

## 二、修复验证
执行 `check_env.py` 验证修复成功，界面如下：
![修复成功校验截图](./env_success.png)
所有依赖导入正常，无报错。

## 三、工程级修复方案
使用 `environment_fixed.yml` 导出可复现的Conda环境，通过 `conda env create -f environment_fixed.yml` 一键创建，保证环境一致性。

## 四、关键避坑说明
1.  不要把 `python` 版本写进 `requirements.txt`。
2.  PyTorch 必须按硬件选择 `+cpu` 或 `+cu11x` 版本。
### 修复成功环境校验截图
![全依赖导入正常](./env_success.png)