import requests


def sum_server_data():
    server_address = input().strip()
    if not server_address.startswith(('http://', 'https://')):
        server_address = 'http://' + server_address

    try:
        response = requests.get(server_address, timeout=5)
        response.raise_for_status()

        data = response.json()
        if not isinstance(data, list):
            print(0)
            return

        total = 0
        for item in data:
            if isinstance(item, (int, float)):
                total += item

        print(total)

    except (requests.exceptions.RequestException, ValueError):
        print(0)


if __name__ == "__main__":
    sum_server_data()
