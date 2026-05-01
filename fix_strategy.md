# 环境修复方案：最小修复 + 工程修复

## 基本信息
• 最小修复环境：LX-mini
• 工程修复环境：LX-project

---

# 一、最小修复
修改点 + 理由

1. **sklearn==0.0 → scikit-learn==1.3.0**
   理由：sklearn==0.0 是空包，无法使用。

2. **torchvision 0.10.0 → 0.17.0**
   理由：与 torch 2.2.0 严格匹配。

3. **numba 0.56.4 → 0.59.1**
   理由：支持 Python 3.11。

4. **删除 tensorflow==2.10.0**
   理由：不支持 Python 3.11，无法修复。

5. **torch==2.2.0 → torch==2.2.0+cpu**
   理由：指定 CPU 版本才能安装。

---

# 二、工程修复（适合 YOLO / PyTorch 训练）
## conda / pip 分工
• **conda**：python、numpy、pandas、matplotlib
  原因：底层二进制依赖稳定。

• **pip**：torch、torchvision、scikit-learn、numba、opencv
  原因：官方更新快、版本精准。

---

# 三、必答问题
## 1. 为什么不能用 sklearn==0.0？
它是假包，无代码，安装后无法导入，直接导致环境崩溃。

## 2. 为什么 torch / torchvision 必须匹配？
两者 API 强绑定，版本不匹配会无法运行、无法加载模型、训练中断。

## 3. GPU / CPU 选择逻辑
• CPU：使用 +cpu 后缀
• GPU：根据 nvidia-smi 选择 +cu118 / +cu121

---

# 四、避坑原则
1. 永远不要用 sklearn==0.0
2. torch 系列必须版本配对
3. 确认包支持当前 Python 版本
4. 基础库优先 conda，AI 框架优先 pip
5. 环境必须导出可复现文件

---

# 修复成功环境校验截图
![环境修复成功](./env_success.png)
