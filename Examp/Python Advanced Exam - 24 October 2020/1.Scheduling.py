jobs_numbers = [int(el) for el in input().split(', ')]
index_to_arrive = int(input())

jobs = {index: time for index, time in enumerate(jobs_numbers)}
sorted_jobs = dict(sorted(jobs.items(), key=lambda x: (x[1], x[0])))

total_time = 0
for job_index, job_time in sorted_jobs.items():
    total_time += job_time
    if job_index == index_to_arrive:
        break

print(total_time)
