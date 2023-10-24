import requests
import sys
import json

class RhodesAPIClient:

    def __init__(self) -> None:
        self.__query_params = {}
        self.__base_url = "https://rhodesapi.up.railway.app/api/search"
    
    def get_operator(self):
        response = requests.get("https://rhodesapi.up.railway.app/api/operator/mudrock")
        
        self.jprint(response.json())

    def get_recruitments(self):
        url = self.__base_url + "?" + "&".join(f"{key}={value}" for key, value in self.query_params.items())
        
        response = requests.get(url)

        json_str = json.dumps(response.json(), sort_keys=True, indent=4)
        data = json.loads(json_str)

        for operator in data:
            print(operator["name"])

    def jprint(self, obj):
        # Create formatted string of python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def add_query_params(self, param, value):
        if not param or not value:
            raise ValueError("Parameter and value must not be empty.")

        if param in self.query_params:
            raise ValueError(f"Parameter '{param}' already exists.")

        self.set_query_param(param, value)

    def modify_query_param(self, param, value):
        if not param or not value:
            raise ValueError("Parameter and value must not be empty.")

        if param not in self.query_params:
            raise ValueError(f"Parameter '{param}' does not exist.")

        self.set_query_param(param, value)

    @property
    def query_params(self):
        return self.__query_params

    def set_query_param(self, param, value):
        if not param or not value:
            raise ValueError("Parameter and value must not be empty.")

        self.__query_params[param] = value