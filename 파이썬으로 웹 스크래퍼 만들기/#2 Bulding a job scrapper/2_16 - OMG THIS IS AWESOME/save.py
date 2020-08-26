import csv

def save_to_file(jobs):
    # newline='' : 각 데이터 사이의 빈 줄 제거
    file = open("jobs.csv", mode="w", newline='', encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])

    for job in jobs:
        writer.writerow(list(job.values()))
    return