"""

Convert notebook to notebook deliverable

"""
import json
import sys


def convert(nb):
    sol_cells = get_sol_cells(nb)
    transformed_sol_cells = transform_sol_cells(sol_cells)
    desired_nb = create_nb(transformed_sol_cells)
    return desired_nb


def get_sol_cells(nb):
    nb_cells = len(nb['cells'])
    sol_cells = [nb['cells'][i] for i in range(4, nb_cells, 5)]
    return sol_cells


def transform_sol_cells(sol_cells):
    transformed_sol_cells = []
    for sol_cell in sol_cells:
        transformed_sol_cell = sol_cell.copy()
        transformed_sol_cell['source'] = transform_source(sol_cell['source'])
        transformed_sol_cells.append(transformed_sol_cell)
    return transformed_sol_cells


def transform_source(source_lines):
    transformed_lines = []
    for line in source_lines:
        if line.startswith('import numpy as np') or line.isspace():
            continue
        transformed_lines.append(line)
    return transformed_lines


def create_nb(transformed_sol_cells):
    desired_cells = []
    for i in range(len(transformed_sol_cells)):
        desired_cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# {1 + i}"
            ]
        })
        desired_cells.append(transformed_sol_cells[i])

    return {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import numpy as np"
                ]
            }
        ] + desired_cells,
        "metadata": {
            "kernelspec": {
                "display_name": "3.7.2",
                "language": "python",
                "name": "dashboards"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.7.2"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

if __name__ == '__main__':
    nb_str = ''.join(line for line in sys.stdin)
    nb = json.loads(nb_str)
    desired_nb = convert(nb)
    print(desired_nb)