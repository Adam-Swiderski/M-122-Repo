import requests

def get_movie_data(url):

    try:
        response = requests.get(url)
        response.raise_for_status()  # Löst einen HTTPError aus, wenn der HTTP-Request einen erfolglosen Statuscode zurückgegeben hat.
        return response.json()  # Gibt das JSON-decodierte dictionary zurück.
    except requests.RequestException as e:
        print(f"Fehler beim Abrufen der Filmdaten aufgrund von: {e}")  # Druckt den Fehler.
        return None  # Gibt None zurück, wenn während des HTTP-Requests Fehler auftreten.

def print_movie_info(movie_data):
    
    if not movie_data:
        print("Keine Filmdaten verfügbar")
        return

    for movie in movie_data:
        title = movie['title']['rendered']  # Extrahiert den Titel aus dem verschachtelten 'title' dictionary.
        cover_image = movie.get('custom_fields', {}).get('poster', "Nicht verfügbar")  # Holt sicher die URL des Coverbildes.
        acf_data = movie.get('acf', {})  # Holt sicher das 'acf' Feld, das das Premierendatum enthalten könnte.

        premiere_date = "Nicht verfügbar"  # Standardwert für das premierdate.
        if isinstance(acf_data, dict):
            premiere_date = acf_data.get('premiereDate', "Nicht verfügbar")  # Holt das Premierdate, wenn 'acf' ein dictionary ist.
        elif isinstance(acf_data, list) and acf_data:
            premiere_date = acf_data[0].get('premiereDate', "Nicht verfügbar")  # Holt aus dem ersten Element, wenn 'acf' eine Liste ist.

        # Daten jedes Films in ein Rahmen.
        print("+-----------------------------------------------------+")
        print("| Titel: {:44} |".format(title))
        print("| URL des Coverbilds: {:34} |".format(cover_image))
        print("| Premierendatum: {:38} |".format(premiere_date))
        print("+-----------------------------------------------------+")

if __name__ == "__main__":
    url = "https://bluecinema.ch/wp-json/wp/v2/movie?lang=en"  # API-URL, um Filmdaten zu holen.
    movie_data = get_movie_data(url)  # Ruft die Funktion auf, um die Filmdaten zu holen.
    print_movie_info(movie_data)  # Ruft die Funktion auf, um die Filminformationen zu drucken.
