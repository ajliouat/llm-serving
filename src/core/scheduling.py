class QoSScheduler:
    def __init__(self, qos_level):
        self.qos_level = qos_level

    def schedule(self, requests):
        if self.qos_level == "high":
            return sorted(requests, key=lambda x: x["priority"], reverse=True)
        elif self.qos_level == "medium":
            return requests
        else:
            return sorted(requests, key=lambda x: x["priority"])