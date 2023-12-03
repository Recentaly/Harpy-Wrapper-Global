# Harpy.chat LLM wrapper (unofficial)

---

## Pre-requisities

1. Python 3.10

2. pip (comes alongside Python)

---

## Installing the dependencies

1. Open up a new __cmd__ window

2. Navigate to the root of the downloaded folder

3. Execute the following command (no quotation marks): "pip3.10 install -r requirements.txt"

## Getting your authentification key

1. Head to [Harpy Chat's official website](https://harpy.chat) and __log in__

3. Open the Developer Console (F12)

4. Head to "Storage" <br>

![Storage Symbol](https://i.imgur.com/uauhW8m.png)

4. Click on "Local Storage" and then on the URL <br>

![Local Storage](https://i.imgur.com/8jthy2Y.jpg)

You will see something like this:

![Storage Expanded](https://i.imgur.com/9ubQs4k.png)

Or like this on the right of your screen: (depends on your browser)

![Storage; Right bar](https://i.imgur.com/te97oei.png) (Copy the access token from there)

__NOTICE: KEYS EXPIRE AFTER AN HOUR!__

## Key validity

Your key's validity will read here:

![Key validity](https://i.imgur.com/v2tZeVP.jpg)

__Note: It's in Unix time. Head to [unixtimestamp.com](https://www.unixtimestamp.com/) to convert Unix time to human time__

---

## Installation

1. Make sure you have it downloaded and are in the root of the folder
   
2. Navigate inside the folder and head inside the __modules__ folder

3. Open the '__config.yaml'__ file

4. Paste your key inside the quotation marks where it says __"ENTER KEY HERE"__

--- 

## Starting the server

1. Start the server by double-clicking the __app.py__ file in the root.

---

## Usage

1. If successfully started, your terminal should look something like this:

![Successfull start look](https://i.imgur.com/gET2ZUl.png)

2. The URL next to __'Running on:'__ is your usable URL.

--- 

## Troubleshoot

Error 401 Unauthorized?

=> Confirm that your access token is still valid and was correctly written inside the .yaml file

---

## Required request data (for development)

1. messages (in the request JSON, include a list of messages in OpenAI format. Example below)

```python
messages = [
  {"role": "system", "content": "You're an AI assistant. Say hello back to the user!"},
  {"role": "user", "content": "Hello, AI!"}, #   <- User starts the conversation
  {"role": "assistant", "content": "Hello, user!"}
]
```

``System:`` A 'System' message to influence the responses by the AI, etc.
``assistant:`` The AI's replies.
``user:`` The user's messages

1. ``temperature:`` (int) -> Number between __0__ and __2__

2. ``streaming:`` (boolean) -> Influences return system (If true, uses ``text/event-stream`` to use a 'fake' streaming. ``false`` uses ``application/json``

3. ``max_tokens:`` (int) -> Number which influences the maximum tokens the AI may generate.


