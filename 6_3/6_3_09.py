import requests
import sys


def update_user():
    server_address = input().strip()
    user_id = input().strip()

    update_data = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        key, value = line.split('=', 1)
        update_data[key] = value

    if not server_address.startswith(('http://', 'https://')):
        server_address = 'http://' + server_address

    try:
        response = requests.put(
            f"{server_address}/users/{user_id}",
            json=update_data,
            timeout=5
        )
        response.raise_for_status()

    except requests.exceptions.RequestException:
        raise Exception


if __name__ == "__main__":
    update_user()
