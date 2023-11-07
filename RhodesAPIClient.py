import requests

class RhodesAPIClient:

    def __init__(self) -> None:

        # Recruit Endpoint
        self.__base_url = "https://rhodesapi.up.railway.app/api/recruit"
    
    def get_recruitments(self, tag1="", tag2="", tag3=""):

        # Declare Dictionary for return
        operators = dict()

        # Parameter required for endpoints
        params = {
            "tag1": tag1,
            "tag2": tag2,
            "tag3": tag3,
        }
        
        try:
            # Make the API request
            response = requests.get(self.__base_url, params=params)
            
            # Check the HTTP status code for errors
            if response.status_code == 200:
                data = response.json()

                # Iterate through operators
                for operator in data:

                    # Get operator attributes
                    name = operator["name"]
                    rarity = operator["rarity"]
                    tags = operator["tags"]

                    operator_data = {"rarity": rarity, "tags": tags}
                    operators[name] = operators.get(name, operator_data)

            else:
                # Handle the API request error here
                print(f"API request failed with status code {response.status_code}")

        except Exception as e:
            # Handle any other exceptions that might occur
            print(f"An error occurred: {str(e)}")

        # Returns Operators
        return operators
