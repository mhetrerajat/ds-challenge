class RecordLog(object):
    def __init__(self, N: int):
        self.data = [0] * N
        self.current_idx = 0
        self.size = N

    def record(self, order_id: int):
        self.data[self.current_idx] = order_id
        self.current_idx = (self.current_idx + 1) % self.size

    def get_last(self, i: int) -> int:
        return self.data[(self.current_idx - i + self.size) % self.size]


if __name__ == "__main__":
    record_log = RecordLog(3)
    record_log.record(3)
    record_log.record(2)
    record_log.record(4)

    assert record_log.get_last(2) == 2
