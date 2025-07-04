# ✅ Official Playwright Python image
FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

# 📁 Set working directory
WORKDIR /app

# 🧠 Copy project files
COPY . .

# 📦 Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 🧱 Install Chromium + cache it to a known location
RUN PLAYWRIGHT_BROWSERS_PATH=/ms-playwright playwright install chromium

# ✅ Set env var so runtime knows where to find it
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# ✅ Run your Flask app (change to app.py if that’s the main file)
CMD ["python", "app.py"]
