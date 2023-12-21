import typing

# create type for cf_bm cookie
Auth = typing.NewType('Authentification', str)
Headers = typing.NewType('Headers', dict)
Cookies = typing.NewType('Cookies', dict)
Prompt = typing.NewType('Prompt', str)
Codec = typing.NewType('Codec', str)
Url = typing.NewType('Url', str)
Settings = typing.NewType('Settings', dict)
Messages = typing.NewType('Messages', list)
Model = typing.NewType('Model', str)
OpenAI_Response = typing.NewType('OpenAI_Response', str)
OpenAI_Streamed = typing.NewType('OpenAI_Streamed', str)
Input = typing.NewType('Input', str)
Output = typing.NewType('Output', str)
