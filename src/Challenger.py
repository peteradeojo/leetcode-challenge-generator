from time import sleep
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import os
import json
from datetime import datetime
import cloudinary.uploader
import os


class Challenger:
    browser: WebDriver
    url = "https://leetcode.com/problemset/algorithms/?sorting=W3t9XQ%3D%3D"

    def __init__(self, driver: WebDriver, url=None) -> None:
        self.browser = driver
        if url:
            self.url = url

    def loadProblems(self) -> list:
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

    def getChallenges(self) -> list:
        links = self.loadProblems()

        for link in links:
            self.browser.get(link['link'])

            sleep(2)

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
        return links


class Saver:

    def saveLinksToJson(self, data, filename=None) -> str:
        year, week, day = datetime.today().isocalendar()
        if filename is None:
            filename = f"{year}-{week}.json"

        with open(filename, "w+") as file:
            file.write(json.dumps(data))

        return filename


class Uploader:

    def save(self, file, folder):
        result = cloudinary.uploader.upload(
            file, folder=f"/leetcode-challenges/{folder}", overwrite=True)
        print(result)
        return result['secure_url']
