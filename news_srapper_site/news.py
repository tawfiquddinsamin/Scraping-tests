from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import time
import pandas as pd

def scrape_news():

    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-dev-shm-usage')

    chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36')

    driver = webdriver.Chrome(options=chrome_options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    driver.get("https://www.prothomalo.com/collection/latest")
    time.sleep(5)
    headlines = []
    details_links = []
    details = []

    for article in driver.find_elements(By.XPATH, "//*[@id='container']/div/div[2]/div/div/div[1]/div/div/div"):
        for headline in article.find_elements(By.CLASS_NAME, "headline-title"):
            print(headline.text)
            headlines.append(headline.text)
        for detail in article.find_elements(By.CLASS_NAME, "title-link"):
            link = detail.get_attribute("href")
            print(link)
            details_links.append(link)

    print(len(headlines))
    print(len(details_links))



    df = pd.DataFrame({"Headline": headlines, "Detail_link": details_links, })
    df.to_csv("news_articles.csv", index=False)

    headlines=[]
    details_links=[]
    driver.get("https://www.kalerkantho.com/special/recent")
    time.sleep(30)

    for article in driver.find_elements(By.XPATH, '//*[@id="__next"]/main/section/div/div/div'):
        for headline in article.find_elements(By.CLASS_NAME, "card-title"):
            print(headline.text)
            headlines.append(headline.text)
        for detail in article.find_elements(By.CLASS_NAME, "text-dark"):
            link = detail.get_attribute("href")
            print(link)
            details_links.append(link)

    print(len(headlines))
    print(len(details_links))

    df = pd.DataFrame({"Headline": headlines, "Detail_link": details_links, })
    df.to_csv("news_kaler_kontho.csv", index=False)

    headlines=[]
    details_links=[]

    driver.get("https://www.dailyamardesh.com/latest")

    for article in driver.find_elements(By.XPATH, '/html/body/section/div[2]'):
        for headline in article.find_elements(By.CLASS_NAME, "text-contrast1"):
            print(headline.text)
            headlines.append(headline.text)
        for detail in article.find_elements(By.CLASS_NAME, "inline"):
            link=detail.get_attribute("href")
            print(detail.text)
            details_links.append(link)
    print(len(headlines))
    print(len(details_links))

    df = pd.DataFrame({"Headline": headlines, "Detail_link": details_links, })
    df.to_csv("news_daily_amardesh.csv", index=False)
    driver.quit()
if __name__ == "__main__":
    scrape_news()