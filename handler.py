# handler.py - Missing critical parts
import torch

# Model not loaded in global scope
# def load_model():  # Should be global!
#     return torch.load("model.pth")

def handler(event):
    # Missing error handling
    # No preprocessing logic
    # No model loading
    return {"error": "not implemented"}