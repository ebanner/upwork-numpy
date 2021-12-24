from dataclasses import dataclass
from typing import List, Dict, Any


# class NoteBook(BaseModel):
#     # cells: List[Any]
#     # metadata: Dict[Any]
#     nbformat: int
#     nbformat_minor: int


@dataclass
class Problem:
    id: str
    title: str
    placeholder: str
    content: str
    output: str

    def __getitem__(self, key):
        return super().__getattribute__(key)
