# -----------------------------------------------------------
# GENESIS AI AUTOMATED DOCKERFILE (GPU - PyTorch)
# -----------------------------------------------------------

# 1. Base Image: Pre-loaded with CUDA and PyTorch
# We use the argument passed from our compatibility_matrix.json
ARG BASE_IMAGE=runpod/pytorch:2.0.1-py3.10-cuda11.8.0-devel 
FROM ${BASE_IMAGE}

# 2. System Setup
# Ensure Python output is sent directly to terminal (logs help debugging)
# 2. System Setup


ENV PYTHONUNBUFFERED=1 

# Set the working directory inside the container
# This is like 'cd /app' in your terminal. All future commands happen here.
WORKDIR /app

# 3. Dependencies
# We copy the requirements file first to leverage Docker caching.
# If requirements.txt hasn't changed, Docker skips the 'pip install' step.
COPY requirements(messy).txt .

# Install dependencies. 
# --no-cache-dir: Don't save downloaded files (keeps image small)
# --upgrade: Ensure we have the latest pip
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 4. App Logic
# Copy all user files into the container
COPY . .

# 5. Execution Command
# This command starts the handler using Python.
# 'python -u' means unbuffered (logs show up instantly)
CMD ["python", "-u", "handler.py"]