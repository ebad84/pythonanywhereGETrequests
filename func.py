import requests
import re
url = "http://virgool.io"

def pyanywhere_requester(url):
    if not "http" in url:
        url = "http://" + url
    url = f"https://api.allorigins.win/get?callback=myFunc&url={url}"
    regex_command = r".{1,}\"contents\"\:\"(.{0,})\",\"status\""
    res = requests.get(url).text
    out = re.findall(regex_command, res)
    try:
        return str(out[0])
    except:
        return "something is wrong i can feel it..."
        
print(pyanywhere_requester(url))
