from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    greatest_salary = 0
    for job in jobs_list:
        salary = job["max_salary"]
        if salary.isnumeric():
            if greatest_salary < int(salary):
                greatest_salary = int(salary)
    return greatest_salary


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    salary_list = []
    for job in jobs_list:
        salary = job['min_salary']
        if salary.isnumeric():
            salary_list.append(int(salary))
    return min(salary_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    # recebi ajuda de colega nesta questão
    job_keys = job.keys()
    if 'min_salary' not in job_keys or 'max_salary' not in job_keys:
        raise ValueError
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except (TypeError, ValueError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_list.append(job)
        except ValueError:
            pass
    return filtered_list
