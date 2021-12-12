from main import (get_id, get_ith_problem_cells, get_nb_cells_as_json,
                  make_csv_from_nb, make_problem)


def test_full():
    input = 'numpy-numpy.ipynb'
    expected = """id,title,placeholder,content,output^M
0622e7b5a2cd4df09c26203dbb0cda20,"Create a zero vector ""v"" of size 10","import numpy as np

# Your code here
print(v)","import numpy as np

v = np.zeros(10)
print(v)",[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]^M
eca6fe43d8624c4c99edcffa58edade7,"Set ""yst"" to yesterday's date","import numpy as np

yst = None;
# Your code here
print(yst)","import numpy as np

yst = None;
yst = np.datetime64('today') - np.timedelta64(1)
print('2021-12-09')",2021-12-09"""
    output = make_csv_from_nb(input)
    assert output == expected


def test_get_nb_cells_as_json():
    input = 'numpy-numpy.ipynb'

    expected = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 1"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Create a zero vector \"\"v\"\" of size 10"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 9,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "None\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "v = None\n",
                "# Your code here\n",
                "print(v)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Solution"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 10,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "v = np.zeros(10)\n",
                "print(v)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 2"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Set \"yst\" to yesterday's date"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 11,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "None\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "yst = None\n",
                "# Your code here\n",
                "print(yst)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Solution"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 12,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "2021-12-09\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "yst = None\n",
                "yst = np.datetime64('today') - np.timedelta64(1)\n",
                "print('2021-12-09')"
            ]
        }
    ]

    output = get_nb_cells_as_json(input)
    # same number of cells
    assert len(output) == len(expected)
    for output_cell, expected_cell in zip(output, expected):
        assert output_cell['source'] == expected_cell['source']
        assert output_cell.get('outputs') == expected_cell.get('outputs')


def test_get_ith_problem_cells():
    nb_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 1"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Create a zero vector \"\"v\"\" of size 10"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 9,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "None\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "v = None\n",
                "# Your code here\n",
                "print(v)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Solution"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 10,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "v = np.zeros(10)\n",
                "print(v)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 2"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Set \"yst\" to yesterday's date"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 11,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "None\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "yst = None\n",
                "# Your code here\n",
                "print(yst)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 12,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "2021-12-09\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "yst = None\n",
                "yst = np.datetime64('today') - np.timedelta64(1)\n",
                "print('2021-12-09')"
            ]
        }
    ]

    expected = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 1"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Create a zero vector \"\"v\"\" of size 10"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 9,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "None\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "v = None\n",
                "# Your code here\n",
                "print(v)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Solution"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 10,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "v = np.zeros(10)\n",
                "print(v)"
            ]
        },
    ]

    first_set = 0
    first_ps = get_ith_problem_cells(nb_cells, first_set)

    assert first_ps == expected


def test_get_id():
    id = get_id()
    print(id)
    for char in id:
        assert char in 'abcdefghijklmnopqrstuvwxyz' or char in '0123456789'


def test_make_problem():
    problem_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 1"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Create a zero vector \"\"v\"\" of size 10"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 9,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "None\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "v = None\n",
                "# Your code here\n",
                "print(v)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Solution"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 10,
            "metadata": {},
            "outputs": [
                {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n"
                ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "v = np.zeros(10)\n",
                "print(v)"
            ]
        },
    ]

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
    print("problem['output']")
    print(problem['output'])
    print("expected['output']")
    print(expected['output'])
    assert problem['placeholder'] == expected['placeholder']
    assert problem['content'] == expected['content']
    assert problem['output'] == expected['output']
