from convert import get_sol_cells, transform_source, transform_sol_cells, create_nb, convert
from main import get_nb_cells_as_json
import json


def test_convert():
    input_str = r'''{
     "cells": [
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
       "execution_count": null,
       "metadata": {},
       "outputs": [],
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
       "execution_count": null,
       "metadata": {},
       "outputs": [],
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
       "execution_count": null,
       "metadata": {},
       "outputs": [],
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
       "execution_count": null,
       "metadata": {},
       "outputs": [],
       "source": [
        "import numpy as np\n",
        "\n",
        "yst = None\n",
        "yst = np.datetime64('today') - np.timedelta64(1)\n",
        "print('2021-12-09')"
       ]
      }
     ],
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
    }'''
    input = json.loads(input_str)

    expected_nb_str = r'''{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
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
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "yst = None\n",
    "yst = np.datetime64('today') - np.timedelta64(1)\n",
    "print('2021-12-09')"
   ]
  }
 ],
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
}'''
    expected = json.loads(expected_nb_str)
    output = convert(input)
    assert output == expected


def test_get_sol_cells():
    nb = {
    "cells": [
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
    "execution_count": 24,
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
    "execution_count": 25,
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
    "execution_count": 26,
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
    "execution_count": 27,
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
    ],
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

    expected = [
    {
    "cell_type": "code",
    "execution_count": 25,
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
    "cell_type": "code",
    "execution_count": 27,
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
    output = get_sol_cells(nb)
    assert output == expected


def test_transform_sol_cells():
    sol_cells = [
    {
    "cell_type": "code",
    "execution_count": 25,
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
    "cell_type": "code",
    "execution_count": 27,
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
    "cell_type": "code",
    "execution_count": 25,
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
        "v = np.zeros(10)\n",
        "print(v)"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 27,
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
        "yst = None\n",
        "yst = np.datetime64('today') - np.timedelta64(1)\n",
        "print('2021-12-09')"
    ]
    }
    ]
    output = transform_sol_cells(sol_cells)
    assert output == expected


def test_transform_source():
    input = [
        "import numpy as np\n",
        "\n",
        "v = np.zeros(10)\n",
        "print(v)"
    ]
    expected = [
        "v = np.zeros(10)\n",
        "print(v)"
    ]
    output = transform_source(input)
    assert output == expected


def test_create_nb():
    input = [
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "v = np.zeros(10)\n",
                "print(v)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "yst = None\n",
                "yst = np.datetime64('today') - np.timedelta64(1)\n",
                "print('2021-12-09')"
            ]
        }
    ]

    expected = {
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
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
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "yst = None\n",
    "yst = np.datetime64('today') - np.timedelta64(1)\n",
    "print('2021-12-09')"
   ]
  }
 ],
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
    output = create_nb(input)
    assert output == expected
