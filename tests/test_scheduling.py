from src.core.scheduling import QoSScheduler

def test_scheduling():
    scheduler = QoSScheduler(qos_level="high")
    requests = [{"priority": 1}, {"priority": 3}, {"priority": 2}]
    scheduled = scheduler.schedule(requests)
    assert scheduled[0]["priority"] == 3

if __name__ == "__main__":
    test_scheduling()