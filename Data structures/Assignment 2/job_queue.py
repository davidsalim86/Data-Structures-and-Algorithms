from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def heap_push(heap, item):
    heap.append(item)
    idx = len(heap) - 1
    parent = (idx - 1) // 2
    while idx > 0 and heap[idx] < heap[parent]:
        heap[idx], heap[parent] = heap[parent], heap[idx]
        idx = parent
        parent = (idx - 1) // 2

def heap_pop(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    item = heap.pop()
    idx = 0
    size = len(heap)
    while True:
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        min_idx = idx
        
        if left_child < size and heap[left_child] < heap[min_idx]:
            min_idx = left_child
        if right_child < size and heap[right_child] < heap[min_idx]:
            min_idx = right_child
        if min_idx == idx:
            break
        heap[idx], heap[min_idx] = heap[min_idx], heap[idx]
        idx = min_idx
    return item

def assign_jobs(n_workers, jobs):
    result = []
    # Initialize the heap with (next_free_time, worker_id) tuples
    heap = [(0, worker) for worker in range(n_workers)]
    
    for job in jobs:
        # Pop the worker with the smallest next_free_time
        next_free_time, worker = heap_pop(heap)
        # Append the job assignment to the result
        result.append(AssignedJob(worker, next_free_time))
        # Push the worker back into the heap with the updated next_free_time
        heap_push(heap, (next_free_time + job, worker))

    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)

if __name__ == "__main__":
    main()