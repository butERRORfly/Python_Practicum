import requests
import json
import sys


def add_new_user():
    server_address = input().strip()
    username = input().strip()
    last_name = input().strip()
    first_name = input().strip()
    email = input().strip()

    if not server_address.startswith(('http://', 'https://')):
        server_address = 'http://' + server_address

    user_data = {
        "username": username,
        "last_name": last_name,
        "first_name": first_name,
        "email": email
    }

    try:
        response = requests.post(
            f"{server_address}/users",
            json=user_data,
            timeout=5
        )
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        raise Exception


if __name__ == "__main__":
    add_new_user()
