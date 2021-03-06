import json
import sys
import uuid
import pandas as pd

from data_types import Problem, make_cell


def get_nb_cells_as_json(nb_string):
    json_dict = json.loads(nb_string)
    return json_dict['cells']


def get_ith_problem_cells(nb_cells, i):
    """

    # input
    nb_cells: notebook cells
    i: the number of problem set you want

    """
    return [make_cell(cell) for cell in nb_cells[i*5:(i*5)+5]]


def get_nb_problems(nb):
    """Get the number of problems in the notebook"""
    return len(nb) // 5


def get_problems(nb):
    nb_problems = get_nb_problems(nb)
    problems = []
    for i in range(nb_problems):
        problem_cells = get_ith_problem_cells(nb, i)
        problem = make_problem(problem_cells)
        problems.append(problem)
    return problems


def get_id():
    """

    # output
    string of length 32 with lowercase letters and numbers

    """
    return str(uuid.uuid4()).replace('-', '')


def get_title(problem_cells):
    return ''.join(problem_cells[1]['source'])


def get_placeholder(problem_cells):
     return ''.join(problem_cells[2]['source'])


def get_content(problem_cells):
    return ''.join(problem_cells[4]['source'])


def get_output(problem_cells):
    output_lines = problem_cells[4]['outputs'][0]['text']
    # strip newline off last line
    output_lines[-1] = output_lines[-1].rstrip()
    output = ''.join(output_line for output_line in output_lines)
    return output


def make_problem(problem_cells):
    id = get_id()
    title = get_title(problem_cells)
    placeholder = get_placeholder(problem_cells)
    content = get_content(problem_cells)
    output = get_output(problem_cells)
    problem = Problem(**{
        'id': id,
        'title': title,
        'placeholder': placeholder,
        'content': content,
        'output': output
    })
    return problem


def make_df(problems):
    return pd.DataFrame(
        problems,
        columns=['id', 'title', 'placeholder', 'content', 'output']
    )


def to_csv(problems_df):
    return problems_df.to_csv(index=False)


def make_csv_from_nb(nb_string):
    nb_cells = get_nb_cells_as_json(nb_string)
    problems = get_problems(nb_cells)
    problems_df = make_df(problems)
    csv = to_csv(problems_df)
    return csv


if __name__ == '__main__':
    lines = ''.join(line for line in sys.stdin)
    csv = make_csv_from_nb(lines)
    print(csv)

