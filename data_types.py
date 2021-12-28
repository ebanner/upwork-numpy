from dataclasses import dataclass
from typing import Dict, Optional, List


def make_cell(cell):
    if cell['cell_type'] == 'markdown':
        return MarkdownCell(**cell)
    elif cell['cell_type'] == 'code':
        return CodeCell(**cell)


@dataclass
class CodeCell:
    cell_type: str
    metadata: Dict
    source: List
    execution_count: int
    outputs: List

    def __getitem__(self, key):
        return super().__getattribute__(key)


@dataclass
class MarkdownCell:
    cell_type: str
    metadata: Dict
    source: List

    def __getitem__(self, key):
        return super().__getattribute__(key)


@dataclass
class Problem:
    id: str
    title: str
    placeholder: str
    content: str
    output: str

    def __getitem__(self, key):
        return super().__getattribute__(key)
