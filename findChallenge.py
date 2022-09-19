#!.\venv\Scripts\python
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

from src.Challenger import Challenger

options = Options()

options.headless = True

service = Service()

driver = WebDriver(service=service, options=options)

challenger = Challenger(driver)

file = challenger.getChallenges()
