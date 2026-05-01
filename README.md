# 📘 Conda 环境排障作业 
本仓库包含环境故障复现、依赖修复、日志与截图，可完整复现作业全过程。

---

## 任务 1：复现依赖安装失败
1. 激活隔离环境
conda activate LX-mini

2. 进入项目目录
cd C:\Users\33684\Desktop\Horizon12-a

3. 执行破损依赖安装（复现失败）
pip install -r requirements_broken.txt

失败截图：![](./imgs/env_fail.png) -
完整失败日志：logs/install_failed.log

---

## 任务 3：环境修复与验证
1. 安装修复后的依赖
pip install -r requirements_fixed.txt

2. 运行环境校验脚本
python check_env.py

成功截图：![](./imgs/env_success.png) -
校验结果：所有依赖导入正常，版本匹配

---

## 任务 4：环境一键重建（可选）
- conda env create -f environment_fixed.yml
- conda activate LX-mini

---

## 提交文件清单
- check_env.py - 环境检查脚本
- requirements_broken.txt - 原始故障依赖文件
- requirements_fixed.txt - 修复后的依赖文件
- environment_fixed.yml - 可复现的 Conda 环境配置
- logs/install_failed.log - 安装失败日志
- conflict_analysis.md - 依赖冲突分析报告
- fix_strategy.md - 修复方案说明
- README.md - 本文件

---

## 备注
本作业全程使用 conda 虚拟环境 LX-mini，未使用系统全局 Python 或 venv -
所有截图与日志均为真实运行记录，可按上述步骤完整复现
