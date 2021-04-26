import json
from selenium import webdriver
from fake_useragent import UserAgent


def amazon_get_songs(pages):
    # Genres links
    rock_url = "https://www.amazon.com/s?i=digital-music-track&bbn=625129011&rh=n%3A625129011%2Cp_72%3A1248981011%2Cp_n_feature_browse-bin%3A625151011&dc&qid=1619266221&rnid=625149011&ref=sr_pg_1"
    pop_url = "https://www.amazon.com/s?i=digital-music-track&bbn=625092011&rh=n%3A625092011%2Cp_n_feature_browse-bin%3A625151011%2Cp_72%3A1248981011&dc&qid=1619265272&rnid=1248979011&ref=sr_pg_1"
    country_url = "https://www.amazon.com/s?i=digital-music-track&bbn=624976011&rh=n%3A624976011%2Cp_n_feature_browse-bin%3A625151011%2Cp_72%3A1248981011&dc&qid=1619266335&rnid=1248979011&ref=sr_pg_1"
    hiphop_url = "https://www.amazon.com/s?i=digital-music-track&bbn=625117011&rh=n%3A625117011%2Cp_n_feature_browse-bin%3A625151011%2Cp_72%3A1248981011&dc&qid=1619266251&rnid=1248979011&ref=sr_pg_1"
    urls = [rock_url, pop_url, country_url, hiphop_url]

    songs = []
    tries = 0
    for url, genre in zip(urls, ['rock', 'pop', 'country', 'hiphop']):
        count = 0
        first = 0
        ur = url
        for i in range(1, pages + 1):
            while True:
                if first == 0:
                    # every genre run with different browser profile
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument("--start-maximized")
                    # Adding fake google user to avoid captcha
                    ua = UserAgent()
                    userAgent = ua.random
                    print(f"Starting to scrape for {genre} with the user agent: {userAgent}")
                    chrome_options.add_argument(f'user-agent={userAgent}')  # bypass captcha
                    browser = webdriver.Chrome('./chromedriver', options=chrome_options)
                    first += 1
                try:
                    if i == 2:
                        b = ur.split('qid')[0] + 'page=2'
                        c = "&qid" + ur.split('qid')[1]
                        ur = b + c
                    elif i > 2:
                        ur = ur.replace(f"&page={i - 1}", f"&page={i}")
                    browser.get(ur)
                    divs = browser.find_elements_by_xpath(
                        '*//div[@class="s-include-content-margin s-border-bottom s-latency-cf-section"]')
                    for div in divs:
                        title = div.find_element_by_tag_name("h2").text
                        artist = div.find_element_by_xpath(
                            '*//div[@class="a-row a-size-base a-color-secondary"]').text  # get the artist
                        artist = artist.split("by ")[1]
                        songs.append({"Genre": genre, "Title": title, "Artist": artist})
                        count += 1
                    break
                except Exception:
                    browser.quit()
                    first = 0
                    tries += 1
                    if tries > 1:  # if its the second time trying to scrape the page then move to the next
                        tries = 0
                        break
                    continue
        print(f"Successfuly scraped {count} songs for {genre}\n")
        browser.quit()
    with open('songs.json', 'w') as f:
        f.write(json.dumps(songs, indent=4))
    return songs
