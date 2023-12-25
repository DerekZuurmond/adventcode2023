"""Import the needing libraries."""
import re
import os


def get_number_string_v1(text) -> int:
    """Find all the numbers in a given text, than return first and last.

    for example  'h3ll01' will return 31
    """
    pattern = r"\d+"
    numbers = re.findall(pattern, text)
    numbers = [int(number) for number in numbers]
    if len(numbers) > 0:
        first = first_num(numbers)
        last = last_num(numbers)
        return int(first + last)
    else:
        return 0


def first_num(numbers: list) -> int:
    """Get the first digit."""
    return str(numbers[0])[0]


def last_num(numbers: list) -> int:
    """Get the last digit."""
    return str(numbers[-1])[-1]


def load_data(filename) -> list:
    """Get the data from adventcode in memmory."""
    file_name = "day1.txt"
    file_path = os.path.join(os.getcwd(), "data", file_name)
    with open(file_path, "r") as file:
        # Use list comprehension to create a list with each line as an element
        lines = [line.strip() for line in file.readlines()]
    return lines


def find_full_out_num(text) -> int:
    """Find all the numbers in a given text, than return first and last.

    for example  'hellthree1' will return 31
    """
    options_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for i in range(1, 10):
        options_mapping[str(i)] = i

    text_indices = []
    text_indices = []
    for key in options_mapping.keys():
        index = text.lower().find(key)
        while index != -1:
            text_indices.append((key, index))
            index = text.lower().find(key, index + 1)

    first_num = options_mapping[min(text_indices, key=lambda x: x[1])[0]]
    last_num = options_mapping[max(text_indices, key=lambda x: x[1])[0]]
    return int(str(first_num) + str(last_num))


input_string = "hellthree1"
result = find_full_out_num(input_string)

lines = load_data("day1")
answer = print(sum([get_number_string_v1(x) for x in lines]))


a = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]
answer2 = print(sum([find_full_out_num(x) for x in lines]))
