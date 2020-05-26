# python3

from collections import namedtuple
from queue import PriorityQueue
import itertools

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.

    q = PriorityQueue()
    counter = itertools.count()
    for i in range(n_workers):
        q.put((0,next(counter), i))

    result = []
    for job in jobs:
        next_worker = q.get()
        result.append(AssignedJob(next_worker[2], next_worker[0]))
        q.put((next_worker[0] + job, next(counter), next_worker[2]))

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
