# ✅ Use official Playwright image (with full Chromium support)
FROM mcr.microsoft.com/playwright/python:v1.44.0-focal

# 📁 Set working directory
WORKDIR /app

# 📄 Copy all files
COPY . .

# 📦 Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# 🧱 Install full Chromium dependencies
RUN playwright install --with-deps

# 🚀 Run your app
CMD ["python", "app.py"]
