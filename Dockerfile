# ✅ Use official Playwright image with Python support
FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

# 📁 Set working directory
WORKDIR /app

# 🧠 Copy your entire project
COPY . .

# 📦 Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# 🧱 Install Chromium browser during build
RUN playwright install chromium

# ✅ Start your script
CMD ["python", "poe_scraper.py"]
