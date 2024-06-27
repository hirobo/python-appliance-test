import pandas as pd
import json
import requests

class DataFrame_Excersises():
    def __init__(self, name: str):
        self.name = name
    def import_data(self) -> pd.DataFrame:
#### Implement a function which read data from csv to DataFrame. Return DataFrame.
        return 0
    def group_by_difficulty(self, dif_level: str) -> pd.DataFrame:
        df = DataFrame_Excersises(self.name).import_data()
#### Implement a function which extract DataFrame containing all exercises with given difficulty level (dif_level). Return extracted DataFrame.
        return df

    def get_statistics(self, mg, **kwargs) -> pd.DataFrame:
#### Assign values to difficutly as following: average -> 5, easy -> 1, hard -> 10. Return requested statistics for a group of muscle in a format of dataframe. Pass kwargs as argument for the function.
#### zB    {"mg":"Forearms","Rating": ["mean", "median"], "Difficulty":["mean", "std"]} ->  {"Rating":{"mean":5.0,"median":4.5,"std":null},"Difficulty":{"mean":5.0,"median":null,"std":3.0779350563}}
        return 0
    def create_nested_dict(self) -> dict:
#### From given DataFrame create a nested dictionary, where all excersises are grouped according to their muscle group and description contains their Rating and Difficuty
#### z.B. {"Abdominals": {"Elbow plank": {"Rating": 8, "Difficulty": "Hard"},"Landmine twist": {"Rating": 10, "Difficulty": "Hard"} ...}
        df = DataFrame_Excersises(self.name).import_data()
        gym_dict = {}
        return gym_dict
    def request_send_url(self, timeout: int) -> str:
#### Create a GET request with URL query string, where parameters are taken from previously created dict, excersises provided for 'Neck'. Include timeout and check for applicability of provided timeout value.
        with open(self.name, "r") as read_file:
            gym_dict = json.load(read_file)
        link_for_request = 'https://httpbin.org/get'
        return ' '
    def request_get_data(self) -> str:
#### Request a json file from provided link. Return the title of the first slide in slideshow.

        link_for_request = 'https://httpbin.org/json'

        return ' '




