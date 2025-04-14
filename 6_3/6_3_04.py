import requests


def get_value_from_server():
    server_address = input().strip()
    key = input().strip()

    if not server_address.startswith(('http://', 'https://')):
        server_address = 'http://' + server_address

    try:
        response = requests.get(server_address, timeout=5)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, dict):
            print("No data")
            return

        value = data.get(key)
        if value is not None:
            print(value)
        else:
            print("No data")

    except (requests.exceptions.RequestException, ValueError):
        print("No data")


if __name__ == "__main__":
    get_value_from_server()
