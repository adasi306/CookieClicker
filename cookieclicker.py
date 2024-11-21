from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

check_interval = 5
timeout = time.time() + check_interval
play_time = time.time() + 300


def get_cookie_count() -> int:
    money: str = driver.find_element(By.ID, "money").text
    return int(money.replace(",", ""))


def get_item_prices() -> list:
    prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
    item_prices: list = []
    for price in prices:
        text: str = price.text
        if "-" in text:
            cost: int = int(text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)
    return item_prices


def get_affordable_upgrades(cookie_count: int, upgrades: dict) -> dict:
    affordable: dict = {}
    for cost, id in upgrades.items():
        if cookie_count >= cost:
            affordable[cost] = id
    return affordable


while True:
    cookie.click()

    if time.time() > timeout:
        cookie_count: int = get_cookie_count()
        item_prices: list = get_item_prices()
        upgrades: dict = dict(zip(item_prices, item_ids))
        affordable_upgrades: dict = get_affordable_upgrades(cookie_count, upgrades)

        if affordable_upgrades:
            highest_price: int = max(affordable_upgrades.keys())
            to_purchase_id: str = affordable_upgrades[highest_price]
            driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + check_interval

    if time.time() > play_time:
        cps: str = driver.find_element(By.ID, "cps").text
        print(f"Cookies per second: {cps}")
        break
