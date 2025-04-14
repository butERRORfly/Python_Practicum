import requests


def sum_all_server_data():
    server_address = input().strip()
    paths = []
    while True:
        try:
            path = input().strip()
            if not path:
                break
            paths.append(path)
        except EOFError:
            break

    if not server_address.startswith(('http://', 'https://')):
        server_address = 'http://' + server_address

    total = 0

    for path in paths:
        try:
            url = server_address + path

            response = requests.get(url, timeout=5)
            response.raise_for_status()

            data = response.json()

            if isinstance(data, list):
                for item in data:
                    if isinstance(item, (int, float)):
                        total += item

        except (requests.exceptions.RequestException, ValueError):
            continue

    print(total)


if __name__ == "__main__":
    sum_all_server_data()
