# # Python-бібліотека requests дозволяє легко працювати з HTTP-запитами.
# # •  GET-запит: Отримання даних із сервера.
# # •  POST-запит: Надсилання даних на сервер.
# # Парсинг (scraping) означає автоматичне зчитування даних зі сторінок веб-сайтів.
# # Для цього часто використовують бібліотеку BeautifulSoup.
# # На деяких сайтах парсинг може бути заборонений
#
#
#
# # import requests
# # from bs4 import BeautifulSoup
# #
# # class Сoinmarket:
# #     def __init__(self,url):
# #         self.url=url
# #         self.headers={
# #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
# #         }
# #         self.soup=None
# #
# #     def fetch_page(self):
# #             #відправка запроса
# #             response = requests.get(self.url, headers=self.headers) #+++
# #             if response.status_code==200:
# #                 self.soup=BeautifulSoup(response.text,"html.parser")
# #             else:
# #                 raise Exception("Не вдалося під'єднатися до сайту")
# #     def getInfo(self):
# #         coins=[]
# #         table=self.soup.find('tbody')
# #         if not table: raise Exception ("Не вдалося знайти таблицю")
# #         rows=table.find_all('tr')[:5]
# #         for i in rows:
# #             nameCoin=i.find("p",class_="coin-item-name") #назва монетки
# #             name=nameCoin.text.strip() if nameCoin else "Назва монетки відсутня"
# #             priceCoin=i.find("div",class_="sc-b3fc6b7-0 dzgUIj") #ціна монетки
# #             price = priceCoin.text.strip() if priceCoin else "Ціна монетки відсутня"
# #
# #             coins.append(
# #                 {
# #                     "Назва":name,
# #                     "Ціна": price
# #                 }
# #             )
# #         return  coins
# #     def printInfo(self,coins):
# #         for i,j in enumerate(coins,start=1):
# #             print(i,") Монетка")
# #             print('\t','Назва:',j['Назва'])#++
# #             print('\t', 'Ціна:', j['Ціна'])
# #         print('='*40,'\n')
# #
# # if __name__ == "__main__":
# #     url="https://coinmarketcap.com/"
# #     parse=Сoinmarket(url)
# #     try:
# #         parse.fetch_page()
# #         coin=parse.getInfo()
# #         parse.printInfo(coin)
# #     except Exception as e:
# #         print(e)
#
#
#
# import requests
# from bs4 import BeautifulSoup
#
# class Minfin:
#     def __init__(self,url):
#         self.url=url
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup=None
#
#     def fetch_page(self):
#             #Відправка запроса
#             response = requests.get(self.url, headers=self.headers)
#             if response.status_code==200:
#                 self.soup=BeautifulSoup(response.text,"html.parser")
#             else:
#                 raise Exception("Не вдалося під'єднатися до сайту")
#     def getInfo(self):
#         Currency = []
#         table = self.soup.find_all('tr', class_="sc-1x32wa2-4 dKDsVV")
#         if not table: raise Exception("Не вдалося знайти таблицю валют")
#         for i in table[1:6]:
#             nameCurrency = i.find("a", class_="sc-1x32wa2-7 ciClTw")
#             name = nameCurrency.text.strip() if nameCurrency else "Назва валюти відсутня"
#             price = i.find_all("td")
#             if len(price) >= 3:
#                 purchase = price[1].text.strip()  # Купівля
#                 sales = price[2].text.strip()  # Продаж
#             else:
#                 purchase = "Ціна купівлі відсутня"
#                 sales = "Ціна продажу відсутня"
#             Currency.append(
#                 {
#                     "Назва:": name,
#                     "Купівля:": purchase,
#                     "Продаж:": sales
#                 }
#             )
#
#         return Currency
#     def printInfo(self,Currency):
#         for i,j in enumerate(Currency,start=1):
#             print(i, ")")
#             print("\tНазва:", j['Назва:'])
#             print("\tКупівля:", j['Купівля:'])
#             print("\tПродаж:", j['Продаж:'])
#         print('='*40,'\n')
#
# if __name__ == "__main__":
#     url="https://minfin.com.ua/ua/currency/"
#     parse=Minfin(url)
#     try:
#         parse.fetch_page()
#         Currency=parse.getInfo()
#         parse.printInfo(Currency)
#     except Exception as e:
#         print(e)
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import requests
# # from bs4 import BeautifulSoup
# #
# # class ComfyParser:
# #     def __init__(self, url):
# #         """
# #         Ініціалізація об'єкта для парсингу.
# #         :param url: URL сторінки для парсингу.
# #         """
# #         self.url = url
# #         self.headers = {
# #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
# #         }
# #         self.soup = None  # Об'єкт BeautifulSoup для парсингу HTML
# #
# #     def fetch_page(self):
# #         """
# #         Завантажує HTML сторінки.
# #         """
# #         response = requests.get(self.url, headers=self.headers)  # Надсилаємо запит
# #         if response.status_code == 200:
# #             self.soup = BeautifulSoup(response.text, "html.parser")  # Ініціалізуємо парсер
# #         else:
# #             raise Exception("Не вдалося під'єднатися до сайту")
# #
# #     def get_info(self):
# #         """
# #         Парсить всю доступну інформацію про товари на сторінці.
# #         :return: Список зі словниками, що містять інформацію про товари.
# #         """
# #         products = []  # Список для зберігання інформації про продукти
# #         product_cards = self.soup.find_all('div', class_='products-catalog')  # Знаходимо всі товари
# #другая ссылка
# #         if not product_cards:
# #             raise Exception("Не вдалося знайти товари на сторінці")
# #
# #         for product in product_cards:
# #             # Назва продукту
# #             title_elem = product.find('a', class_='prdl-item__name ellipsis-2-lines')
# #             title = title_elem.text.strip() if title_elem else "Назва відсутня"
# #
# #             # Ціна продукту
# #             price_elem = product.find('div', class_='products-list-item-price__actions-price-current')
# #             price = price_elem.text.strip() if price_elem else "Ціна відсутня"
# #
# #             # Додаємо інформацію про продукт до списку
# #             products.append({
# #                 "Назва": title,
# #                 "Ціна": price,
# #             })
# #
# #         return products
# #
# #     def print_info(self, products):
# #         """
# #         Виводить інформацію про товари у вигляді таблиці.
# #         :param products: Список зі словниками, що містять інформацію про товари.
# #         """
#             # цикл додати
# #         # Виводимо заголовок таблиці
# #         print(f"{'№':<5} {'Назва':<50} {'Ціна':<20}")
# #         print("-" * 75)
# #
# #         # Виводимо інформацію про кожен продукт
# #         for index, product in enumerate(products, start=1):
# #             print(f"{index:<5} {product['Назва']:<50} {product['Ціна']:<20}")
# #
# # if __name__ == "__main__":
# #     url = "https://comfy.ua/ua/black-friday/cat__120/?gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswyhJ-lMrSryvvEIyf_s3FPnjgF7ydctFE_R10Yj_zj9l231aRd-ZIeAaAmjrEALw_wcB"
# #     parser = ComfyParser(url)
# #
# #     try:
# #         parser.fetch_page()  # Завантажуємо сторінку
# #         products = parser.get_info()  # Отримуємо інформацію про товари
# #         parser.print_info(products)  # Виводимо інформацію у вигляді таблиці
# #     except Exception as e:
# #         print(f"Помилка: {e}")
#
#
#
#
# import requests
# from bs4 import BeautifulSoup
#
# class Minfin:
#     def __init__(self, url):
#         self.url = url
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup = None
#
#     def fetch_page(self):
#         response = requests.get(self.url, headers=self.headers)
#         if response.status_code == 200:
#             self.soup = BeautifulSoup(response.text, "html.parser")
#         else:
#             raise Exception("Не вдалося під'єднатися до сайту")
#
#     def getInfo(self):
#         currency = []
#         table = self.soup.find_all('tr', class_="sc-1x32wa2-4 dKDsVV")
#         if not table:
#             raise Exception("Не вдалося знайти таблицю")
#         for i in table[1:6]:
#             name_currency = i.find("a", class_="sc-1x32wa2-7 ciClTw")
#             name = name_currency.text.strip() if name_currency else "Назва відсутня"
#             price = i.find_all("td")
#             if len(price) >= 3:
#                 purchase = price[1].text.strip().replace(',', '')
#                 sales = price[2].text.strip().replace(',', '')
#             else:
#                 purchase = "Не доступний"
#                 sales = "Не доступний"
#             currency.append(
#                 {
#                     "Назва": name,
#                     "Купити": purchase,
#                     "Продати": sales
#                 }
#             )
#         return currency
#
#     def printInfo(self, currency):
#         for i, j in enumerate(currency, start=1):
#             print(i, ")")
#             print("\tНазва", j['Назва'])
#             print("\tКупити:", j['Купити'])
#             print("\tПродати:", j['Продати'])
#         print('=' * 40, '\n')
#
#
# if __name__ == "__main__":
#     url = "https://minfin.com.ua/ua/currency/"
#     parse = Minfin(url)
#     try:
#         parse.fetch_page()
#         currency = parse.getInfo()
#         parse.printInfo(currency)
#     except Exception as e:
#         print(e)
#
#     operation = int(input("1 - Купити, 2 - Продати. Введіть цифру: "))
#     if operation == 1:
#         print("Купити")
#     elif operation == 2:
#         print("Продати")
#     else:
#         print("Некоректний вибір!")
#
#     currency_choice = int(input("Введіть цифру купюри: "))
#     if currency_choice < 1 or currency_choice > len(currency):
#         print("Некоректний вибір!")
#         exit()
#
#     try:
#         amount = float(input("Введіть суму: "))
#         selected_currency = currency[currency_choice - 1]
#
#         if operation == 2:
#             sales = float(selected_currency['Продати'])
#             result = amount / sales
#             print(f"Ви можете продати {result:.2f} {selected_currency['Назва']}")
#         elif operation == 1:
#             purchase = float(selected_currency['Купити'])
#             result = amount * purchase
#             print(f"Ви маєте {result:.2f} UAH")
#     except ValueError:
#         print("Некоректний вибір")


import requests
from bs4 import BeautifulSoup


class Coinmarket:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def fetch_page(self):
        # Відправка запроса
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, "html.parser")
        else:
            raise Exception("Не вдалося під'єднатися до сайту")

    def getInfo(self):
        coins = []
        table = self.soup.find('div', class_="h-market-table_limiter", id="market-table_currency-cash_limiter")
        if not table: raise Exception("Не вдалося знайти таблицю")
        for i in table:
            nameCoin = i.find_all("td", class_="c1")  # Назва монети
            name = nameCoin[0].text.strip() if nameCoin else "Назва монети відсутня"
            priceCoin = i.find_all("td", class_="c2")  # опис фильму
            price = priceCoin[0].text.strip() if priceCoin else "Ціна монети відсутня"
            priceCoin2 = i.find_all("td", class_="c3")  # опис фильму
            price2 = priceCoin2[0].text.strip() if priceCoin2 else "Ціна монети відсутня"
            cols = table.find_all('td')
            if len(cols) >= 2:  # Убедиться, что есть достаточное количество колонок
                currency = cols[0].text.strip()  # Валюта
                buy = cols[1].text.strip()  # Покупка
                sell = cols[2].text.strip()  # Продажа

            coins.append(
                {
                    "Назва:": name,
                    "Купівля:": price,
                    "Продаж:": price2
                }
            )
        return coins

    def getInfo1(self):
        coins1 = []
        table1 = self.soup.find('div', class_="h-market-table_limiter", id="market-table_currency-cash_limiter")
        if not table1: raise Exception("Не вдалося знайти таблицю")
        for i in table1:
            nameCoin1 = i.find_all("td", class_="c1")  # Назва монети
            name1 = nameCoin1[1].text.strip() if nameCoin1 else "Назва монети відсутня"
            priceCoin1 = i.find_all("td", class_="c2")  # опис фильму
            price1 = priceCoin1[1].text.strip() if priceCoin1 else "Ціна монети відсутня"
            priceCoin3 = i.find_all("td", class_="c3")  # опис фильму
            price3 = priceCoin3[1].text.strip() if priceCoin3 else "Ціна монети відсутня"
            cols1 = table1.find_all('td')
            if len(cols1) >= 2:  # Убедиться, что есть достаточное количество колонок
                currency = cols1[0].text.strip()  # Валюта
                buy = cols1[1].text.strip()  # Покупка
                sell = cols1[2].text.strip()  # Продажа

            coins1.append(
                {
                    "Назва:": name1,
                    "Купівля:": price1,
                    "Продаж:": price3
                }
            )
        return coins1

    def getInfo2(self):
        coins2 = []
        table2 = self.soup.find('div', class_="h-market-table_limiter", id="market-table_currency-cash_limiter")
        if not table2: raise Exception("Не вдалося знайти таблицю")
        for i in table2:
            nameCoin2 = i.find_all("td", class_="c1")  # Назва монети
            name2 = nameCoin2[2].text.strip() if nameCoin2 else "Назва монети відсутня"
            priceCoin4 = i.find_all("td", class_="c2")  # опис фильму
            price4 = priceCoin4[2].text.strip() if priceCoin4 else "Ціна монети відсутня"
            priceCoin5 = i.find_all("td", class_="c3")  # опис фильму
            price5 = priceCoin5[2].text.strip() if priceCoin5 else "Ціна монети відсутня"
            cols2 = table2.find_all('td')
            if len(cols2) >= 3:  # Убедиться, что есть достаточное количество колонок
                currency = cols2[0].text.strip()  # Валюта
                buy = cols2[1].text.strip()  # Покупка
                sell = cols2[2].text.strip()  # Продажа

            coins2.append(
                {
                    "Назва:": name2,
                    "Купівля:": price4,
                    "Продаж:": price5
                }
            )
        return coins2

    def getInfo3(self):
        coins3 = []
        table3 = self.soup.find('div', class_="h-market-table_limiter", id="market-table_currency-cash_limiter")
        if not table3: raise Exception("Не вдалося знайти таблицю")
        for i in table3:
            nameCoin3 = i.find_all("td", class_="c1")  # Назва монети
            name3 = nameCoin3[3].text.strip() if nameCoin3 else "Назва монети відсутня"
            priceCoin6 = i.find_all("td", class_="c2")  # опис фильму
            price6 = priceCoin6[3].text.strip() if priceCoin6 else "Ціна монети відсутня"
            priceCoin7 = i.find_all("td", class_="c3")  # опис фильму
            price7 = priceCoin7[3].text.strip() if priceCoin7 else "Ціна монети відсутня"
            cols3 = table3.find_all('td')
            if len(cols3) >= 4:  # Убедиться, что есть достаточное количество колонок
                currency = cols3[0].text.strip()  # Валюта
                buy = cols3[1].text.strip()  # Покупка
                sell = cols3[2].text.strip()  # Продажа

            coins3.append(
                {
                    "Назва:": name3,
                    "Купівля:": price6,
                    "Продаж:": price7
                }
            )
        return coins3

    def getInfo4(self):
        coins4 = []
        table4 = self.soup.find('div', class_="h-market-table_limiter", id="market-table_currency-cash_limiter")
        if not table4: raise Exception("Не вдалося знайти таблицю")
        for i in table4:
            nameCoin4 = i.find_all("td", class_="c1")  # Назва монети
            name4 = nameCoin4[4].text.strip() if nameCoin4 else "Назва монети відсутня"
            priceCoin8 = i.find_all("td", class_="c2")  # опис фильму
            price8 = priceCoin8[4].text.strip() if priceCoin8 else "Ціна монети відсутня"
            priceCoin9 = i.find_all("td", class_="c3")  # опис фильму
            price9 = priceCoin9[4].text.strip() if priceCoin9 else "Ціна монети відсутня"
            cols4 = table4.find_all('td')
            if len(cols4) >= 5:  # Убедиться, что есть достаточное количество колонок
                currency = cols4[0].text.strip()  # Валюта
                buy = cols4[1].text.strip()  # Покупка
                sell = cols4[2].text.strip()  # Продажа

            coins4.append(
                {
                    "Назва:": name4,
                    "Купівля:": price8,
                    "Продаж:": price9
                }
            )
        return coins4

    def printInfo(self, coins):
        for i, j in enumerate(coins, start=1):
            print(i, ") Валюта")
            print('\t', 'Назва:', j['Назва:'])
            print('\t', 'Купівля:', j['Купівля:'])
            print('\t', 'Продаж:', j['Продаж:'])
        print('=' * 40, '\n')

    def printInfo1(self, coins1):
        for i, j in enumerate(coins1, start=2):
            print(i, ") Валюта")
            print('\t', 'Назва:', j['Назва:'])
            print('\t', 'Купівля:', j['Купівля:'])
            print('\t', 'Продаж:', j['Продаж:'])
        print('=' * 40, '\n')

    def printInfo2(self, coins2):
        for i, j in enumerate(coins2, start=3):
            print(i, ") Валюта")
            print('\t', 'Назва:', j['Назва:'])
            print('\t', 'Купівля:', j['Купівля:'])
            print('\t', 'Продаж:', j['Продаж:'])
        print('=' * 40, '\n')

    def printInfo3(self, coins3):
        for i, j in enumerate(coins3, start=4):
            print(i, ") Валюта")
            print('\t', 'Назва:', j['Назва:'])
            print('\t', 'Купівля:', j['Купівля:'])
            print('\t', 'Продаж:', j['Продаж:'])
        print('=' * 40, '\n')

    def printInfo4(self, coins4):
        for i, j in enumerate(coins4, start=5):
            print(i, ") Валюта")
            print('\t', 'Назва:', j['Назва:'])
            print('\t', 'Купівля:', j['Купівля:'])
            print('\t', 'Продаж:', j['Продаж:'])
        print('=' * 40, '\n')


if __name__ == "__main__":
    url = "https://finance.ua/ua/currency"  # Update URL if necessary
    parser = Coinmarket(url)
    try:
        parser.fetch_page()
        exchange_rates = parser.get_exchange_rates()
        parser.print_exchange_rates(exchange_rates)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = "https://finance.ua/ua/currency"
    parse = Coinmarket(url)
    try:
        parse.fetch_page()
        parse.fetch_page()
        # f=parse.get_info()
        # в3.print_info()
        coin = parse.getInfo()
        coin1 = parse.getInfo1()
        coin2 = parse.getInfo2()
        coin3 = parse.getInfo3()
        coin4 = parse.getInfo4()
        parse.printInfo(coin)
        parse.printInfo1(coin1)
        parse.printInfo2(coin2)
        parse.printInfo3(coin3)
        parse.printInfo4(coin4)
        exchange_rates = parser.get_exchange_rates()
        parser.print_exchange_rates(exchange_rates)

    except Exception as e:
        print(e)


def get_exchange_rates():
    return {
        "USD": {"buy": 42.05, "sell": 42.66},
        "EUR": {"buy": 43.33, "sell": 44.07},
        "AED": {"buy": 10.68, "sell": 10.90},
        "AMD": {"buy": 00.09, "sell": 00.10},
        "AUD": {"buy": 23.80, "sell": 26.35},
    }


def display_exchange_rates(rates):
    print("Полученные курсы валют:")
    for i, (currency, rate) in enumerate(rates.items()):
        print(f"{i + 1}. {currency}: Покупка {rate['buy']} грн, Продажа {rate['sell']} грн")


def handle_buy(rates):
    currency_choice = get_currency_choice(rates)
    amount_uah = get_amount_uah()
    currency = list(rates.keys())[currency_choice - 1]
    exchange_rate = rates[currency]['sell']
    amount_currency = amount_uah / exchange_rate
    print(f"Вы хотите купить {currency} за {amount_uah} грн.")
    print(f"Вы получите: {amount_currency:.2f} {currency} по курсу {exchange_rate} гривен.")


def handle_sell(rates):
    currency_choice = get_currency_choice(rates)
    amount_currency = get_amount_currency()
    currency = list(rates.keys())[currency_choice - 1]
    exchange_rate = rates[currency]['buy']
    amount_uah = amount_currency * exchange_rate
    print(f"Вы хотите продать {amount_currency:.2f} {currency}.")
    print(f"Вы получите: {amount_uah:.2f} грн по курсу {exchange_rate} гривен.")


def get_currency_choice(rates):
    for i, currency in enumerate(rates):
        print(f"{i + 1}. {currency}")
    while True:
        try:
            choice = int(input("Выберите валюту (введите число из списка): "))
            if 1 <= choice <= len(rates):
                return choice
            else:
                print("Неверный номер валюты.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")


def get_amount_uah():
    while True:
        try:
            amount = float(input("Введите сумму в гривнах: "))
            if amount > 0:
                return amount
            else:
                print("Сумма должна быть больше нуля.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")


def get_amount_currency():
    while True:
        try:
            amount = float(input("Введите сумму валюты: "))
            if amount > 0:
                return amount
            else:
                print("Сумма должна быть больше нуля.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")


if __name__ == "__main__":
    rates = get_exchange_rates()
    display_exchange_rates(rates)

    while True:
        try:
            action = int(input("Выберите действие:\n1. Покупка\n2. Продажа\n> "))
            if action == 1:
                handle_buy(rates)
                break
            elif action == 2:
                handle_sell(rates)
                break
            else:
                print("Неверный выбор действия.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")