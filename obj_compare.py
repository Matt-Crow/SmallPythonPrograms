"""
Compares collections of objects to see which properties are different.
Currently only supports csv
"""


import csv
from typing import Callable


def read_csv(path: str) -> list[dict]:
    with open(path) as f:
        reader = csv.DictReader(f)
        return [record for record in reader]


def get_primary_keys(objs: list[dict]) -> list[str]:
    total_records = len(objs)
    key_to_total_unique_values = dict()
    for key in objs[0].keys():
        values = (obj[key] for obj in objs)
        unique_values = set(values)
        key_to_total_unique_values[key] = len(unique_values)
    return [key for key, total_unique_values in key_to_total_unique_values if total_unique_values == total_records]


def compare(old_objs: list[dict], new_objs: list[dict], get_key: Callable[[dict], str]):
    old_map = {get_key(obj): obj for obj in old_objs}
    new_map = {get_key(obj): obj for obj in new_objs}

    for old_key in old_map:
        if old_key not in new_map:
            print(f"New is missing key [{old_key}]")
    
    for new_key in new_map:
        if new_key not in old_map:
            print(f"Old is missing key [{new_key}]")
    
    # now check for changed records
    joined = []
    for old_key, old_obj in old_map.items():
        for new_key, new_obj in new_map.items():
            if old_key == new_key:
                joined.append((old_key, old_obj, new_obj))
    for pair in joined:
        pk = pair[0]
        old_obj = pair[1]
        new_obj = pair[2]
        for key in old_obj.keys():
            old_value = old_obj[key]
            new_value = new_obj[key]
            if old_value != new_value:
                print(f"{pk} [{old_value}] != [{new_value}]")
