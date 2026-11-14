import requests

headers = {
    "AIC-User-Agent": "museum-crawler (yli26@berklee.edu)",
    "User-Agent": "museum-crawler (yli26@berklee.edu)",
}

url = "https://api.artic.edu/api/v1/artworks/search"


def format_and_print(data, min, max):  # data param should be a dict
    data = data['data']

    for d in data:
        title = d['title']
        artist = d['artist_display']
        date = d['date_display']
        year = d['date_start']

        if year is not None and year >= min and year <= max:
            print(title, "is by", artist, "which was displayed on", date)


search = input("What would you like to search? ")
min_year = int(input("What's the minimum year you'd like to search? "))
max_year = int(input("What's the maximum year you'd like to search? "))
print()

params = {
    'q': search,
    'fields': "title,artist_display,date_display,date_start",  # no spaces here
    'limit' : 100
}

response = requests.get(url, params=params, headers=headers)
data = response.json()
format_and_print(data, min_year, max_year)