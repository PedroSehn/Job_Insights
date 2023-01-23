from functools import lru_cache
from typing import List, Dict
import csv
doc_path = '../data/job.csv'


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, 'r') as data:
        data_list = csv.DictReader(data)
        clear_data_list = [*data_list]
    return clear_data_list


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
