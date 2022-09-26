#!./venv/Scripts/python
from datetime import datetime
import json
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

import dotenv

dotenv.load_dotenv()

from src.Challenger import Challenger, Saver, Uploader
from src.Notifier import Notifier

options = Options()

options.headless = True

service = Service()

driver = WebDriver(service=service, options=options)

challenger = Challenger(driver)
uploader = Uploader()

links = challenger.getChallenges()

file = Saver().saveLinksToJson(links)

# file = "2022-38-1.json"
with open(file, 'r') as file:
    data = json.loads(file.read())
    year, week, day = datetime.today().isocalendar()
    for item in data:
        url = uploader.save(item['description'], f"{year}-{week}")
        item['description'] = url

    notifier = Notifier()

    notifier.post(data)
