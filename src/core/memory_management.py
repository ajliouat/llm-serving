class PageAttentionMemory:
    def __init__(self, max_memory):
        self.max_memory = max_memory
        self.allocated_memory = 0

    def allocate(self, size):
        if self.allocated_memory + size > self.max_memory:
            raise MemoryError("Insufficient memory")
        self.allocated_memory += size

    def free(self, size):
        self.allocated_memory -= size