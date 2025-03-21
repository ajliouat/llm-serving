#!/bin/bash

# Start Triton Inference Server
tritonserver --model-repository=models/model_repository --log-verbose=1

echo "Triton Inference Server started!"