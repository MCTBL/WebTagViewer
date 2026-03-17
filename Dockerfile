# 使用官方 Python 3.12 精简版镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 将当前构建上下文的所有文件复制到工作目录
COPY . .

# 安装 Python 依赖（如果 requirements.txt 存在）
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1145

# 启动 server.py
CMD ["python", "server.py"]