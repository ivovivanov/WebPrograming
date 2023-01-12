import requests
import urllib3.exceptions


def is_alive(url):
    url = 'https://' + url
    url_check = False
    try:
        website_req = requests.get(url)
        if website_req.ok:
            url_check = True
    except:
        pass

    return url_check
