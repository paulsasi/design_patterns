from dataclasses import dataclass
import json

class JsonCounter:

    @staticmethod
    def compute_field_number(data: str) -> int:
        return len(json.loads(data))