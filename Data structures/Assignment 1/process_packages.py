# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        current_time = request.arrived_at
        # Remove finished requests
        while self.finish_time and self.finish_time[0] <= current_time:
            self.finish_time.pop(0)
        # If the buffer is empty, start processing immediately
        if not self.finish_time:
            self.finish_time.append(current_time + request.time_to_process)
            return Response(False, current_time)
        # If the buffer is full, drop the request
        if len(self.finish_time) >= self.size:
            return Response(True,-1)
        # If there's space in the buffer, start processing after the last request finishes
        start_time = max(self.finish_time[-1], current_time)
        self.finish_time.append(start_time+request.time_to_process)
        return Response(False, start_time)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
