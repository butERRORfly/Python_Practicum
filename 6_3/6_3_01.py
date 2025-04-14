import requests


def get_server_message():
    try:
        response = requests.get('http://127.0.0.1:5000')

        response.raise_for_status()

        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при обращении к серверу: {e}")


if __name__ == "__main__":
    get_server_message()
