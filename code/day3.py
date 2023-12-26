import os
import numpy as np


def is_special(value):
    try:
        float_value = float(value)
        return False
    except (ValueError, TypeError):
        if value == ".":
            return False
        else:
            return True


def has_special_neighbor(arr, row, col):
    m, n = arr.shape

    # Define relative positions of neighbors
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        # Check if the new position is within the array bounds
        if 0 <= new_row < m and 0 <= new_col < n:
            neighbor_value = arr[new_row, new_col]
            if is_special(neighbor_value):
                return True

    return False


def make_special_matrix(arr):
    uit = []
    len_row, len_col = arr.shape
    it = np.nditer(arr, flags=["multi_index"])

    for x in it:
        row, col = it.multi_index
        uit.append(has_special_neighbor(arr, row, col))
    special_neigh_arr = np.array(uit).reshape(len_row, len_col)
    return special_neigh_arr


def find_number_subvectors(arr):
    subvectors = []
    for i in range(arr.shape[0]):
        subvector = []
        start = None

        for j in range(arr.shape[1]):
            if arr[i, j].isdigit():
                if start is None:
                    start = j
            elif start is not None:
                subvector.append((i, start, j - 1))
                start = None

        # Check if the last element in the row is a number
        if start is not None:
            subvector.append((i, start, arr.shape[1] - 1))

        subvectors.extend(subvector)

    return subvectors


def sub_vectors_allowed(sub_vector, special_neigh_arr):
    res = []
    for row, start, end in sub_vector:
        r = range(start, end + 1)
        keep = False
        for col in r:
            if special_neigh_arr[row][col]:
                keep = True
        if keep:
            res.append((row, r))
    return res


def answer1(arr, allowed):
    res = []
    for row, r in allowed_sub_vec:
        sub_str = ""
        for col in r:
            sub_str = sub_str + arr[row][col]

        res.append(int(sub_str))
    return sum(res)


def load_data(filename) -> list:
    """Get the data from adventcode in memmory."""
    file_path = os.path.join(os.getcwd(), "data", filename)
    with open(file_path, "r") as file:
        file_content = file.read()
    arr = np.array(
        [[c for c in row] for row in file_content.split("\n") if row.strip()]
    )
    return arr


arr = np.array(load_data("day3.txt"))
print(arr)
# arr = np.array([[c for c in row] for row in exampel_day3.split("\n") if row.strip()])


sub_vec = find_number_subvectors(arr)
special_neigh_arr = make_special_matrix(arr)
allowed_sub_vec = sub_vectors_allowed(sub_vec, special_neigh_arr)
print(answer1(arr, allowed_sub_vec))

# extra comment
