import json
from selenium import webdriver
from fake_useragent import UserAgent


def get_features(filename):
    """
    first -> if first time user the browser's profile.
    tries -> if failed to scrape data. give it another go
    """
    with open(filename, 'r') as f:
        songs = json.loads(f.read())
    url = "https://musicstax.com/search?q="
    tries = 0
    first = 0
    for song in songs:
        while True:
            if first == 0:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--start-maximized")
                # Adding fake google user to avoid captcha
                ua = UserAgent()
                userAgent = ua.random
                chrome_options.add_argument(f'user-agent={userAgent}')  # bypass captcha
                # chrome_options.add_argument("headless")  # we dont want to see the whole proccess..
                browser = webdriver.Chrome('./chromedriver', options=chrome_options)
                first += 1
            try:
                artist = song['Artist']
                title = song['Title']
                search = title + " " + artist
                search = search.replace(' ', '+')  # replace space with + in the url
                browser.get(url=(url + search))
                # search and click on result
                next_ur = browser.find_element_by_xpath('*//a[@class="song-details-right search-details-right"]')
                next_ur=next_ur.get_attribute("href")
                browser.get(next_ur)
                key = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[5]/div[3]/div[3]').text
                scale, key = key.split()
                bpm = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[5]/div[2]/div[3]').text
                length = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[5]/div[1]/div[3]').text
                danceability = browser.find_element_by_xpath(
                    '/html/body/div[2]/div[3]/div/div[7]/div[1]/div/div/div[2]/div/div[3]/div/div').text
                positiveness = browser.find_element_by_xpath(
                    '/html/body/div[2]/div[3]/div/div[7]/div[1]/div/div/div[4]/div/div[3]/div/div').text
                liveness = browser.find_element_by_xpath(
                    '/html/body/div[2]/div[3]/div/div[7]/div[1]/div/div/div[6]/div/div[3]/div/div').text
                energy = browser.find_element_by_xpath(
                    '/html/body/div[2]/div[3]/div/div[7]/div[1]/div/div/div[3]/div/div[3]/div/div').text
                speechness = browser.find_element_by_xpath(
                    '/html/body/div[2]/div[3]/div/div[7]/div[1]/div/div/div[5]/div/div[3]/div/div').text
                song['Length'] = length
                song['Scale'] = scale  # A#,Bb,C...
                song['Key'] = key  # Major/ Minor
                song['BPM'] = bpm
                # They all have % at the end.
                song['Danceability'] = danceability[:-1]
                song['Positiveness'] = positiveness[:-1]
                song['Liveness'] = liveness[:-1]
                song['Energy'] = energy[:-1]
                song['speechness'] = speechness[:-1]
                break
            except Exception:
                print("Could not scrape for: ", title)
                browser.quit()
                first = 0
                tries += 1
                if tries > 1:
                    tries = 0
                    break
                continue
    with open(filename, 'w') as f:
        f.write(json.dumps(songs, indent=4))
    return songs