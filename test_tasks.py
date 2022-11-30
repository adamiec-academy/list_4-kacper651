import pytest
from test_data import IS_PALINDROME_DATA, MY_SPLIT_DATA, MIN_MAX_DATA, BORDER_MAP_DATA


def _data_args(data):
    if not data:
        return
    size = len(data[0])
    names = []
    for entry in data:
        name = []
        for arg in range(size - 1):
            name.append(str(entry[arg]))
        names.append(", ".join(name))
    return names


@pytest.mark.parametrize("arg, expected_output", IS_PALINDROME_DATA, ids=_data_args(IS_PALINDROME_DATA))
def test_task_1_is_palindrome(arg, expected_output):
    from task_1 import is_palindrome
    assert is_palindrome(arg) == expected_output


@pytest.mark.parametrize("arg, expected_output", MY_SPLIT_DATA, ids=_data_args(MY_SPLIT_DATA))
def test_task_2_my_split(arg, expected_output):
    from task_2 import my_split
    assert my_split(arg) == expected_output


@pytest.mark.parametrize("arg, expected_output", MIN_MAX_DATA, ids=_data_args(MIN_MAX_DATA))
def test_task_3_min_max(arg, expected_output):
    from task_3 import min_max
    assert min_max(arg) == expected_output


@pytest.mark.parametrize("a, b, expected_output", BORDER_MAP_DATA, ids=_data_args(BORDER_MAP_DATA))
def test_task_4_border_map(a, b, expected_output):
    from task_4 import border_map
    assert border_map(a, b) == expected_output


def test_task_5_image_drawing():
    file = open("task_5.py", "r", encoding="utf-8")
    assert file.readline().strip() != "# Remove this comment to confirm that this task is done"
