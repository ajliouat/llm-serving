class ContinuousBatching:
    def __init__(self, batch_size=32):
        self.batch_size = batch_size
        self.batch_queue = []

    def add_request(self, request):
        self.batch_queue.append(request)
        if len(self.batch_queue) >= self.batch_size:
            return self.process_batch()
        return None

    def process_batch(self):
        batch = self.batch_queue[:self.batch_size]
        self.batch_queue = self.batch_queue[self.batch_size:]
        return batch