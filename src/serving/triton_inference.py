import tritonclient.grpc as grpcclient

class TritonInference:
    def __init__(self, model_name):
        self.client = grpcclient.InferenceServerClient(url="localhost:8001")
        self.model_name = model_name

    def predict(self, input_data):
        inputs = [grpcclient.InferInput("input", input_data.shape, "FP32")]
        inputs[0].set_data_from_numpy(input_data)
        outputs = [grpcclient.InferRequestedOutput("output")]
        response = self.client.infer(self.model_name, inputs, outputs=outputs)
        return response.as_numpy("output")