import time
import numpy as np
from src.serving.triton_inference import TritonInference

def benchmark_latency(model_name, num_requests=100):
    inference = TritonInference(model_name)
    latencies = []

    for _ in range(num_requests):
        start_time = time.time()
        input_data = np.random.rand(1, 512).astype(np.float32)  # Example input
        inference.predict({"input": input_data})
        end_time = time.time()
        latencies.append((end_time - start_time) * 1000)  # Convert to milliseconds

    avg_latency = sum(latencies) / num_requests
    print(f"Average latency: {avg_latency:.2f} ms")

if __name__ == "__main__":
    benchmark_latency("llama-2-7b")