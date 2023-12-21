# module to send http requests
import requests

# import typing
from modules.typing import Url, Messages, Settings, Output, Auth

# import function to compile headers
from modules.headers.headers import compile_headers

# and module to parse response
from modules.response.parse import parse_response_for_message

# main class for api
class Api:

    def __init__(self, url: Url | str, auth: Auth) -> None:

        self.url = url
    
        # start a new session
        self.session = requests.Session()

        self.headers = compile_headers(auth=auth)

    def generate(self, messages: Messages | list, settings: Settings | dict = {"max_new_token": 60, "model": "sparrow-beta", "temperature": 0.7, "is_lore_supported": False, "character_id": "2e6bab2b-1bcf-4274-9012-edddffb0f098"}) -> Output | str:

        # compile the data
        data = {
            "character_id": settings.get('character_id', '2e6bab2b-1bcf-4274-9012-edddffb0f098'),
            "is_lore_supported": settings.get('is_lore_supported', False),
            "temperature": settings['temperature'],
            "messages": messages,
            "max_new_token": settings['max_new_token'],
            "model": settings['model'],
        }

        # send a post request to the url with the headers
        with self.session.post(self.url, headers=self.headers, json=data) as response:

            # raise errros if any occur
            response.raise_for_status()

            # return whatever the ai replied
            return parse_response_for_message(response)
