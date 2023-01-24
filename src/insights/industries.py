from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    unique_industries = []
    for job in data:
        job_industry = job["industry"]
        if job_industry not in unique_industries and len(job_industry) > 0:
            unique_industries.append(job_industry)
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_data = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_data.append(job)
    return filtered_data
