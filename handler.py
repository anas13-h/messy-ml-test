import runpod
import torch

# 1. GLOBAL SCOPE (Runs once when container starts)
print("--> Loading Model...")
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"--> Device selected: {device}")

# 2. HANDLER FUNCTION
def handler(job):
    job_input = job["input"]
    return {"message": "Success! The container is running.", "device": device}

# 3. ENTRY POINT
if __name__ == "__main__":
    # This prevents the script from exiting immediately
    runpod.serverless.start({"handler": handler})