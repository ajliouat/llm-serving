import time
import numpy as np
from src.serving.triton_inference import TritonInference

def benchmark_throughput(model_name, num_requests=1000):
    inference = TritonInference(model_name)
    latencies = []
    throughputs = []

    for _ in range(num_requests):
        start_time = time.time()
        input_data = np.random.rand(1, 512).astype(np.float32)  # Example input
        inference.predict({"input": input_data})
        end_time = time.time()
        latencies.append((end_time - start_time) * 1000)  # Convert to milliseconds
        throughputs.append(1 / (end_time - start_time))  # Requests per second

    avg_latency = sum(latencies) / num_requests
    avg_throughput = sum(throughputs) / num_requests
    print(f"Average latency: {avg_latency:.2f} ms")
    print(f"Average throughput: {avg_throughput:.2f} requests/sec")

if __name__ == "__main__":
    benchmark_throughput("llama-2-7b")