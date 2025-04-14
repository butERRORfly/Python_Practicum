import requests


def delete_user():
    server_address = input().strip()
    user_id = input().strip()

    if not server_address.startswith(('http://', 'https://')):
        server_address = 'http://' + server_address

    try:
        response = requests.delete(
            f"{server_address}/users/{user_id}",
            timeout=5
        )
        response.raise_for_status()

    except requests.exceptions.RequestException:
        raise Exception


if __name__ == "__main__":
    delete_user()
