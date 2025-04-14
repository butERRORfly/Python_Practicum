import requests
import sys


def prepare_email():
    server_address = input().strip()
    user_id = input().strip()

    message_template = sys.stdin.read().strip()

    if not server_address.startswith(('http://', 'https://')):
        server_address = 'http://' + server_address

    try:
        response = requests.get(f"{server_address}/users/{user_id}", timeout=5)

        if response.status_code == 404:
            print("Пользователь не найден")
            return

        response.raise_for_status()
        user_data = response.json()

        try:
            formatted_message = message_template.format(**user_data)
            print(formatted_message)
        except KeyError as e:
            print(f"Ошибка: отсутствует поле {e} в данных пользователя")

    except requests.exceptions.RequestException:
        print("Ошибка соединения с сервером")


if __name__ == "__main__":
    prepare_email()
