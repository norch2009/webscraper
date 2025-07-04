FROM python:3.11-slim

# Dependencies for Playwright Chromium
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg \
    libglib2.0-0 libnss3 libgconf-2-4 libatk1.0-0 \
    libatk-bridge2.0-0 libx11-xcb1 libxcb1 libxcomposite1 \
    libxcursor1 libxdamage1 libxi6 libxtst6 libxrandr2 \
    libasound2 libpangocairo-1.0-0 libxss1 libgtk-3-0 \
    libdrm2 libgbm1 libxshmfence1 && \
    apt-get clean

# Copy app files
WORKDIR /app
COPY . .

# Install Python deps
RUN pip install -r requirements.txt && playwright install chromium

# Entry point
CMD ["bash", "start.sh"]
