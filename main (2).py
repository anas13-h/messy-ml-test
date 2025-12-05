# main-an.py - A "messy" ML script
import torch
import tensorflow as tf  # Mixed frameworks!
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import cv2

# Global variables everywhere
MODEL_PATH = "model.pth"
IMG_SIZE = 224

def train():
    # PyTorch code
    model = torch.nn.Linear(10, 2)
    
    # But also TensorFlow!
    tf_model = tf.keras.Sequential([
        tf.keras.layers.Dense(10)
    ])
    
    return model

def predict():
    # Uses OpenCV but not imported correctly
    img = cv2.imread("test.jpg")
    # CUDA usage but no device check
    tensor = torch.randn(1, 3, 224, 224).cuda()
    
    return "prediction"

if __name__ == "__main__":
    # No clear entry point
    train()
    predict()