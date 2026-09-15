import bisect

class RequestLog:
    def __init__(self):
        self.seen_ids = set()
        self.timestamps = []

    def log_request(self, request_id, timestamp):
        if request_id in self.seen_ids:
            return False

        self.seen_ids.add(request_id)
        bisect.insort(self.timestamps, timestamp)
        return True

    def requests_since(self, cutoff_timestamp):
        index = bisect.bisect_left(self.timestamps, cutoff_timestamp)
        return len(self.timestamps) - index


log = RequestLog()
log.log_request("req1", 100)
log.log_request("req2", 105)
log.log_request("req3", 110)
print(log.requests_since(103))

