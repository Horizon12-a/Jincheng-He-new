# 依赖冲突分析报告
环境信息
操作系统：Windows 11
Python 版本：3.11
环境：conda 独立环境 LX-mini
GPU：CPU only

## 问题1：sklearn==0.0 是无效空包（包名/版本陷阱）
表现：安装直接冲突、无法解析。
根因：sklearn==0.0 是 PyPI 占位假包，无实际代码，必须使用 scikit-learn。
类型：包名错误 + 无效版本。

## 问题2：torch 与 torchvision 版本完全不匹配（强依赖冲突）
表现：安装后无法运行，导入报错。
根因：torch==2.2.0 必须搭配 torchvision==0.17.0，但文件写的是 torchvision==0.10.0，版本极度不匹配。
类型：包间强依赖冲突。

## 问题3：numba==0.56.4 不支持 Python 3.11（Python 版本冲突）
表现：安装失败或无法运行。
根因：numba 0.56.4 最高只支持 Python 3.10，而当前环境是 3.11。
类型：Python 版本不兼容。

## 问题4：tensorflow==2.10.0 与 Python 3.11 不兼容（版本冲突）
表现：安装失败。
根因：tensorflow 2.10 不支持 Python 3.11。
类型：Python 版本与包不兼容。

## conda 与 pip 解析差异
conda：管理二进制依赖、C 扩展、系统库，解析更严格。
pip：仅管理 Python 层级依赖，不关心底层编译兼容性。
混用会导致底层库被覆盖，引发运行时崩溃。

### 安装失败现场截图
![依赖安装失败截图](./imgs/env_fail.png)
