import requests
import urllib.parse
url = urllib.parse.quote(input("Please paste the link you would like to shorten: "))
short = requests.get(f"https://api.shrtco.de/v2/shorten?url={url}").json()
print(f"Your new link is: {short['result']['full_short_link']}")
