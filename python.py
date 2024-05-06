import requests

def get_movie_data():
    url = "https://bluecinema.ch/wp-json/wp/v2/movie?lang=en"
    response = requests.get(url)
    
    if response.status_code == 200:   #data fetch
        movie_data = response.json()
        return movie_data
    else:
        print("Failed to fetch movie data. Status code:", response.status_code)
-        return None

def print_movie_info(movie_data):
    if movie_data:   #luegt obs null ish ---> is null or not
        for movie in movie_data:
            title = movie['title']['rendered']
            cover_image = movie['custom_fields']['poster']

            # Checking if 'acf' is a dictionary or a list and then accessing 'premiereDate'
            acf_data = movie['acf']
            if isinstance(acf_data, dict):
                premiere_date = acf_data.get('premiereDate', "Not available")
            elif isinstance(acf_data, list) and len(acf_data) > 0:
                # Assuming 'premiereDate' might be in the first dictionary of the list
                premiere_date = acf_data[0].get('premiereDate', "Not available") if 'premiereDate' in acf_data[0] else "Not available"
            else:
                premiere_date = "Not available"
            
            print("Title:", title)
            print("Cover Image URL:", cover_image)
            print("Premiere Date:", premiere_date)
    else:
        print("No movie data available")

# Fetch movie data
movie_data = get_movie_data()

# Print movie info for each movie in the list
print_movie_info(movie_data)
