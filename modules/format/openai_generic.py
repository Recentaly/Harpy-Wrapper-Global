from ..typing import OpenAI_Response, Model # for type hints

# this function returns a generic OpenAI-type response
def get_openai_generic(model: Model | str = "harpy-ai", role: str = "assistant", content: str = "", finish_reason: str = "stop") -> OpenAI_Response | dict:

    return {
        "object": "chat.completion",
        "model": f"{model}",
        "choices": [{
            "index": 0,
            "message": {
                "role": f"{role}",
                "content": f"{content}",
            },
            "finish_reason": f"{finish_reason}",
        }],
    }