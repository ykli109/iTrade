# iTrade

## 安装依赖包

在项目根目录下运行以下命令以安装所需的依赖包：

```bash
pip install -r requirements.txt
```

### 使用虚拟环境（可选）

为了避免依赖包之间的冲突，建议使用虚拟环境。您可以使用 `venv` 或 `virtualenv` 创建一个虚拟环境：

```bash
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
#Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
# 然后安装依赖包
pip install -r requirements.txt
# 固化依赖
pip freeze > requirements.txt
```
