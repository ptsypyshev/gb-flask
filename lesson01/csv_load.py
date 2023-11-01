from csv import DictReader
from random import shuffle

def load_dict(file_path: str) -> dict:
    result = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for row in DictReader(f, delimiter=','):
            result[row['name']] = row
        return result

def load_listdict(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as f:
        return list(DictReader(f, delimiter=','))

def get_random_items(items: list, length: int) -> list:
    result = items[:]
    shuffle(result)
    return result[:length]


def get_category_items(items: list, category: str, length: int = 9) -> list:
    result = []
    for elem in items:
        if not elem['category'] == category:
            continue
        result.append(elem)
    return get_random_items(result, length)
