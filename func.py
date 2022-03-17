import requests
import re
url = "http://virgool.io"

def pyanywhere_requester(url):
    if not "http" in url:
        url = "http://" + url
    short_url = requests.post("http://urlshorter.pythonanywhere.com/short", data={"url":url}).json()["short_url"] # https://github.com/ebad84/url-shorter
    # print(short_url.headers)
    url = f"https://api.allorigins.win/get?callback=myFunc&url={short_url}"
    regex_command = r".{1,}\"contents\"\:\"(.{0,})\",\"status\""
    res = requests.get(url).text
    out = re.findall(regex_command, res)
    # print(out[0].strip())
    try:
        out = out[0].replace(r"\r", "").replace(r"\n","").replace('\\"', '"').replace(r"\t", "").replace(": true", ": True").replace(":true", ":True")
        # print(out)
        return str(out)
    except:
        return "something is wrong i can feel it..."

        
print(pyanywhere_requester(url))
