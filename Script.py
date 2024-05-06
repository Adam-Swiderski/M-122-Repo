from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
try:
    # Webdriver-Optionen konfigurieren, um den Browser unsichtbar zu machen
    chrome_options = Options()
    chrome_options.headless = True

    # Pfad zum Chromedriver angeben (stellen Sie sicher, dass Sie den Chromedriver heruntergeladen haben)
    chromedriver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    # URL der Website
    URL = "https://bluecinema.ch/en/daily-program/"
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    driver.implicitly_wait(30)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    driver.quit()

    # Finde alle Span-Elemente mit dem Text "Jetzt kostenlos" und gib das übergeordnete <a>-Tag zurück
    parent_a_tags = []
    cards = soup.find_all('div', {"class":'card'})
    for card in cards:
        print(card)
        title = card.find_all(name:"h4", {"class":'pointer'})
        # parent_a_tag = span.find_parent('a')
        # img_tags = []
        # # get_game_name(  parent_a_tag.get("href"))
        # for img_tag in parent_a_tag.find_all('img'):
        #     img_tags.append(img_tag.get("src"))
    


except Exception as e:
    print( f"ERROR: {str(e)}")
