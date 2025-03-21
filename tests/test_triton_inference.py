from src.serving.triton_inference import TritonInference

def test_triton_inference():
    inference = TritonInference("llama-2-7b")
    output = inference.predict({"input": "Sample input"})
    assert output is not None

if __name__ == "__main__":
    test_triton_inference()