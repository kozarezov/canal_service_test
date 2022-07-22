import os
import json
from http import HTTPStatus
from datetime import datetime

from sheetfu import SpreadsheetApp
from dotenv import load_dotenv
import requests

from .models import Order

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Api():
    """Соединение с API Google и сбор информации."""

    DOCUMENT_ID = os.getenv('DOCUMENT_ID')
    CBR_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def __init__(self) -> None:
        """Инициализация, соединение с API и книгой."""
        try:
            sa = SpreadsheetApp(
                os.path.join(os.path.dirname(__file__), 'service.json')
            )
        except Exception:
            raise Exception('Неудачная попытка соединения с API')

        try:
            self.spreadsheet = sa.open_by_id(self.DOCUMENT_ID)
            self.sheet = self.spreadsheet.get_sheet_by_name('Лист1')
            self.data_range = self.sheet.get_data_range()
        except Exception:
            raise Exception('Неудачная попытка соединения с книгой')

    def get_values(self) -> list:
        """Получение данных из книги."""
        HEADERS = ['№', 'заказ №', 'стоимость,$', 'срок поставки']
        try:
            all_values = self.data_range.get_values()
            headers = all_values[:1][0]
            if headers != HEADERS:
                raise Exception('Неверное расположение столбцов')
            values = all_values[1:]
        except Exception:
            raise Exception('В книге нет данных')
        else:
            return values

    def get_course(self) -> float:
        """Получение курса доллара с сайта центробанка."""
        response = requests.get(self.CBR_URL)

        if response.status_code != HTTPStatus.OK:
            raise Exception('Сайт центробанка не доступен')

        try:
            course = response.json()['Valute']['USD']['Value']
        except json.JSONDecodeError:
            raise json.JSONDecodeError('Неверные данные в response')
        else:
            return course


class ParseData():
    """Парсинг и сохранение данных в базу данных"""

    def __init__(self) -> None:
        """Инициализация, получение данных."""
        api = Api()
        self.course = api.get_course()
        self.values = api.get_values()

    def save(self, order: list) -> None:
        obj, created = Order.objects.get_or_create(order_id=order[0])

        obj.number = order[1]
        obj.cost_dollar = order[2]
        obj.cost_ruble = round(order[2] * self.course, 2)
        obj.date = datetime.date(order[3])

    def parsing(self) -> None:
        """Обработка полученных данных."""
        exclude_list = Order.objects.values_list('order_id')
        print(exclude_list)

        for order in self.values:
            self.save(order)
        


def script() -> None:
    """Основной скрипт программы."""
    ParseData().parsing()


if __name__ == '__main__':
    script()