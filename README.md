# Messy ML Test Repository

This repo is deliberately messy to test the Genesis Agent's scanning capabilities.

## Challenges for the Agent:
1. **Mixed Frameworks**: Both PyTorch and TensorFlow imports
2. **Missing Versions**: requirements.txt has no version pins
3. **Incomplete Handler**: handler.py doesn't load model globally
4. **Training vs Inference**: Both train.py and inference code mixed
5. **CUDA Assumptions**: Code uses `.cuda()` without checking device
6. **Unused Dependencies**: Many imported but unused libraries
7. **Missing Model File**: References model.pth but doesn't include it

## Expected Agent Behavior:
1. Detect this is primarily PyTorch (based on imports)
2. Suggest removing tensorflow from requirements.txt
3. Identify that handler.py needs fixing
4. Recommend CUDA version based on torch import
5. Ignore train.py for deployment
