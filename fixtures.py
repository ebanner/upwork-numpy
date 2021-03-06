import json

import pytest


@pytest.fixture
def nb_str():
    return r'''{
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
       "execution_count": 1,
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
       "execution_count": 2,
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
       "execution_count": 3,
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
       "execution_count": 4,
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
    }'''


@pytest.fixture
def nb(nb_str):
    return json.loads(nb_str)


@pytest.fixture
def nb_cells(nb):
    return nb['cells']
