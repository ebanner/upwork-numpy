import json
import uuid


def get_nb_cells_as_json(fname):
    with open('numpy-numpy.ipynb') as f:
        lines = [line for line in f.readlines()]
        json_str = ''.join(lines)
        json_dict = json.loads(json_str)

    return json_dict['cells']


def make_csv_from_nb(ipynb_fname):
    nb_cells = get_nb_cells_as_json(ipynb_fname)
    problems = get_problems(nb_cells)
    problems_df = make_df(problems)
    csv = output_to_csv(problems_df)
    return csv


def get_ith_problem_cells(nb_cells, i):
    """

    # input
    nb_cells: notebook cells
    i: the number of problem set you want

    """
    return nb_cells[(i*5):(i*5)+5]


def get_problems(nb):
    nb_problems = len(nb) // 5
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
    problem = {
        'id': id,
        'title': title,
        'placeholder': placeholder,
        'content': content,
        'output': output
    }
    return problem
