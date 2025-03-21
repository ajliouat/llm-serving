import psutil
import GPUtil

def monitor_system():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    gpu_usage = GPUtil.getGPUs()[0].load * 100 if GPUtil.getGPUs() else 0
    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "gpu_usage": gpu_usage,
    }