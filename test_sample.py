import json

import pytest

from main import (get_id, get_ith_problem_cells, get_nb_cells_as_json,
                  make_csv_from_nb, make_problem, make_df, to_csv, get_nb_problems)

import pandas as pd

from fixtures import nb_str, nb, nb_cells


def test_get_nb_cells_as_json(nb_str, nb_cells):
    input = nb_str
    expected = nb_cells

    output = get_nb_cells_as_json(input)
    # same number of cells
    assert len(output) == len(expected)
    for output_cell, expected_cell in zip(output, expected):
        assert output_cell['source'] == expected_cell['source']
        assert output_cell.get('outputs') == expected_cell.get('outputs')


def test_get_ith_problem_cells(nb_cells):
    expected = nb_cells[:5]
    first_set = 0
    first_ps = get_ith_problem_cells(nb_cells, first_set)
    from dataclasses import asdict
    first_ps = [asdict(ps) for ps in first_ps]

    assert first_ps == expected


def test_get_id():
    id = get_id()
    print(id)
    for char in id:
        assert char in 'abcdefghijklmnopqrstuvwxyz' or char in '0123456789'


def test_make_problem(nb_cells):
    problem_cells = nb_cells[:5]

    expected = {
        'id': id,
        'title': """Create a zero vector ""v"" of size 10""",
        'placeholder': """import numpy as np

v = None
# Your code here
print(v)""",
        'content': """import numpy as np

v = np.zeros(10)
print(v)"""
,
        'output': "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]"
    }

    problem = make_problem(problem_cells)
    
    assert problem['title'] == expected['title']
    assert problem['placeholder'] == expected['placeholder']
    assert problem['content'] == expected['content']
    assert problem['output'] == expected['output']


def test_make_df():
    expected = pd.DataFrame([
        {
            'id': 'a',
            'title': """Create a zero vector ""v"" of size 10""",
            'placeholder': """import numpy as np

v = None
# Your code here
print(v)""",
            'content': """import numpy as np

v = np.zeros(10)
print(v)""",
            'output': '[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]'
        },
        {
            'id': 'b',
            'title': """Set "yst" to yesterday's date""",
            'placeholder': """import numpy as np

yst = None
# Your code here
print(yst)""",
            'content': """import numpy as np

yst = None
yst = np.datetime64('today') - np.timedelta64(1)
print('2021-12-09')""",
            'output': '2021-12-09'
        },
    ],
        columns=['id', 'title', 'placeholder', 'content', 'output']
    )

    problems = [
        {
            'id': '21de0a129f63435ab3a80889e17ec484',
            'title': 'Create a zero vector ""v"" of size 10',
            'placeholder': 'import numpy as np\n\nv = None\n# Your code here\nprint(v)',
            'content': 'import numpy as np\n\nv = np.zeros(10)\nprint(v)',
            'output': '[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]'
        },
        {
            'id': 'f9e96043e56c4e90a89e30d3b4785619',
            'title': 'Set "yst" to yesterday\'s date',
            'placeholder': 'import numpy as np\n\nyst = None\n# Your code here\nprint(yst)',
            'content': "import numpy as np\n\nyst = None\nyst = np.datetime64('today') - np.timedelta64(1)\nprint('2021-12-09')",
            'output': '2021-12-09'
        }
    ]

    output = make_df(problems)

    columns = ['title', 'placeholder', 'content', 'output']
    grid = expected[columns] == output[columns]
    assert grid.all().all()


def test_to_csv():
    expected = """id,title,placeholder,content,output
a,"Create a zero vector \"\"\"\"v\"\"\"\" of size 10","import numpy as np

v = None
# Your code here
print(v)","import numpy as np

v = np.zeros(10)
print(v)",[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
b,"Set ""yst"" to yesterday's date","import numpy as np

yst = None
# Your code here
print(yst)","import numpy as np

yst = None
yst = np.datetime64('today') - np.timedelta64(1)
print('2021-12-09')",2021-12-09
"""
    
    problems_df = pd.DataFrame([
        {
            'id': 'a',
            'title': """Create a zero vector ""v"" of size 10""",
            'placeholder': """import numpy as np

v = None
# Your code here
print(v)""",
            'content': """import numpy as np

v = np.zeros(10)
print(v)""",
            'output': '[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]'
        },
        {
            'id': 'b',
            'title': """Set "yst" to yesterday's date""",
            'placeholder': """import numpy as np

yst = None
# Your code here
print(yst)""",
            'content': """import numpy as np

yst = None
yst = np.datetime64('today') - np.timedelta64(1)
print('2021-12-09')""",
            'output': '2021-12-09'
        },
    ],
        columns=['id', 'title', 'placeholder', 'content', 'output']
    )
    
    output = to_csv(problems_df)
    assert output == expected


def test_full(mocker, nb_str):
    input = nb_str
    expected = """id,title,placeholder,content,output
a,"Create a zero vector \"\"\"\"v\"\"\"\" of size 10","import numpy as np

v = None
# Your code here
print(v)","import numpy as np

v = np.zeros(10)
print(v)",[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
b,"Set ""yst"" to yesterday's date","import numpy as np

yst = None
# Your code here
print(yst)","import numpy as np

yst = None
yst = np.datetime64('today') - np.timedelta64(1)
print('2021-12-09')",2021-12-09
"""
    mocker.patch('main.get_id', side_effect=['a', 'b'])
    output = make_csv_from_nb(input)
    assert output == expected


def test_get_nb_problems(nb_cells):
    input = nb_cells
    nb_problems = get_nb_problems(nb_cells)
    assert nb_problems == 2
