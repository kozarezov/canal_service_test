import os
import json
from http import HTTPStatus

from sheetfu import SpreadsheetApp
from dotenv import load_dotenv
import requests

load_dotenv('../canal/.env')


class Api():
    """Соединение с API Google и сбор информации."""

    DOCUMENT_ID = os.getenv('DOCUMENT_ID')
    CBR_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def __init__(self) -> None:
        """Инициализация, соединение с API и книгой."""
        try:
            sa = SpreadsheetApp('service.json')
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
        try:
            all_values = self.data_range.get_values()
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


if __name__ == '__main__':
    print(Api().get_course())
