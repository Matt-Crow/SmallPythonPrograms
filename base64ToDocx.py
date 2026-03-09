"""
Helps troubleshoot corrupted Word documents sent by Logic Apps
"""

import base64
import json
import os

def decode_json(input_json_path: str, output_folder_path: str):
    os.makedirs(output_folder_path, exist_ok=True)
    with open(input_json_path, "rt") as file:
        as_json = json.loads(file.read())
        for doc in as_json:
            base64_str: str = doc['ContentBytes']
            print(f"{doc['Name']} ({len(base64_str)})")
            base64_bytes = base64_str.encode('utf-8')
            raw_bytes = base64.b64decode(base64_bytes)
            with open(os.path.join(output_folder_path, doc['Name']), "wb") as out:
                out.write(raw_bytes)

decode_json("corrupt.json", "corrupt")
decode_json("works.json", "works")
