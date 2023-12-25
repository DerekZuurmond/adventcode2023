import os
import pandas as pd

MAX_VALE_RED = 12
MAX_VALE_BLUE = 14
MAX_VALE_GREEN = 13


with open("data/day2.txt", "r") as file:
    # Use list comprehension to create a list with each line as an element
    lines = [line.strip() for line in file.readlines()]


def parser(lines) -> pd.DataFrame:
    """This function parses the format such for each game each row has all trials.


    Args:
        lines (_type_): loaded data from txt file

    Returns:
        pd.DataFrame: DataFrame with games as rows and trials as cols
    """

    for line in lines:  # Makes dict where wth structure dict[game_no] = trial
        game_no, game_res = line.split(":")
        game_trial = game_res.lstrip().split(";")
        game_dict[game_no] = game_trial

    max_trials = max(len(trials) for trials in game_dict.values())
    columns = []
    for i in range(1, max_trials + 1):
        columns.extend([f"trial_{i}_blue", f"trial_{i}_green", f"trial_{i}_red"])

    df_data = []
    for game, trials in game_dict.items():
        game_no = int(game.split(" ")[1])
        row_data = []
        for trial in trials:
            trial_data = [0, 0, 0]  # Default values for blue, green, red
            for item in trial.split(","):
                count, color = item.strip().split()
                if color == "blue":
                    trial_data[0] = int(count)
                elif color == "green":
                    trial_data[1] = int(count)
                elif color == "red":
                    trial_data[2] = int(count)
            row_data.extend(trial_data)
        # Pad the row data with zeros to match the maximum number of trials
        row_data.extend([0] * (len(columns) - len(row_data)))
        df_data.append([game_no] + row_data)

    # Create the DataFrame
    df = pd.DataFrame(df_data, columns=["game"] + columns)
    df = df.set_index("game")
    return df


def count_colors(df, color, max_value):
    return (df.filter(like=color) <= max_value).all(axis=1)


def power_colors(df):
    red = df.filter(like="red").max(axis=1)
    blue = df.filter(like="blue").max(axis=1)
    yellow = df.filter(like="green").max(axis=1)
    cube = red * blue * yellow
    return sum(cube)


game_dict = dict()
for line in lines:
    game_no, game_res = line.split(":")
    game_trial = game_res.lstrip().split(";")
    game_dict[game_no] = game_trial


df = parser(lines)
## Solution 1
bool_red_arr = count_colors(df, "red", MAX_VALE_RED)
bool_blue_arr = count_colors(df, "blue", MAX_VALE_BLUE)
bool_green_arr = count_colors(df, "green", MAX_VALE_GREEN)
sol_bool_arr = bool_blue_arr & bool_red_arr & bool_green_arr
print(sum(sol_bool_arr[sol_bool_arr == True].index))


## Solution 2
print(power_colors(df))
