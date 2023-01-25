
from src.pre_built.counter import count_ocurrences


def test_counte():
    'Deve retornar 1639'
    result = count_ocurrences('data/jobs.csv', 'Python')
    assert result == 1639
