import requests

artist = input("Artist: ")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + artist)

o = response.json()

for result in o["results"]:
    print(result["trackName"])
