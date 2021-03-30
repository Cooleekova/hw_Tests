import unittest
import requests
from datetime import datetime


token = '*** СЮДА НУЖНО ВВЕСТИ ТОКЕН ЯНДЕКС ДИСКА ***'


class TestYandexAPINewFolder(unittest.TestCase):

    # тестируем, что запрос на создание новой папки получает ответ 201
    def test_status_200(self):
        folder_name = f'Папка {datetime.now().strftime("%H.%M.%S")}'
        new_folder = requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            params={'path': folder_name},
            headers={"Authorization": token},
        )
        self.assertEqual(201, new_folder.status_code)

    # тестируем, что новая папка появилась в списке файлов на Яндекс.Диске
    def test_new_folder_created(self):
        folder_name = f'Папка {datetime.now().strftime("%H.%M.%S")}'
        requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            params={'path': folder_name},
            headers={"Authorization": token},
        )
        response = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources?path=%2F',
            params={'path': '%2F'},
            headers={"Authorization": token},
        )
        data = response.json()['_embedded']['items']
        names = list()
        for item in data:
            names.append(item['name'])
        self.assertIn(folder_name, names)

    # тестируем, что API возвращает ошибку 409,
    # если папка с таким именем уже сущестует
    def test_folder_name_exists(self):
        folder_name = 'Папка'
        requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            params={'path': folder_name},
            headers={"Authorization": token},
        )
        second_new_folder = requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            params={'path': folder_name},
            headers={"Authorization": token},
        )
        self.assertEqual(409, second_new_folder.status_code)


if __name__ == '__main__':
    unittest.main()
