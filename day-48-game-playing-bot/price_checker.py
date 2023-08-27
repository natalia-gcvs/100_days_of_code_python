from selenium.webdriver.common.by import By
from price_data import PriceData


class PriceChecker:
    def compare_prices(self, driver):
        price_data = PriceData(
            money=int(driver.find_element(By.ID, "money").get_attribute("textContent").replace(",", "")),
            cursor=[{'click': driver.find_element(By.CSS_SELECTOR, '#buyCursor')},
                    {'price': int(
                        driver.find_element(By.CSS_SELECTOR, '#buyCursor > b').get_attribute("textContent").split(
                            " -  ")[-1].replace(",", ""))}],
            grandma=[{'click': driver.find_element(By.CSS_SELECTOR, '#buyGrandma')},
                     {'price': int(
                         driver.find_element(By.CSS_SELECTOR, '#buyGrandma > b').get_attribute("textContent").split(
                             " -  ")[-1].replace(",", ""))}],
            factory=[{'click': driver.find_element(By.CSS_SELECTOR, '#buyFactory')},
                     {'price': int(
                         driver.find_element(By.CSS_SELECTOR, '#buyFactory > b').get_attribute("textContent").split(
                             " -  ")[-1].replace(",", ""))}],
            mine=[{'click': driver.find_element(By.CSS_SELECTOR, '#buyMine')},
                  {'price': int(
                      driver.find_element(By.CSS_SELECTOR, '#buyMine > b').get_attribute("textContent").split(" -  ")[
                          -1].replace(",", ""))}],
            shipment=[{'click': driver.find_element(By.CSS_SELECTOR, '#buyShipment')},
                      {'price': int(
                          driver.find_element(By.CSS_SELECTOR, '#buyShipment > b').get_attribute("textContent").split(
                              " -  ")[-1].replace(",", ""))}],
            alchemy_lab=[{'click': driver.find_element(By.ID, 'buyAlchemy lab')},
                         {'price': int(
                             driver.find_element(By.CSS_SELECTOR, '#buyAlchemy\ lab > b').get_attribute(
                                 "textContent").split(" -  ")[-1].replace(",", ""))}],
            portal=[{'click': driver.find_element(By.CSS_SELECTOR, '#buyPortal')},
                    {'price': int(
                        driver.find_element(By.CSS_SELECTOR, '#buyPortal > b').get_attribute("textContent").split(
                            " -  ")[-1].replace(",", ""))}],
            time_machine=[{'click': driver.find_element(By.CSS_SELECTOR, '#buyTime\ machine')},
                         {'price': int(
                             driver.find_element(By.CSS_SELECTOR, '#buyTime\ machine > b').get_attribute(
                                 "textContent").split(" -  ")[-1].replace(",", ""))}],

        )
        money = price_data.money
        price_dict = [{'click': price_data.cursor[0]['click'], 'price': price_data.cursor[1]['price']},
                      {'click': price_data.grandma[0]['click'], 'price': price_data.grandma[1]['price']},
                      {'click': price_data.factory[0]['click'],'price': price_data.factory[1]['price']},
                      {'click': price_data.mine[0]['click'],'price': price_data.mine[1]['price']},
                      {'click': price_data.shipment[0]['click'], 'price': price_data.shipment[1]['price']},
                      {'click': price_data.alchemy_lab[0]['click'], 'price': price_data.alchemy_lab[1]['price']},
                      {'click': price_data.portal[0]['click'], 'price': price_data.portal[1]['price']},
                      {'click': price_data.time_machine[0]['click'], 'price': price_data.time_machine[1]['price']},
                      ]

        affordable_upgrades = [{'click': upgrade['click'], 'price': upgrade['price']} for upgrade in price_dict if money > upgrade['price']]
        higher_price = 0
        higher_price_click = None
        for value in affordable_upgrades:
            if value['price'] > higher_price:
                higher_price = value['price']
                higher_price_click = value['click']
        return higher_price_click





