from src.core.batching import ContinuousBatching

def test_batching():
    batcher = ContinuousBatching(batch_size=2)
    batcher.add_request({"input": "Request 1"})
    batcher.add_request({"input": "Request 2"})
    batch = batcher.add_request({"input": "Request 3"})
    assert len(batch) == 2

if __name__ == "__main__":
    test_batching()