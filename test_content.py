import json

from main import get_problems, get_placeholder, get_content


def test_your_code_here():
    """Ensure placeholder and content are 1-to-1 when
    `# Your code here' is swapped out with the solution.

    """
    with open('numpy-numpy.ipynb') as f:
        nb_str = ''.join(f.readlines())
        nb = json.loads(nb_str)
        nb_cells = nb['cells']

    for i, problem in enumerate(get_problems(nb_cells), 1):
        print(i)
        placeholder = problem['placeholder']
        content = problem['content']
        j = None
        placeholder_lines = placeholder.split('\n')
        content_lines = content.split('\n')
        for line_no, line in enumerate(placeholder_lines):
            if line == '# Your code here':
                j = line_no
                break
        placeholder_lines[j] = content_lines[j]
        for placeholder_line, content_line in zip(placeholder_lines, content_lines):
            assert placeholder_line == content_line
