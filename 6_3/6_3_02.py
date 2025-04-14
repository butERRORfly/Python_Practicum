import requests


def sum_server_data():
    server_address = input().strip()
    if not server_address.startswith(('http://', 'https://')):
        server_address = 'http://' + server_address

    total = 0
    while True:
        try:
            response = requests.get(server_address, timeout=5)
            response.raise_for_status()
            number = int(response.text.strip())

            if number == 0:
                break

            total += number

        except (requests.exceptions.RequestException, ValueError):
            break

    print(total)


if __name__ == "__main__":
    sum_server_data()
