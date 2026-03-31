# CV Assignment 1 — 混合图像 / Hybrid Images

本仓库为计算机视觉作业 1 的实现代码，包含：

- **图像滤波**（`my_imfilter`）：使用镜像填充的卷积实现
- **混合图像生成**（`create_hybrid_image`）：低通 + 高通合成

---

## 目录 / Table of Contents

1. [项目结构](#项目结构)
2. [环境准备](#环境准备)
3. [最小运行命令](#最小运行命令)
4. [在 VS Code 中运行](#在-vs-code-中运行)
5. [常见报错排查](#常见报错排查)

---

## 项目结构

```
CV_Assignment1/
├── Assignment 1 code/
│   └── Assignment-1/
│       ├── code/
│       │   ├── proj1.ipynb              ← 主实验 Notebook（入口）
│       │   ├── proj1_test_filtering.ipynb ← 滤波测试 Notebook
│       │   ├── student_code.py          ← 你需要完成/修改的代码
│       │   ├── utils.py                 ← 工具函数（读写图像等）
│       │   └── __init__.py
│       ├── data/                        ← 输入图像（.bmp）
│       └── results/                     ← 输出结果图像
├── requirements.txt                     ← Python 依赖
├── .vscode/
│   ├── settings.json                    ← VS Code 配置
│   └── launch.json                      ← 调试配置
└── Assignment 1 .pdf                    ← 作业说明 PDF
```

---

## 环境准备

### 依赖

- Python 3.8 或以上（推荐 3.10+）
- 依赖包：`numpy`、`opencv-python`、`matplotlib`、`jupyter`、`ipykernel`

### 安装步骤

#### Windows / macOS / Linux 通用流程

```bash
# 1. 克隆仓库（如果还没有克隆）
git clone https://github.com/baixuezhixia/CV_Assignment1.git
cd CV_Assignment1

# 2. 创建并激活虚拟环境（推荐，避免与系统包冲突）
python -m venv .venv

# Windows（PowerShell）激活：
.venv\Scripts\Activate.ps1

# macOS / Linux 激活：
source .venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt
```

> **Windows 注意**：如果 `python` 找不到，请尝试 `python3` 或从
> [python.org](https://www.python.org/downloads/) 下载安装 Python，
> 并在安装时勾选 **"Add Python to PATH"**。

---

## 最小运行命令

激活虚拟环境后，在仓库根目录启动 Jupyter：

```bash
jupyter notebook "Assignment 1 code/Assignment-1/code/proj1.ipynb"
```

或使用 Jupyter Lab：

```bash
jupyter lab
```

然后导航到 `Assignment 1 code/Assignment-1/code/proj1.ipynb`，
依次点击每个 cell 旁边的 **▶ 运行** 按钮，或使用菜单
**Kernel → Restart & Run All**。

---

## 在 VS Code 中运行

### 前提：安装必要扩展

在 VS Code 扩展面板（`Ctrl+Shift+X`）搜索并安装：

| 扩展名 | 说明 |
|--------|------|
| **Python**（Microsoft） | Python 语言支持 |
| **Jupyter**（Microsoft） | Notebook 支持 |

### 步骤 1：选择 Python 解释器

1. 打开命令面板：`Ctrl+Shift+P`（macOS: `Cmd+Shift+P`）
2. 输入并选择：`Python: Select Interpreter`
3. 选择 `.venv` 里的 Python：
   - **macOS / Linux**：路径类似 `./.venv/bin/python`
   - **Windows**：路径类似 `.\.venv\Scripts\python.exe`
   - 如果列表中没有，点 **"Enter interpreter path…"** 手动输入完整路径

### 步骤 2：打开并运行主 Notebook

1. 在 VS Code 左侧文件树中，展开：
   `Assignment 1 code` → `Assignment-1` → `code`
2. 双击打开 **`proj1.ipynb`**
3. 在 Notebook 右上角确认 kernel 为你选好的 `.venv` Python
4. 点击最上方的 **▶▶ Run All**（或 `Shift+Enter` 逐个运行 cell）

### 步骤 3：调试 student_code.py

如果需要断点调试 `student_code.py`：

1. 打开 `student_code.py`
2. 在需要暂停的行号左侧点击，设置断点（红点）
3. 按 `F5` 或点击左侧"运行和调试"图标 → 选择 **"Python: student_code.py"**

> `.vscode/launch.json` 已配置好调试启动项，无需额外修改。

---

## 常见报错排查

### 1. `ModuleNotFoundError: No module named 'cv2'`

**原因**：`opencv-python` 未安装或未在当前虚拟环境中。

**解决**：

```bash
# 确保已激活虚拟环境，再安装
pip install opencv-python
```

在 VS Code 中检查右下角状态栏，确保 Python 解释器显示的是 `.venv` 路径，而非系统 Python。

---

### 2. `ModuleNotFoundError: No module named 'utils'` 或 `student_code`

**原因**：运行 Notebook 时工作目录不对，Python 找不到同级的模块。

**解决**：

- 在 VS Code 中，`.vscode/settings.json` 已设置 `"jupyter.notebookFileRoot": "${fileDirname}"`，可确保工作目录为 Notebook 所在文件夹。
- 若仍报错，在 Notebook 首个 cell 手动添加：

```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath('proj1.ipynb')))
```

---

### 3. `FileNotFoundError: ... data/dog.bmp`

**原因**：图像路径是相对路径，当前工作目录不正确。

**解决**：

- 确认运行时工作目录是 `Assignment 1 code/Assignment-1/code/`
- 也可在 Notebook 中修改路径为绝对路径：

```python
import os
base = os.path.dirname(os.path.abspath('proj1.ipynb'))
image1 = load_image(os.path.join(base, '../data/dog.bmp'))
```

---

### 4. `AssertionError`（滤波器尺寸）

**原因**：传入 `my_imfilter` 的滤波器宽或高为偶数。

**解决**：确保 `ksize` 为奇数。例如使用 `cv2.getGaussianKernel(ksize=29, sigma=7)`（`cutoff_frequency=7` 时 `ksize = 7*4+1 = 29`，为奇数，正确）。

---

### 5. VS Code 提示"Select Kernel"但没有 `.venv` 选项

**原因**：虚拟环境的 `ipykernel` 未注册。

**解决**：

```bash
# 激活虚拟环境后执行
python -m ipykernel install --user --name=cv_assignment1 --display-name "CV Assignment 1 (.venv)"
```

然后在 VS Code Notebook 右上角 kernel 选择器里选择 **"CV Assignment 1 (.venv)"**。

---

### 6. Windows 下激活虚拟环境报错

**原因**：PowerShell 执行策略限制。

**解决**：以管理员身份运行 PowerShell，执行：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 快速参考

| 操作 | 命令 |
|------|------|
| 创建虚拟环境 | `python -m venv .venv` |
| 激活（Linux/macOS） | `source .venv/bin/activate` |
| 激活（Windows PS） | `.venv\Scripts\Activate.ps1` |
| 安装依赖 | `pip install -r requirements.txt` |
| 启动 Notebook | `jupyter notebook` 或 VS Code 直接打开 `.ipynb` |
| 运行全部 cell | VS Code: **▶▶ Run All**；命令行: Kernel → Restart & Run All |
