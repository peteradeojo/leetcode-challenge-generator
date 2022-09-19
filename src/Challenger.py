from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import os
from pprint import pprint
import json
from datetime import date, datetime


class Challenger:
    browser: WebDriver
    url = "https://leetcode.com/problemset/algorithms/?sorting=W3sic29ydE9yZGVyIjoiQVNDRU5ESU5HIiwib3JkZXJCeSI6IkRJRkZJQ1VMVFkifV0%3D"

    def __init__(self, driver: WebDriver, url=None) -> None:
        self.browser = driver
        if url:
            self.url = url

    def loadProblems(self):
        links = []
        self.browser.get(self.url)

        for i in range(2, 7):
            el = WebDriverWait(
                self.browser,
                20,
                ignored_exceptions=(NoSuchElementException,
                                    StaleElementReferenceException)
            ).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    f"div[role='rowgroup'] div[role='row']:nth-child({i}) div[role='cell']:nth-child(2) a"
                )))

            links.append({"title": el.text, "link": el.get_attribute('href')})

        return links

    def getChallenges(self):
        links = self.loadProblems()

        for link in links:
            self.browser.get(link['link'])

            description = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "description__24sA")))

            year, week, day = datetime.today().isocalendar()

            dirname = f"./screenshots/{year}-{week}/"
            if not os.path.exists(dirname):
                os.makedirs(dirname)

            with open(dirname + link['title'] + ".png", "wb") as file:
                file.write(description.screenshot_as_png)

            link['description'] = dirname + link['title'] + ".png"

        self.browser.quit()
        return self.saveLinksToJson(links)

    def saveLinksToJson(self, data):
        year, week, day = datetime.today().isocalendar()
        filename = f"{year}-{week}.json"

        with open(filename, "w+") as file:
            file.write(json.dumps(data))

        return filename
