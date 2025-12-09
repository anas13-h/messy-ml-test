import runpod
import torch
# IMPORT YOUR MODEL CODE HERE
# from model import load_model, predict_fn

# ---------------------------------------------------------
# 1. GLOBAL SCOPE (Runs once when container starts)
# ---------------------------------------------------------
# We load the model here so it stays in GPU memory (VRAM).
# If we put this inside the handler(), we would reload the model 
# for every single request, which is very slow.
print("--> Loading Model...")
device = "cuda" if torch.cuda.is_available() else "cpu"

# Placeholder: Replace this with actual loading logic
# model = load_model("model.pkl") 
print("--> Model Loaded Successfully")

# ---------------------------------------------------------
# 2. HANDLER FUNCTION (Runs for every API request)
# ---------------------------------------------------------
def handler(job):
    """
    job: A dictionary containing the API input.
    Example: {"input": {"prompt": "Hello world"}}
    """
    job_input = job["input"]
    
    # Run prediction
    # result = model(job_input)
    result = {"message": "Hello from Genesis AI!", "your_input": job_input}
    
    return result

# ---------------------------------------------------------
# 3. ENTRY POINT
# ---------------------------------------------------------
# This connects the function to RunPod's serverless infrastructure
runpod.serverless.start({"handler": handler})