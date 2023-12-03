# typing
from ..typing import Model, OpenAI_Streamed

# to convert json to string
from json import dumps

# this function takes bytes as input and returns a dict with OpenAI format response in streaming mode
def get_openai_streamed(model: Model | str = "harpy-ai", role: str = "assistant", content: str = "") -> OpenAI_Streamed | str:

    return dumps({
            "object": "chat.completion.chunk",
            "model": f"{model}",
            "choices": [
                {
                    "index": 0,
                    "delta": {
                        "content": f"{content} ",
                    },
                    "finish_reason": None,
                }
            ]
        })

# this returns the last chunk in an OpenAI formatted response
def get_streamed_last(model: Model | str = "harpy-ai", role: str = "assistant") -> OpenAI_Streamed | str:

    return dumps({
        "object": "chat.completion.chunk",
        "model": f"{model}",
        "choices": [
            {
                "index": 0,
                "delta": {},
                "finish_reason": "stop",
            }
        ]
    })