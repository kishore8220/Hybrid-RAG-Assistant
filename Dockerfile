# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /Hybrid-RAG-Assistant

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Set environment variable to prevent Streamlit from prompting for email
ENV STREAMLIT_DISABLE_WELCOME_MESSAGE=true

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
