from dataclasses import dataclass
from typing import List, Tuple

class Scraper:

    def get_data(self) -> List[Tuple[str, int]]:
        data = [
                    ("field1", 1),
                    ("field2", 2),
                    ("field3", 3),
                    ("field4", 4)
        ]
        return data
