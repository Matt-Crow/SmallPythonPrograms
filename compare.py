import csv
from typing import Callable


def main():
    #compare_files("cleanup-sites.csv", lambda r: str(int(r["envirostor_id"]))) # looks good!
    compare_files("hazardous-waste-facilities.csv", lambda r: r["epa_id"])
    #compare_files("joined-ice.csv", lambda r: str(int(r["envirostor_id"]))) # looks good!


def compare_files(file_name: str, get_key: Callable[[dict], str]):
    old_records = {get_key(r): r for r in read_csv(f"./old/{file_name}")}
    new_records = {get_key(r): r for r in read_csv(f"./new/{file_name}")}

    # check for records in old but not in new
    for old_key in old_records:
        if old_key not in new_records:
            print(f"[{file_name}] Missing from new: {old_key}")

    # check for records in new but not in old
    for new_key in new_records:
        if new_key not in old_records:
            print(f"[{file_name}] Missing from old: {new_key}")

    # check for changed records
    joined = []
    for old_key, old_value in old_records.items():
        for new_key, new_value in new_records.items():
            if old_key == new_key:
                joined.append({
                    "old": old_value,
                    "new": new_value
                })
    for pair in joined:
        for k, v in pair["old"].items():
            if pair["new"][k] != v:
                # check if it may be a set
                if str_to_set(v) != str_to_set(pair["new"][k]):
                    print(f'[{file_name}] {get_key(pair["old"])} mismatched {k} [{pair["new"][k]}] != [{v}]')
        # too excessive
        #if set(pair["old"].keys()) != set(pair["new"].keys()):
        #    print(f"[{file_name}] Mismatched keys")


def find_primary_keys(path: str) -> list[str]:
    csv = read_csv(path)
    total_records = len(csv)
    total_unique_values_for_each_column = dict()
    for column in csv[0].keys():
        values_for_this_column = (record[column] for record in csv)
        unique_values_for_this_column = set(values_for_this_column)
        total_unique_values_for_each_column[column] = len(unique_values_for_this_column)
    return [column for column, unique_count in total_unique_values_for_each_column.items() if unique_count == total_records]


def read_csv(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [record for record in reader]


def str_to_set(a_str: str) -> set:
    return set([s.strip() for s in a_str.split(",")])


if __name__ == "__main__":
    main()