import requests

city_name = input("Enter the city name: ")

url = f"https://api.teleport.org/api/urban_areas/slug:{city_name}/images/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response

    # Extract and print URLs that start with "https://d13k13wj6adfdf.cloudfront.net/urban_areas/"
    for photo in data.get('photos', []):
        web_url = photo.get('image', {}).get('web')
        if web_url and web_url.startswith("https://d13k13wj6adfdf.cloudfront.net/urban_areas/"):
            print(web_url)
else:
    print("Failed to fetch data. Status code:", response.status_code)