"""
1723. Find Minimum Time to Finish All Jobs

You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker.
The working time of a worker is the sum of the time it takes to complete all jobs assigned to them.
Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.

Example 1:

Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.

Example 2:

Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.
"""


def _minimum_time_required(start, jobs, k, worker_time, result):
    if start == len(jobs):
        result[0] = min(result[0], max(worker_time))
        return

    for i in range(k):
        worker_time[i] += jobs[start]
        _minimum_time_required(start + 1, jobs, k, worker_time, result)
        worker_time[i] -= jobs[start]


def minimum_time_required(jobs, k):
    start = 0
    worker_time = [0] * k
    result = [float('inf')]
    _minimum_time_required(start, jobs, k, worker_time, result)
    return result[0]


def main():
    print(minimum_time_required([3,2,3], 3))        # 3
    print(minimum_time_required([1,2,4,7,8], 2))    # 11


if __name__ == '__main__':
    main()
