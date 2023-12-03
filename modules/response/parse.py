from requests import Response # for type hints
from ..typing import Codec # also for type hints

# json module to process response
from json import loads

# this function simply takes a response and returns the ai's generated text inside
def parse_response_for_message(response: Response, codec: Codec | str = 'utf-8', prefix: str = "[", suffix: str = "]") -> str:

    return loads(response.content.decode(codec).removeprefix(prefix).removesuffix(suffix))['generated_text']