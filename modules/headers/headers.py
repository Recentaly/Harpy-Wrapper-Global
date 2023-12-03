from ..typing import *

# this function compiles headers and returns them 
def compile_headers(auth: Auth) -> Headers:

    return {
        
        "Host": "api.harpy.chat",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": "Bearer " + auth,
        "Content-Type": "application/json",
        "Content-Length": "2931",
        "Origin": "https://harpy.chat",
        "Connection": "keep-alive",
        "Referer": "https://harpy.chat/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers",
    }
