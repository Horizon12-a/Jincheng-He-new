# 依赖冲突分析报告

环境信息
操作系统：Windows 11 64位
Python 版本：3.11
使用隔离环境：Conda 虚拟环境 LX-mini
环境创建方式：conda create 命令
未使用：Python venv 虚拟环境、系统全局 Python 环境
GPU：无，CPU 单机运行

安装失败复现
执行题目提供的破损依赖文件 requirements_broken.txt：

pip install -r requirements_broken.txt

错误日志已完整记录在 logs/install_failed.log 中。

## 主要冲突问题分析

### Python 版本冲突问题
问题：requirements.txt 内写入 python==3.11
pip 仅用于安装第三方库，**无法安装 Python 解释器本体**，conda 与 pip 解析规则不互通。
影响：安装指令直接报错终止，整个依赖流程无法继续执行。

### 错误包名问题
问题：使用 cv2、sklearn 作为 pip 安装包名
cv2 是代码导入名，真实安装包为 opencv-python；sklearn 无 0.0 有效版本，真实包名为 scikit-learn。
conda 优先识别标准库名，pip 严格识别 PyPI 官方包名，二者包名不统一极易报错。
影响：pip 检索不到对应安装包，依赖下载直接失败。

### PyTorch 硬件版本不匹配问题
问题：torch==2.0.0 未添加 +cpu 后缀
裸版本 Torch 默认适配显卡 CUDA 环境，CPU 电脑无法匹配对应安装包。
影响：PyPI 源无法找到对应资源，torch 与 torchvision 双双安装失败。

### 包之间版本依赖不兼容问题
问题：torch==2.0.0 配套 torchvision 应为 0.15.x，文件内错误填写 0.16.0
conda 会自动校验上下游依赖适配，pip 不会主动校验版本关联关系。
影响：即便强行安装成功，运行时接口不兼容，脚本导入直接报错崩溃。

### Conda 与 Pip 解析机制差异
1. Conda 跨语言管理环境，自带依赖关联校验，会自动适配 Python、torch、附属库版本
2. Pip 仅管理 Python 第三方包，不校验 Python 本体版本，不自动匹配上下游依赖
3. 二者源不互通、版本规则不一致，混用极易出现隐性冲突

### 安装失败现场截图
![依赖安装失败复现](./env_fail.png)
