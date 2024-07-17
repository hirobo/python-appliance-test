import pandas as pd
import json
import requests
import os
from urllib.parse import urlencode


class DataFrame_Excersises():

    def __init__(self, name: str):
        # comment: the variable name "name" is not suitable, since we expect a path there
        self.name = name

    def import_data(self) -> pd.DataFrame:
        # Implement a function which read data from csv to DataFrame. Return DataFrame.

        if not self.name.lower().endswith('.csv'):
            raise ValueError("The file is not a CSV file.")

        if not os.path.isfile(self.name):
            raise FileNotFoundError("The file does not exist.")

        df = pd.read_csv(self.name, delimiter=";")

        return df

    def group_by_difficulty(self, dif_level: str) -> pd.DataFrame:  # comment: I'd rather call this filter_by_difficulty
        df = DataFrame_Excersises(self.name).import_data()
        # Implement a function which extract DataFrame containing all exercises with given difficulty level (dif_level). Return extracted DataFrame.
        if dif_level not in ["Easy", "Average", "Hard"]:
            raise ValueError("Invalid difficulty level")

        df_filtered = df[df["Difficulty"] == dif_level].reset_index(drop=True)

        return df_filtered

    def get_statistics(self, mg, **kwargs) -> pd.DataFrame:
        # Assign values to difficutly as following: average -> 5, easy -> 1, hard -> 10. Return requested statistics for a group of muscle in a format of dataframe. Pass kwargs as argument for the function.
        # zB    {"mg":"Forearms","Rating": ["mean", "median"], "Difficulty":["mean", "std"]} ->  {"Rating":{"mean":5.0,"median":4.5,"std":null},"Difficulty":{"mean":5.0,"median":null,"std":3.0779350563}}
        df = DataFrame_Excersises(self.name).import_data()

        results = {}

        filtered_df = df[df['muscle_gp'] == mg]

        for key, stats in kwargs.items():
            if key not in ["Rating", "Difficulty"]:
                raise ValueError(f"Unsupported key: {key}")
            column_stats = {}
            series = filtered_df[key]
            if key == "Difficulty":
                series = series.map({'Average': 5, 'Easy': 1, 'Hard': 10})

            for stat in stats:
                try:
                    column_stats[stat] = series.agg(stat)
                except AttributeError:
                    raise ValueError(f"unexpected statistic: {stat}")
            results[key] = column_stats

        result_df = pd.DataFrame(results)

        return result_df

    def create_nested_dict(self) -> dict:
        # From given DataFrame create a nested dictionary, where all excersises are grouped according to their muscle group and description contains their Rating and Difficuty
        # z.B. {"Abdominals": {"Elbow plank": {"Rating": 8, "Difficulty": "Hard"},"Landmine twist": {"Rating": 10, "Difficulty": "Hard"} ...}
        df = DataFrame_Excersises(self.name).import_data()
        gym_dict = {}


        # comment: if there is multiple entries for the same (muscle_gp, Exercise_Name), the last one to be taken
        for _, row in df.iterrows():
            muscle_group = row['muscle_gp']
            exercise_name = row['Exercise_Name']
            rating = row['Rating']
            difficulty = row['Difficulty']

            if muscle_group not in gym_dict:
                gym_dict[muscle_group] = {}

            gym_dict[muscle_group][exercise_name] = {
                'Rating': rating,
                'Difficulty': difficulty
            }

        return gym_dict

    def request_send_url(self, timeout: int) -> str:
        # Create a GET request with URL query string, where parameters are taken from previously created dict, excersises provided for 'Neck'. Include timeout and check for applicability of provided timeout value.

        if not isinstance(timeout, int) or timeout <= 0:
            raise ValueError("Timeout must be a positive integer")

        with open(self.name, "r") as read_file:
            gym_dict = json.load(read_file)

        neck_exercises = gym_dict.get('Neck', {})
        if not neck_exercises:
            raise ValueError("No exercises found for 'Neck'")

        params = []
        for exercise, details in neck_exercises.items():
            for key in details.keys():
                params.append((exercise, key))

        query_string = urlencode(params)
        link_for_request = f'https://httpbin.org/get?{query_string}'

        return link_for_request

    def request_get_data(self) -> str:
        # Request a json file from provided link. Return the title of the first slide in slideshow.

        link_for_request = 'https://httpbin.org/json'

        try:
            response = requests.get(link_for_request)
            response.raise_for_status()
            data = response.json()
            first_slide_title = data['slideshow']['slides'][0]['title']
            return first_slide_title
        except requests.RequestException as e:
            raise RuntimeError(f"HTTP request failed: {str(e)}") from e
        except (KeyError, TypeError) as e:
            raise RuntimeError(f"Data structure error: {str(e)}") from e
