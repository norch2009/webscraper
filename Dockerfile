FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

WORKDIR /app
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Chromium for Playwright
RUN playwright install chromium

# Start Flask app
CMD ["python", "poe_scraper.py"]
