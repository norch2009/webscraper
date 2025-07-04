# ✅ Official Playwright image with Chromium
FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

# 📁 Set working directory
WORKDIR /app

# 🧠 Copy project files
COPY . .

# 📦 Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ❌ DO NOT repeat playwright install chromium (already installed in image)

# 🚀 Start with app.py (Flask)
CMD ["python", "app.py"]
