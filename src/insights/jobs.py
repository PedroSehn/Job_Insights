from functools import lru_cache
from typing import List, Dict
import csv
doc_path = '../data/job.csv'


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, 'r', encoding="utf8") as data:
        data_list = csv.DictReader(data)
        clear_data_list = list(data_list)
    return clear_data_list


def get_unique_job_types(path: str) -> List[str]:
    data_list = read(path)
    unique_jobs_list = []
    for job in data_list:
        job_type = job["job_type"]
        if job_type not in unique_jobs_list:
            unique_jobs_list.append(job_type)
    return unique_jobs_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_data = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_data.append(job)
    return filtered_data
